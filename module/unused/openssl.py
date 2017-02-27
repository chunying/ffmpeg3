
class openssl:
    name = "openssl 1.1.0c"
    url = "https://www.openssl.org/source/openssl-1.1.0c.tar.gz"
    dirname = "" # leave empty to auto guess
    ffmpeg_opts = [ "--enable-openssl" ];

    def skip(self, prefix, force):
        if force: return False;
        if file_exist(prefix + "/bin/openssl"): return True;
        return False;

    def configure(self, prefix):
        runcmd("./config --prefix={} --openssldir={}/ssl".format(prefix, prefix)
	             + " enable-heartbeats enable-weak-ssl-ciphers"
		     + " enable-md2 enable-rc5 zlib");

    def make(self, prefix, opts):
        runcmd("make {}".format(opts));

    def install(self, prefix):
        runcmd("make install");

deps.append(openssl());

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
