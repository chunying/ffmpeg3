
class opencv:
    name = "OpenCV 3.2.0"
    url = "https://github.com/opencv/opencv/archive/3.2.0.zip"
    dirname = "opencv-3.2.0"
    #ffmpeg_opts = [ "--enable-libopencv" ] # temporarily disabled for ffmpeg?

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/opencv/cv.h"): return True;
        return False;

    def configure(self, prefix):
        runcmd("mkdir -p build");
        runcmd("cd build; cmake -DCMAKE_INSTALL_PREFIX={} ..".format(prefix));

    def make(self, prefix, opts):
        runcmd("chdir build; make {}".format(opts));

    def install(self, prefix):
        runcmd("chdir build; make install");

deps.append(opencv());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
