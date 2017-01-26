
class nasm:
    name = "nasm 2.12.02"
    url = "http://www.nasm.us/pub/nasm/releasebuilds/2.12.02/nasm-2.12.02.tar.xz"
    dirname = "" # leave empty to auto guess

    def has_builtin(self):
        if which("nasm") != None: return which("nasm");
        return None;

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/bin/nasm"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./configure --prefix {}".format(prefix));

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(nasm());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
