
class vorbis:
    name = "libvorbis 1.3.5"
    url = "http://downloads.xiph.org/releases/vorbis/libvorbis-1.3.5.tar.xz"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libvorbis" ]

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/vorbis/vorbisenc.h"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix={} --with-pic".format(prefix));

    def make(self, opts):
        runcmd("make {}".format(opts));

    def install(self):
        runcmd("make install");

deps.append(vorbis());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
