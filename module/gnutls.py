
class gnutls:
    name = "gnutls"
    url = "ftp://ftp.gnutls.org/gcrypt/gnutls/v3.5/gnutls-3.5.8.tar.xz"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-gnutls" ]

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/gnutls/gnutls.h"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix={} --with-included-libtasn1 --with-included-unistring --without-p11-kit".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(gnutls());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
