
class theora:
    name = "libtheora 1.1.1"
    url = "http://downloads.xiph.org/releases/theora/libtheora-1.1.1.tar.bz2"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libtheora" ]

    def has_builtin(self):
        return pkg_config_builtin("theora");

    def skip(self, prefix, force):
        if force: return False;
        return pkg_config_exists("theora");

    def configure(self, prefix):
        runcmd("./configure --prefix={} --with-pic --disable-examples".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(theora());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
