
class sdl2:
    name = "sdl 2.0.5"
    url = "https://www.libsdl.org/release/SDL2-2.0.5.tar.gz"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = []

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/SDL2/SDL.h"): return True;
        return False;

    def configure(self, prefix):
        os.mkdir("mybuild");
        runcmd("cd mybuild; ../configure --prefix={} --with-pic".format(prefix));

    def make(self, opts):
        runcmd("make -C mybuild {}".format(opts));

    def install(self):
        runcmd("make -C mybuild install");

deps.append(sdl2());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
