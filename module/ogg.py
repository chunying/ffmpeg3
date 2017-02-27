
class ogg:
    name = "libogg 1.3.2"
    url = "http://downloads.xiph.org/releases/ogg/libogg-1.3.2.tar.xz"
    dirname = "" # leave empty to auto guess

    def has_builtin(self):
        return pkg_config_builtin("ogg");
        return None;

    def skip(self, prefix, force):
        if force: return False;
        return pkg_config_exists("ogg");

    def configure(self, prefix):
        runcmd("./configure --prefix={} --with-pic".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(ogg());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
