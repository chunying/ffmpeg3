
class webp:
    name = "libwebp"
    proto = "git"
    url = "https://chromium.googlesource.com/webm/libwebp"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libwebp " ]

    def has_builtin(self):
        return pkg_config_builtin("libwebp");

    def skip(self, prefix, force):
        if force: return False;
        return pkg_config_exists("libwebp");

    def configure(self, prefix):
        runcmd("./autogen.sh");
        runcmd("./configure --prefix={} --with-pic ".format(prefix) +
               "--enable-experimental --enable-libwebpmux " +
               "--enable-libwebpdemux --enable-libwebpdecoder " +
               "--enable-libwebpextras");

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(webp());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
