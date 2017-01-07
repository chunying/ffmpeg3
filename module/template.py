
class RENAME:
    name = ""   # [MANDATORY]
    proto = ""  # http (default), ftp, or git
    url = ""    # [MANDATORY]
    dirname = "" # [MANDATORY] leave empty to auto guess
    sha1 = ""   # remove or leave empty if unknown
    md5 = ""    # remove or leave empty if unknown
    ffmpeg_opts = []

    def skip(self, prefix, force):
        if force: return False;
        #if file_exist(prefix + "/include/xxx/xxx.h"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix={}".format(prefix));

    def make(self, opts):
        runcmd("make {}".format(opts));

    def install(self):
        runcmd("make install");

deps.append(RENAME());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
