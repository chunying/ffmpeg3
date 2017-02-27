
class openjpeg:
    name = "openjpeg 2.1.2"
    url = "https://github.com/uclouvain/openjpeg/archive/v2.1.2.tar.gz"
    dirname = "openjpeg-2.1.2" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libopenjpeg" ]

    def has_builtin(self):
        return pkg_config_builtin("libopenjp2");

    def skip(self, prefix, force):
        if force: return False;
        return pkg_config_exists("libopenjp2");

    def configure(self, prefix):
        cwd = os.getcwd();
        runcmd("mkdir -p build");
        os.chdir("build");
        runcmd("cmake -DCMAKE_INSTALL_PREFIX={} ..".format(prefix));
        os.chdir(cwd);

    def make(self, prefix, opts):
        cwd = os.getcwd();
        os.chdir("build");
        runcmd("make {}".format(opts));
        os.chdir(cwd);

    def install(self, prefix):
        cwd = os.getcwd();
        os.chdir("build");
        runcmd("make install");
        os.chdir(cwd);

deps.append(openjpeg());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
