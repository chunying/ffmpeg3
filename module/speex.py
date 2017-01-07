
class speex:
    name = "speex 1.2.0"
    url = "http://downloads.xiph.org/releases/speex/speex-1.2.0.tar.gz"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libspeex" ]

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/speex/speex.h"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix={}".format(prefix));

    def make(self, opts):
        runcmd("make {}".format(opts));

    def install(self):
        runcmd("make install");

deps.append(speex());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
