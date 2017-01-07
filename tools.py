import hashlib
import errno
import sys
import os

def highlight(msg):
    return "\x1b[1m" + msg + "\x1b[m";

def error(msg):
    return "\x1b[1;31m" + msg + "\x1b[m";

def info(msg):
    return "\x1b[1;33m" + msg + "\x1b[m";

def auto_dirname(filename):
    idx = filename.find(".");
    if idx < 0: return filename;
    return filename[:idx];

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

def download(pkg):
    sha1 = "";
    if hasattr(pkg, 'sha1'): sha1 = pkg.sha1.strip();
    cachename = "cached/" + pkg.filename;
    if file_exist(cachename): return cachename;
    runcmd("wget -P ./cached {}".format(pkg.baseurl + pkg.filename));
    if len(sha1) > 0:
        m = hashlib.sha1();
        m.update(open(cachename).read());
        mysum = m.hexdigest();
        if mysum != sha1:
            print(error("*** Invalid checksum {} != {}".format(mysum, sha1)));
            sys.exit(-1);
    return cachename;

def unpack(fn):
    if fn[-7:] == ".tar.gz":    runcmd("tar xzf {} -C build/".format(fn));
    if fn[-8:] == ".tar.bz2":   runcmd("tar xjf {} -C build/".format(fn));
    if fn[-4:] == ".zip":       runcmd("unzip {} -C build/".format(fn));

def cleanup(pkg):
    ccmd = "rm -rf {}".format(pkg.dirname);
    if ccmd.find("/") != -1:
        print(error("*** Invalid directory name: {}", pkg.dirname));
    else:
        runcmd(ccmd);

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
