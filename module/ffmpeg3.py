
class ffmpeg3:
    name = "ffmpeg 3.2.4"
    proto = "http"
    url = "http://ffmpeg.org/releases/ffmpeg-3.2.4.tar.bz2"
    dirname = "" # leave empty to auto guess

    def skip(self, prefix, force):
        if file_exist(prefix + "/bin/ffmpeg"): return True;
        return False;

    # this is a special configuration for ffmpeg3!
    def configure(self, prefix, opts):
        optstr = " ".join(opts);
        runcmd("./configure --prefix={}".format(prefix) + " " +  optstr);

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

#deps.append(ffmpeg3());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
