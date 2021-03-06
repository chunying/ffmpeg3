
class libass:
    name = "libass 0.13.6"
    url = "https://github.com/libass/libass/releases/download/0.13.6/libass-0.13.6.tar.xz"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libass" ]

    def has_builtin(self):
        return pkg_config_builtin("libass");

    def skip(self, prefix, force):
        if force: return False;
        return pkg_config_exists("libass");

    def configure(self, prefix):
        runcmd("./configure --prefix={}".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

sysdeps.append(("harfbuzz", None));
deps.append(libass());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
