#!/usr/bin/env python3
# need 'future' package
import os
import sys
from tools import *
from past.builtins import execfile

deps = [];
prefix = "/usr/local/ffmpeg3";
make_opts = "-j10";
force = False

os.environ["PKG_CONFIG_PATH"] = prefix + "/lib/pkgconfig:/opt/local/lib/pkgconfig:/usr/lib/i386-linux-gnu/pkgconfig/:/usr/lib/pkgconfig";
os.environ["PREFIX"] = prefix;

execfile("module/yasm.py");
execfile("module/lame.py");
execfile("module/x264.py");
execfile("module/ffmpeg3.py");

create_dir("./cached");
create_dir("./build");
pwd = os.getcwd();

for d in deps:
    os.chdir(pwd);
    print(highlight("### Process package {}".format(d.name)));

    if len(d.dirname) == 0:
        d.dirname = auto_dirname(d.filename);
        print(info("--- auto dirname: {}".format(d.dirname)));

    if len(d.dirname) == 0 or d.dirname.find("/") != -1:
        print(error("*** Invalid directory name: {}", d.dirname));
        sys.exit(-1);

    if d.skip(prefix, force):
        print(info("*** {} alreay installed, skipped".format(d.name)));
        continue;

    filename = download(d);
    unpack(filename);
    os.chdir("./build/" + d.dirname);
    d.configure(prefix);
    d.make(make_opts);
    d.install();
    os.chdir("..");
    cleanup(d);

# install ffmpeg3
os.chdir(pwd);
ff = ffmpeg3();
print(highlight("### Process package {}".format(ff.name)));
if ff.skip(prefix, force):
    print(info("*** {} alreay installed, skipped".format(ff.name)));
    sys.exit(0);
filename = download(ff);
unpack(filename);
os.chdir("./build/" + ff.dirname);
# built configure options
opts = [ "--enable-gpl", "--enable-version3", "--enable-nonfree",
         "--enable-shared",
         "--enable-avresample" ];
for d in deps:
    if hasattr(d, "ffmpeg_opts"): opts.extend(d.ffmpeg_opts);
opts.append("--extra-cflags=-I{}/include".format(prefix));
opts.append("--extra-ldflags=-L{}/lib".format(prefix));
#
ff.configure(prefix, opts);
ff.make(make_opts);
ff.install();
os.chdir("..");
cleanup(ff);

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
