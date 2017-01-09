
class fdkaac:
    name = "fdk aac 0.1.4"
    url = "http://downloads.sourceforge.net/project/opencore-amr/fdk-aac/fdk-aac-0.1.4.tar.gz"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libfdk-aac" ]

    def skip(self, prefix, force):
        if force: return False;
        #if file_exist(prefix + "/bin/fdkaac"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix={} --with-pic".format(prefix));

    def make(self, opts):
        runcmd("make {}".format(opts));

    def install(self):
        runcmd("make install");

deps.append(fdkaac());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
