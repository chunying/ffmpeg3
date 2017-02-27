
class openh264:
    name = "libopenh264"
    proto = "git"
    url = "https://github.com/cisco/openh264.git"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libopenh264 " ]

    def has_builtin(self):
        return pkg_config_builtin("openh264");

    def skip(self, prefix, force):
        if force: return False;
        return pkg_config_exists("openh264");

    def configure(self, prefix):
        print(info("*** No need to run ./configure"));

    def make(self, prefix, opts):
        runcmd("make PREFIX={} {}".format(prefix, opts));

    def install(self, prefix):
        runcmd("make PREFIX={} install".format(prefix));

deps.append(openh264());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
