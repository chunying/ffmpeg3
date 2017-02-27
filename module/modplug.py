
class modplug:
    # mandatory fields
    name = "libmodplug 0.8.8.5"
    url = "http://sourceforge.net/projects/modplug-xmms/files/libmodplug/0.8.8.5/libmodplug-0.8.8.5.tar.gz"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libmodplug" ]

    def has_builtin(self):
        return pkg_config_builtin("libmodplug");

    def skip(self, prefix, force):
        if force: return False;
        return pkg_config_exists("libmodplug");

    def configure(self, prefix):
        runcmd("./configure --prefix={}".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(modplug());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
