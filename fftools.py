import hashlib
import errno
import sys
import os
import platform
import subprocess
import tempfile

all_modules = [ "yasm", "nasm", "gpg_error", "gcrypt", "opencl",
            "sdl2", "sdl2_ttf",
            "ladspa", "frei0r", "fribidi", "harfbuzz", "libass", "caca", "gsm", "modplug",
            "rtmp",
            "celt", "lame", "ogg", "opus", "vorbis", "speex", "fdkaac", "twolame", "wavpack",
            "openjpeg",
            "webp", "theora", "vpx", "x264", "openh264", "x265", "xvid",
            "live555" ];

def highlight(msg):
    return "\x1b[1m" + msg + "\x1b[m";

def red(msg):
    return "\x1b[1;31m" + msg + "\x1b[m";

def yellow(msg):
    return "\x1b[1;33m" + msg + "\x1b[m";

def green(msg):
    return "\x1b[1;32m" + msg + "\x1b[m";

def error(msg):
    return red(msg);

def info(msg):
    return yellow(msg);

def ok(msg):
    return green(msg);

def errq(msg):
    print(error(msg));
    sys.exit(-1);

def usage():
    print("""
Options:
    -h, --help                 Show this message
    -v, --version              Show package version
    --prefix [prefix]          Specify prefix directory
    --modules [module[,...]]   Build and install selected modules
    --disable [module[,...]]   Do not build selected modules
    --make [options]           Additional make options
    --force                    Rebuild all modules
    --rebuild [module[,...]]   Rebuild selected modules
""");

def dump_modules(msg, mods):
    print(highlight(msg), end='');
    print(" ".join(mods));
    print(ok("### {} module(s) activated".format(len(mods))));

def msys_sysname():
    if platform.system().lower()[:4] != "msys": return None;
    bits = 32;
    if platform.machine() == "x86_64": bits = 64;
    return "{}-w{}-mingw32".format(platform.machine(), bits);

def guess_dirname(fn):
    fn = os.path.basename(fn);
    if fn[-8:] == ".tar.bz2":   return fn[0:-8];
    if fn[-7:] == ".tar.gz":    return fn[0:-7];
    if fn[-7:] == ".tar.xz":    return fn[0:-7];
    if fn[-4:] == ".tgz":       return fn[0:-4];
    if fn[-4:] == ".tbz":       return fn[0:-4];
    if fn[-4:] == ".zip":       return fn[0:-4];
    if fn[-4:] == ".git":       return fn;
    idx = fn.find(".");
    if idx < 0: return fn;
    return fn[:idx];

def create_dir(dn):
    try: os.mkdir(dn)
    except OSError as e:
        if e.errno != errno.EEXIST or os.path.isfile(dn): raise e;

def file_exist(fn):
    try:
        os.stat(fn);
    except Exception as e:
        return False;
    return True;

def is_exe(fpath):
    return os.path.isfile(fpath) and os.access(fpath, os.X_OK);

def which(program):
    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file
    return None

def runcmd_noquit(cmd):
    return os.system(cmd);

def runcmd(cmd):
    ret = runcmd_noquit(cmd);
    if ret != 0:
        print(error("*** command '{}' failed with code {}".format(cmd, ret)));
        print(error("*** working directory: {}".format(os.getcwd())));
        sys.exit(-1)

def runcmd_output(cmd):
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return out.decode('utf-8').strip();

def pkg_config_reset():
    msys = msys_sysname();
    p = "/opt/local/lib/pkgconfig:/usr/local/lib/pkgconfig:/usr/lib/i386-linux-gnu/pkgconfig/:/usr/lib/pkgconfig";
    if msys != None:
        if msys[:5] == "x86_64": p = "/mingw64/lib/pkgconfig:" + p;
        else: p = "/mingw32/lib/pkgconfig:" + p;
    os.environ["PKG_CONFIG_PATH"] = p;
    return p;

def pkg_config_setup(prefix):
    os.environ["PKG_CONFIG_PATH"] = prefix + "/lib/pkgconfig:" + pkg_config_reset();

def pkg_config_exists(pkg):
    return True if runcmd_noquit("pkg-config --exists {}".format(pkg)) == 0 else False;

def pkg_config_version(pkg):
    if pkg_config_exists(pkg):
        return runcmd_output("pkg-config --modversion {}".format(pkg));
    return "[unknown version]";

def pkg_config_builtin(pkg):
    ret = None
    pkg_config_reset()
    if pkg_config_exists(pkg): ret = pkg_config_version(pkg);
    pkg_config_setup(os.environ["FFMPEG3"]);
    return ret;

def sysdeps_check(sysdeps):
    for d in sysdeps:
        red("Test {}".format(d));
        if pkg_config_exists(d[0]) == False:
            print(red("Package '{}' not found!".format(d[0])));
            return False
        ver = pkg_config_version(d[0])
        if d[1] == None:
            print(green("Package {} [{}] found.".format(d[0], ver)));
            continue;
        # TODO: compare version
    return True

def test_compile(headers, libs):
    test = "";
    for h in headers: test = test + "#include <{}>\n".format(h);
    test = test + "int main() { return 0; }\n";
    fout = tempfile.mkstemp(suffix=".exe");
    os.close(fout[0]);
    fsrc = tempfile.mkstemp(suffix=".c");
    os.write(fsrc[0], bytes(test, 'utf-8'));
    os.close(fsrc[0]);
    ldflags = "";
    for l in libs: ldflags = ldflags + " -l" + l;
    cmd = "gcc -o {} {} {} > /dev/null 2>&1".format(fout[1], fsrc[1], ldflags);
    if runcmd_noquit(cmd) != 0:
        print(yellow("*** Compile failed: {}, {}".format(headers, ldflags)));
        os.unlink(fsrc[1]);
        return False;
    os.unlink(fsrc[1]);
    os.unlink(fout[1]);
    return headers;

def verify_checksum(fn, checksum, alg):
    m = None;
    checksum = checksum.strip();
    if len(checksum) == 0: return True
    if alg == 'sha1':    m = hashlib.sha1();
    elif alg == 'md5':   m = hashlib.md5();
    else: return True # unsupported algorithm
    m.update(open(fn, "rb").read());
    mysum = m.hexdigest();
    if mysum != checksum: return False;
    return True;

def download(pkg):
    fname = os.path.basename(pkg.url);
    # proto other than http and ftp?
    if hasattr(pkg, 'proto'):
        if pkg.proto == "null":
            if os.path.isdir("build/"+fname): runcmd("rm -rf 'build/{}'".format(fname));
            os.mkdir("build/"+fname);
            return fname;
        elif pkg.proto == "git":
            if os.path.isdir("build/"+fname): runcmd("rm -rf 'build/{}'".format(fname));
            runcmd("git clone {} build/{}".format(pkg.url, fname));
            return fname;
    # regular file
    cachename = "cached/" + fname;
    if hasattr(pkg, 'outname'): cachename = "cached/" + pkg.outname;
    if file_exist(cachename):
        st = os.stat(cachename);
        if st.st_size > 0: return cachename;
    runcmd("wget -O {} {}".format(cachename, pkg.url));
    # verify checksum
    sha1 = "";
    if hasattr(pkg, 'sha1'): sha1 = pkg.sha1.strip();
    if len(sha1) > 0 and not verify_checksum(cachename, sha1, 'sha1'):
        errq("*** Invalid sha1 checksum (!= {})".format(sha1));
    md5 = "";
    if hasattr(pkg, 'md5'): md5 = pkg.md5.strip();
    if len(md5) > 0 and not verify_checksum(cachename, md5, 'md5'):
        errq("*** Invalid md5 checksum (!= {})".format(md5));
    return cachename;

def unpack(fn):
    if fn[-8:] == ".tar.bz2":   runcmd("tar xjf {} -C build/".format(fn));
    if fn[-7:] == ".tar.gz":    runcmd("tar xzf {} -C build/".format(fn));
    if fn[-7:] == ".tar.xz":    runcmd("xz -dc {} | tar xf - -C build/".format(fn));
    if fn[-4:] == ".tbz":       runcmd("tar xjf {} -C build/".format(fn));
    if fn[-4:] == ".tgz":       runcmd("tar xzf {} -C build/".format(fn));
    if fn[-4:] == ".zip":       runcmd("unzip -o {} -d build/".format(fn));
    # otherwise: do nothing

def cleanup(pkg):
    ccmd = "rm -rf {}".format(pkg.dirname);
    if ccmd.find("/") != -1:
        print(error("*** Invalid directory name: {}", pkg.dirname));
    else:
        runcmd(ccmd);

def install(pkg, workdir, prefix, make_opts):
    os.chdir(workdir);
    print(highlight("### Process module {} ".format(pkg.name)), end='');

    if len(pkg.dirname) == 0:
        pkg.dirname = guess_dirname(pkg.url);
        print(ok("[{}*] ".format(pkg.dirname)), end='');
    else:
        print(ok("[{}] ".format(pkg.dirname)), end='');

    if len(pkg.dirname) == 0 or pkg.dirname.find("/") != -1:
        print('... ' + error("Bad directory name: {}", pkg.dirname));
        sys.exit(-1);

    print("...");

    filename = download(pkg);
    unpack(filename);
    os.chdir(workdir + "/build/" + pkg.dirname);
    pkg.configure(prefix);
    pkg.make(prefix, make_opts);
    pkg.install(prefix);
    os.chdir(workdir + "/build");
    cleanup(pkg);

    return True

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
