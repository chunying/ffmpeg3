
class gmplib:
    name = "gmplib 6.1.2 (required by gnutls)"
    url = "https://gmplib.org/download/gmp/gmp-6.1.2.tar.xz"
    dirname = "" # leave empty to auto guess

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/gmp.h"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix={}".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(gmplib());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
