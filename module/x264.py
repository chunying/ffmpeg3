
class x264:
    name = "x264-snapshot-20170106"
    url = "ftp://ftp.videolan.org/pub/x264/snapshots/x264-snapshot-20170106-2245.tar.bz2"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libx264" ];

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/x264.h"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix={} --enable-static --enable-shared --enable-pic".format(prefix));

    def make(self, opts):
        runcmd("make {}".format(opts));

    def install(self):
        runcmd("make install");

deps.append(x264());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
