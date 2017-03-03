
class gpg_error:
    name = "gpg-error 1.26"
    url = "https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-1.26.tar.bz2"
    dirname = "" # leave empty to auto guess

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/gpg-error.h"): return True;
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

deps.append(gpg_error());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
