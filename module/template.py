
class RENAME:
    name = ""
    dirname = "" # leave empty to use filename prefixes (before the 1st dot)
    baseurl = ""
    filename = ""
    sha1 = ""   # leave empty if unknown
    ffmpeg_opts = []

    def skip(self, prefix, force):
        if force: return False;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix={}".format(prefix));

    def make(self, opts):
        runcmd("make {}".format(opts));

    def install(self):
        runcmd("make install");

deps.append(RENAME());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
