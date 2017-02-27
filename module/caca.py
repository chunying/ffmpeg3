
class caca:
    # mandatory fields
    name = "libcaca 0.9"
    url = "http://caca.zoy.org/files/libcaca/libcaca-0.99.beta19.tar.gz"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libcaca" ]

    def has_builtin(self):
        return pkg_config_builtin("caca");

    def skip(self, prefix, force):
        if force: return False;
        return pkg_config_exists("caca");

    def configure(self, prefix):
        runcmd("./configure --prefix={} --disable-python --disable-ruby --disable-java --disable-doc".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(caca());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
