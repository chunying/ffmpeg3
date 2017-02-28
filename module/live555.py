
class live555:
    name = "live555 (2016.01.26)"
    url = "http://www.live555.com/liveMedia/public/live.2017.01.26.tar.gz"
    dirname = "live" # leave empty to auto guess

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/include/live555/liveMedia.hh"): return True;
        return False;

    def configure(self, prefix):
        runcmd("mv -f config.linux config.linux.OLD");
        runcmd("mv -f config.macosx config.macosx.OLD");
        runcmd("sed -e 's,^COMPILE_OPTS.*$,& -fPIC,' config.linux.OLD > config.linux");
        runcmd("sed -e 's,^COMPILE_OPTS.*$,& -fPIC,' config.macosx.OLD > config.macosx");
        runcmd("./genMakefiles `uname -s | tr A-Z a-z | sed -e 's,darwin,macosx,'`");

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("mkdir -p {}/lib".format(prefix));
        runcmd("find . -name '*.a' -exec cp -f {} "+prefix+"/lib/ \\;");
        runcmd("mkdir -p {}/include/live555".format(prefix));
        runcmd("find . -name '*.hh' -exec cp -f {} "+prefix+"/include/live555/ \\;");
        runcmd("cp -f groupsock/include/NetCommon.h "+prefix+"/include/live555/");

deps.append(live555());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
