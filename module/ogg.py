
class ogg:
    name = "libogg 1.3.2"
    url = "http://downloads.xiph.org/releases/ogg/libogg-1.3.2.tar.xz"
    dirname = "" # leave empty to auto guess

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/ogg/ogg.h"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix={} --with-pic".format(prefix));

    def make(self, opts):
        runcmd("make {}".format(opts));

    def install(self):
        runcmd("make install");

deps.append(ogg());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
