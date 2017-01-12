
class celt:
    # mandatory fields
    name = "celt 0.11.1"
    url = "http://downloads.xiph.org/releases/celt/celt-0.11.1.tar.gz"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libcelt" ]

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/bin/celtenc"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix={}".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(celt());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
