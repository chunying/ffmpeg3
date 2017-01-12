
class theora:
    name = "libtheora 1.1.1"
    url = "http://downloads.xiph.org/releases/theora/libtheora-1.1.1.tar.bz2"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libtheora" ]

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/theora/theora.h"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix={} --with-pic".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(theora());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
