
class harfbuzz:
    # class name SHOULD be equivalent to filename (without .py),
    # so that the --rebuild option works for the module
    # mandatory fields
    name = "harfbuzz"
    url = "https://www.freedesktop.org/software/harfbuzz/release/harfbuzz-1.4.3.tar.bz2"
    dirname = "" # leave empty to auto guess
    # optional fields
    proto = ""  # http (default), ftp, git, or null
    sha1 = ""   # remove or leave empty if unknown
    md5 = ""    # remove or leave empty if unknown
    ffmpeg_opts = []

    def has_builtin(self):
        return pkg_config_builtin("harfbuzz");

    def skip(self, prefix, force):
        return pkg_config_exists("harfbuzz") if force == False else False;

    def configure(self, prefix):
        runcmd("./configure --prefix={}".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(harfbuzz());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
