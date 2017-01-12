
class webp:
    name = "libwebp"
    proto = "git"
    url = "https://chromium.googlesource.com/webm/libwebp"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libwebp " ]

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/webp/encode.h"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./autogen.sh");
        runcmd("./configure --prefix={} --with-pic ".format(prefix) +
               "--enable-experimental --enable-libwebpmux " +
               "--enable-libwebpdemux --enable-libwebpdecoder " +
               "--enable-libwebpextras");

    def make(self, opts):
        runcmd("make {}".format(opts));

    def install(self):
        runcmd("make install");

deps.append(webp());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
