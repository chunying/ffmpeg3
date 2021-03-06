
class xvid:
    name = "xvid 1.3.4"
    url = "http://downloads.xvid.org/downloads/xvidcore-1.3.4.tar.gz"
    dirname = "xvidcore" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libxvid" ];

    def has_builtin(self):
        t = test_compile(['xvid.h'], ['xvidcore']);
        return t if t != False else None;

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/xvid.h"): return True;
        return False;

    def configure(self, prefix):
        cwd = os.getcwd();
        os.chdir("build/generic");
        runcmd("./configure --prefix={}".format(prefix));
        os.chdir(cwd);

    def make(self, prefix, opts):
        runcmd("make -C build/generic {}".format(opts));

    def install(self, prefix):
        runcmd("make -C build/generic install");

deps.append(xvid());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
