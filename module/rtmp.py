
class rtmp:
    name = "RTMPDUMP 2.3"
    url = "http://rtmpdump.mplayerhq.hu/download/rtmpdump-2.3.tgz";
    dirname = "";
    ffmpeg_opts = [ "--enable-librtmp" ]

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/bin/rtmpdump"): return True;
        return False;

    def configure(self, prefix):
        print(info("*** No need to run ./configure"));
        runcmd("cp -f Makefile Makefile.OLD");
        runcmd("cp -f librtmp/Makefile librtmp/Makefile.OLD");
        runcmd("sed -e 's,prefix=/usr/local,prefix={},' Makefile.OLD > Makefile".format(prefix));
        runcmd("sed -e 's,prefix=/usr/local,prefix={},' librtmp/Makefile.OLD > librtmp/Makefile".format(prefix));

    def make(self, opts):
        runcmd("make {}".format(opts));

    def install(self):
        runcmd("make install");

deps.append(rtmp());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
