
class RENAME:
    name = "x264-snapshot-20170106"
    dirname = ""    # leave empty to use filename prefixes (before dot)
    baseurl = "ftp://ftp.videolan.org/pub/x264/snapshots/"
    filename = "x264-snapshot-20170106-2245.tar.bz2"
    sha1 = ""   # leave empty if unknown
    ffmpeg_opts = [ "--enable-libx264" ];

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/bin/x264"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix={} --enable-static --enable-shared".format(prefix));

    def make(self, opts):
        runcmd("make {}".format(opts));

    def install(self):
        runcmd("make install");

deps.append(RENAME());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
