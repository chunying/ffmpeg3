
class opus:
    name = "opus 1.1.3"
    url = "http://downloads.xiph.org/releases/opus/opus-1.1.3.tar.gz"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libopus" ]

    def has_builtin(self):
        if file_exist('/usr/local/include/opus/opus.h'): return '/usr/local/include/opus/opus.h';
        return None;

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/opus/opus.h"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix={} --with-pic".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(opus());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
