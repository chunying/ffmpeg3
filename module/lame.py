
class lame:
    name = "lame 3.99.5"
    dirname = "lame-3.99.5" # leave empty to use filename prefixes (before the 1st dot)
    baseurl = "https://nchc.dl.sourceforge.net/project/lame/lame/3.99/"
    filename = "lame-3.99.5.tar.gz"
    sha1 = ""   # leave empty if unknown
    ffmpeg_opts = [ "--enable-libmp3lame" ]

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/bin/lame"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix={}".format(prefix));

    def make(self, opts):
        runcmd("make {}".format(opts));

    def install(self):
        runcmd("make install");

deps.append(lame());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
