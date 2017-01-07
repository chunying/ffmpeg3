
class yasm:
    name = "yasm 1.3.0"
    url = "http://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz"
    dirname = "" # leave empty to auto guess
    sha1 = "b7574e9f0826bedef975d64d3825f75fbaeef55e"   # leave empty if unknown

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/bin/yasm"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix {}".format(prefix));

    def make(self, opts):
        runcmd("make {}".format(opts));

    def install(self):
        runcmd("make install");

deps.append(yasm());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
