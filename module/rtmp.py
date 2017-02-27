
class rtmp:
    name = "rtmpdump"
    proto = "git"
    url = "git://git.ffmpeg.org/rtmpdump"
    dirname = "";
    ffmpeg_opts = [ "--enable-librtmp" ]

    def has_builtin(self):
        return pkg_config_builtin("librtmp");

    def skip(self, prefix, force):
        if force: return False;
        return pkg_config_exists("librtmp");

    def configure(self, prefix):
        sed = (("sed -e 's,prefix=/usr/local,prefix={},' "
                 + " -e 's,^CFLAGS.*,& -I{}/include,'"
                 + " -e 's,^LIB_GNUTLS=.*,LIB_GNUTLS=-L{}/lib -lgnutls -lgcrypt -lgmp -lhogweed -lnettle -lz,'"));
        if platform.system().lower() == "darwin":
            sed = sed + " -e 's/-Wl,-soname,/-Wl,-install_name,/'";
        sed = sed.format(prefix, prefix, prefix);
        runcmd("cp -f Makefile Makefile.OLD");
        runcmd("cp -f librtmp/Makefile librtmp/Makefile.OLD");
        runcmd(sed + " Makefile.OLD > Makefile");
        runcmd(sed + " librtmp/Makefile.OLD > librtmp/Makefile");

    def make(self, prefix, opts):
        runcmd("make {} CRYPTO=GNUTLS".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(rtmp());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
