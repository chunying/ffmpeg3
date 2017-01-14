
class RENAME:
    # class name SHOULD be equivalent to filename (without .py),
    # so that the --rebuild option works for the module
    # mandatory fields
    name = ""
    url = ""
    dirname = "" # leave empty to auto guess
    # optional fields
    proto = ""  # http (default), ftp, git, or null
    sha1 = ""   # remove or leave empty if unknown
    md5 = ""    # remove or leave empty if unknown
    ffmpeg_opts = []

    def skip(self, prefix, force):
        if force: return False;
        #if file_exist(prefix + "/include/xxx/xxx.h"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix={}".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(RENAME());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
