
class opencl:
    name = "opencl"
    proto = "null"
    url = "OpenCL/opencl.h"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-opencl" ]

    def has_builtin(self):
        return "OpenCL/opencl.h";

    def skip(self, prefix, force):
        return False;

    def configure(self, prefix):
        print(info("*** No need to run ./configure"));

    def make(self, prefix, opts):
        print(info("*** No need to run make"));

    def install(self, prefix):
        print(info("*** No need to run make install"));

#sysdeps.append(("", None));
if test_compile(["OpenCL/opencl.h"], []):
    print(yellow("*** OpenCL activated ***"));
    deps.append(opencl());
else:
    print(red("*** You do not have OpenCL installed ***"));
    print(yellow("*** If you would like to activate this feature,"));
    print(yellow("    Please install the OpenCL package for your platform"));

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
