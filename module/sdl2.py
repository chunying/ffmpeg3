
class sdl2:
    name = "sdl 2.0.5"
    url = "https://www.libsdl.org/release/SDL2-2.0.5.tar.gz"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = []

    def has_builtin(self):
        return pkg_config_builtin("sdl2");

    def skip(self, prefix, force):
        if force: return False;
        return pkg_config_exists("sdl2");

    def configure(self, prefix):
        runcmd("rm -rf mybuild");
        os.mkdir("mybuild");
        runcmd("cd mybuild; ../configure --prefix={} --with-pic".format(prefix));

    def make(self, prefix, opts):
        runcmd("make -C mybuild {}".format(opts));

    def install(self, prefix):
        runcmd("make -C mybuild install");

deps.append(sdl2());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
