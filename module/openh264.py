
class openh264:
    name = "libopenh264"
    proto = "git"
    url = "https://github.com/cisco/openh264.git"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libopenh264 " ]

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/wels/codec_api.h"): return True;
        return False;

    def configure(self, prefix):
        print(info("*** No need to run ./configure"));

    def make(self, opts):
        runcmd("make PREFIX={} {}".format(prefix, opts));

    def install(self):
        runcmd("make PREFIX={} install".format(prefix));

deps.append(openh264());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
