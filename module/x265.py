
class x265:
    name = "x265 2.2"
    url = "https://bitbucket.org/multicoreware/x265/downloads/x265_2.2.tar.gz"
    dirname = "" # leave empty to auto guess
    md5 = "36161843a70e4d46af1fa38cf221d0f3"    # leave empty if unknown
    ffmpeg_opts = [ "--enable-libx265" ];

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/x265.h"): return True;
        return False;

    def configure(self, prefix):
        cwd = os.getcwd();
        os.chdir("build/linux");
        runcmd('cmake -DCMAKE_INSTALL_PREFIX:PATH={} -D CMAKE_CXX_FLAGS="-fPIC" -D CMAKE_C_FLAGS="-fPIC" ../../source'.format(prefix));
        os.chdir(cwd);

    def make(self, prefix, opts):
        runcmd("make -C build/linux {}".format(opts));

    def install(self, prefix):
        runcmd("make -C build/linux install");

deps.append(x265());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
