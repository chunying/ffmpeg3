
class libass:
    name = "libass 0.13.6"
    url = "https://github.com/libass/libass/releases/download/0.13.6/libass-0.13.6.tar.xz"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libass" ]

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/ass/ass.h"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix={}".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(libass());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
