
class celt:
    # mandatory fields
    name = "celt 0.11.1"
    url = "http://downloads.xiph.org/releases/celt/celt-0.11.1.tar.gz"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libcelt" ]

    def has_builtin(self):
        return pkg_config_builtin("celt");

    def skip(self, prefix, force):
        if force: return False;
        return pkg_config_exists("celt");

    def configure(self, prefix):
        runcmd("./configure --prefix={}".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(celt());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
