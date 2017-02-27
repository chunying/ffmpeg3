
class twolame:
    name = "TwoLame 0.3.13"
    ### work with source
    url = "http://downloads.sourceforge.net/twolame/twolame-0.3.13.tar.gz";
    dirname = "";
    ffmpeg_opts = [ "--enable-libtwolame" ]

    def has_builtin(self):
        return pkg_config_builtin("twolame");

    def skip(self, prefix, force):
        if force: return False;
        return pkg_config_exists("twolame");

    def configure(self, prefix):
        runcmd("./configure --prefix={}".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(twolame());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
