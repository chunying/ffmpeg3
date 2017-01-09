
class wavpack:
    name = "WavPack 5.0.0"
    url = "https://github.com/dbry/WavPack/archive/5.0.0.tar.gz"
    dirname = "WavPack-5.0.0"
    ffmpeg_opts = [ "--enable-libwavpack" ]

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/bin/wavpack"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./autogen.sh");
        runcmd("./configure --prefix={} --with-pic".format(prefix));

    def make(self, opts):
        runcmd("make {}".format(opts));

    def install(self):
        runcmd("make install");

deps.append(wavpack());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
