
class fdkaac:
    name = "fdk aac 0.1.4"
    url = "http://downloads.sourceforge.net/project/opencore-amr/fdk-aac/fdk-aac-0.1.4.tar.gz"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libfdk-aac" ]

    def has_builtin(self):
        return pkg_config_builtin("fdk-aac");

    def skip(self, prefix, force):
        if force: return False;
        return pkg_config_exists("fdk-aac");

    def configure(self, prefix):
        runcmd("./configure --prefix={} --with-pic".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(fdkaac());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
