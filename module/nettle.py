
class nettle:
    name = "nettle 3.3 (required by gnutls)"
    url = "https://ftp.gnu.org/gnu/nettle/nettle-3.3.tar.gz"
    dirname = "" # leave empty to auto guess

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/nettle/nettle-types.h"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix={} --enable-mini-gmp".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(nettle());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
