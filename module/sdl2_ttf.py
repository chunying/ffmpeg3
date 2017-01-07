
class sdl2_ttf:
    name = "sdl2_ttf 2.0.14"
    url = "https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-2.0.14.tar.gz"
    dirname = "" # leave empty to auto guess

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/SDL2/SDL_ttf.h"): return True;
        return False;

    def configure(self, prefix):
        os.mkdir("mybuild");
        runcmd("cd mybuild; ../configure --prefix={} --with-pic".format(prefix));

    def make(self, opts):
        runcmd("make -C mybuild {}".format(opts));

    def install(self):
        runcmd("make -C mybuild install");

deps.append(sdl2_ttf());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
