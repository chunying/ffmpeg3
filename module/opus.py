
class opus:
    name = "opus 1.1.3"
    url = "http://downloads.xiph.org/releases/opus/opus-1.1.3.tar.gz"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libopus" ]

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/opus/opus.h"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix={} --with-pic".format(prefix));

    def make(self, opts):
        runcmd("make {}".format(opts));

    def install(self):
        runcmd("make install");

deps.append(opus());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
