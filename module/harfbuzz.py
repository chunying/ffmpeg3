
class harfbuzz:
    # class name SHOULD be equivalent to filename (without .py),
    # so that the --rebuild option works for the module
    # mandatory fields
    name = "harfbuzz"
    url = "https://www.freedesktop.org/software/harfbuzz/release/harfbuzz-1.4.3.tar.bz2"
    dirname = "" # leave empty to auto guess

    def has_builtin(self):
        return pkg_config_builtin("harfbuzz");

    def skip(self, prefix, force):
        if force: return False;
        return pkg_config_exists("harfbuzz");

    def configure(self, prefix):
        runcmd("./configure --prefix={}".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(harfbuzz());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
