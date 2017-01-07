
class ffmpeg3:
    name = "ffmpeg 3.2.2"
    dirname = "ffmpeg-3.2.2" # leave empty to use filename prefixes (before the 1st dot)
    baseurl = "http://ffmpeg.org/releases/"
    filename = "ffmpeg-3.2.2.tar.bz2"
    sha1 = ""   # leave empty if unknown

    def skip(self, prefix, force):
        if force: return False;
        return False;

    # this is a special configuration for ffmpeg3!
    def configure(self, prefix, opts):
        optstr = " ".join(opts);
        runcmd("./configure --prefix={}".format(prefix) + " " +  optstr);

    def make(self, opts):
        runcmd("make {}".format(opts));

    def install(self):
        runcmd("make install");

#deps.append(ffmpeg3());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
