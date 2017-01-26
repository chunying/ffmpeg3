
class caca:
    # mandatory fields
    name = "libcaca 0.9"
    url = "http://caca.zoy.org/files/libcaca/libcaca-0.99.beta19.tar.gz"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libcaca" ]

    def has_builtin(self):
        if file_exist('/usr/local/include/caca.h'): return '/usr/local/include/caca.h';
        return None;

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/caca.h"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix={} --disable-python --disable-ruby --disable-java --disable-doc".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(caca());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
