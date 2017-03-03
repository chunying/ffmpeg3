
class gcrypt:
    name = "gcrypt 1.7.5"
    url = "https://gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-1.7.5.tar.bz2"
    dirname = "" # leave empty to auto guess

    def has_builtin(self):
        return which("libgcrypt-config");

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/gcrypt.h"): return True;
        return False;

    def configure(self, prefix):
        param = ""
        msys = msys_sysname();
        if msys != None:
            param = "--build {} --host {}".format(msys, msys);
            print(yellow("### Configure with additional parameters '{}'".format(param)));
        runcmd("./configure --prefix={} {}".format(prefix, param));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(gcrypt());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
