import hashlib
import errno
import sys
import os

all_modules = [ "yasm", "nasm", "sdl2", "sdl2_ttf",
            "ladspa", "frei0r", "fribidi", "libass", "caca", "gsm", "modplug",
            "rtmp",
            "celt", "lame", "ogg", "opus", "vorbis", "speex", "fdkaac", "twolame", "wavpack",
            "openjpeg",
            "webp", "theora", "vpx", "x264", "openh264", "x265", "xvid",
            "live555" ];

def highlight(msg):
    return "\x1b[1m" + msg + "\x1b[m";

def error(msg):
    return "\x1b[1;31m" + msg + "\x1b[m";

def info(msg):
    return "\x1b[1;33m" + msg + "\x1b[m";

def ok(msg):
    return "\x1b[1;32m" + msg + "\x1b[m";

def errq(msg):
    print(error(msg));
    sys.exit(-1);

def usage():
    print("""Options:
    -h, --help                 Show this message
    --prefix [prefix]          Specify prefix directory
    --modules [module[,...]]   Build and install selected modules
    --make [options]           Additional make options
    --force                    Rebuild all modules
    --rebuild [module[,...]]   Rebuild selected modules""");

def dump_modules(msg, mods):
    print(highlight(msg), end='');
    print(" ".join(mods));
    print(ok("### {} module(s) activated".format(len(mods))));

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

def runcmd(cmd):
    ret = os.system(cmd);
    if ret != 0:
        print(error("*** command '{}' failed with code {}".format(cmd, ret)));
        print(error("*** working directory: {}".format(os.getcwd())));
        sys.exit(-1)

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
    if file_exist(cachename): return cachename;
    runcmd("wget -P ./cached {}".format(pkg.url));
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
    if fn[-4:] == ".zip":       runcmd("unzip {} -C build/".format(fn));
    # otherwise: do nothing

def cleanup(pkg):
    ccmd = "rm -rf {}".format(pkg.dirname);
    if ccmd.find("/") != -1:
        print(error("*** Invalid directory name: {}", pkg.dirname));
    else:
        runcmd(ccmd);

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
