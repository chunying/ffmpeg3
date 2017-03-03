
class frei0r:
    name = "frei0r 1.5.0"
    proto = "git"
    url = "https://github.com/dyne/frei0r.git"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-frei0r" ]

    def has_builtin(self):
        return pkg_config_builtin("frei0r");

    def skip(self, prefix, force):
        if force: return False;
        return pkg_config_exists("frei0r");

    def configure(self, prefix):
        if msys_sysname() != None:
            runcmd("mkdir -p build");
            runcmd("cd build; cmake -G \"MSYS Makefiles\" -DCMAKE_INSTALL_PREFIX={} ..".format(prefix));
            return;
        runcmd("./autogen.sh");
        runcmd("./configure --prefix={}".format(prefix));

    def make(self, prefix, opts):
        if msys_sysname() != None:
            runcmd("cd build; make {}".format(opts));
            return;
        runcmd("make {}".format(opts));

    def install(self, prefix):
        if msys_sysname() != None:
            runcmd("cd build; make install");
            return;
        runcmd("make install");

deps.append(frei0r());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
