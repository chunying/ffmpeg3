
class frei0r:
    name = "frei0r 1.5.0"
    proto = "git"
    url = "https://github.com/dyne/frei0r.git"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-frei0r" ]

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/lib/frei0r-1"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./autogen.sh");
        runcmd("./configure --prefix={}".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(frei0r());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
