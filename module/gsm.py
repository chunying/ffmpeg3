
class gsm:
    # mandatory fields
    name = "gsm 1.0.16"
    url = "http://www.quut.com/gsm/gsm-1.0.16.tar.gz"
    dirname = "gsm-1.0-pl16" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-libgsm" ]

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/gsm.h"): return True;
        return False;

    def configure(self, prefix):
        runcmd("cp -f Makefile Makefile.OLD");
        runcmd("sed -e 's,^INSTALL_ROOT.*,INSTALL_ROOT = "+prefix+",'"
                + " -e 's,^GSM_INSTALL_INC.*,GSM_INSTALL_INC = $(GSM_INSTALL_ROOT)/include,'"
                + " -e 's,^CCFLAGS.*,CCFLAGS = -c -O2 -DNeedFunctionPrototypes=1 -fPIC,'"
                + " -e 's,^RMFLAGS.*,RMFLAGS = -f,'"
                + " -e 's,-rm $@,-rm -f $@,g'"
                + " Makefile.OLD > Makefile");

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(gsm());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
