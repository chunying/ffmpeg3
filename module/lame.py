
class lame:
    name = "lame 3.99.5"
    url = "https://nchc.dl.sourceforge.net/project/lame/lame/3.99/lame-3.99.5.tar.gz"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libmp3lame" ]

    def has_builtin(self):
        if file_exist('/usr/local/include/lame/lame.h'): return "/usr/local/include/lame/lame.h";
        return None;

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/bin/lame"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix={} --with-pic --enable-nasm".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(lame());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
