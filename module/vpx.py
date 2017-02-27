
class vpx:
    name = "libvpx"
    proto = "git"
    url = "https://chromium.googlesource.com/webm/libvpx"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libvpx" ]

    def has_builtin(self):
        return pkg_config_builtin("vpx");

    def skip(self, prefix, force):
        if force: return False;
        return pkg_config_exists("vpx");

    def configure(self, prefix):
        runcmd("./configure --prefix={} --enable-shared --enable-pic".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(vpx());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
