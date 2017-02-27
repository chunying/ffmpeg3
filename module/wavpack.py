
class wavpack:
    name = "WavPack 5.0.0"
    url = "https://github.com/dbry/WavPack/archive/5.0.0.tar.gz"
    dirname = "WavPack-5.0.0"
    ffmpeg_opts = [ "--enable-libwavpack" ]

    def has_builtin(self):
        return pkg_config_builtin("wavpack");

    def skip(self, prefix, force):
        if force: return False;
        return pkg_config_exists("wavpack");

    def configure(self, prefix):
        runcmd("./autogen.sh");
        runcmd("./configure --prefix={} --with-pic".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(wavpack());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
