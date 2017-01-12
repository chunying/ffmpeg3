
class fribidi:
    name = "fribidi 0.19.7 (required by libass)"
    url = "http://fribidi.org/download/fribidi-0.19.7.tar.bz2"
    dirname = "" # leave empty to auto guess

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/bin/fribidi"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix={}".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(fribidi());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
