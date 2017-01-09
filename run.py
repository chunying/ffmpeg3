#!/usr/bin/env python3
# need 'future' package: pip3 install future
import os
import sys
from tools import *
from past.builtins import execfile

DEFAULT_PREFIX = "/usr/local/ffmpeg3";

deps = [];
make_opts = "-j10";
force = False;

prefix = "";
if 'FFMPEG' in os.environ.keys():
    prefix = os.environ['FFMPEG'];
else:
    prefix = DEFAULT_PREFIX;

os.environ["PATH"] = prefix + "/bin:" + os.environ["PATH"];
os.environ["PKG_CONFIG_PATH"] = prefix + "/lib/pkgconfig:/opt/local/lib/pkgconfig:/usr/lib/i386-linux-gnu/pkgconfig/:/usr/lib/pkgconfig";

modules = [ "yasm", "nasm", "sdl2", "sdl2_ttf",
            "lame", "opus", "vorbis", "speex", "fdkaac",
            "theora", "vpx", "x264", "x265", "xvid" ];
for m in modules:
    execfile("module/{}.py".format(m));
execfile("module/ffmpeg3.py");

create_dir("./cached");
create_dir("./build");
cwd = os.getcwd();

for d in deps:
    os.chdir(cwd);
    print(highlight("### Process package {}".format(d.name)));

    if len(d.dirname) == 0:
        d.dirname = guess_dirname(d.url);
        print(info("--- guessed dirname: {}".format(d.dirname)));

    if len(d.dirname) == 0 or d.dirname.find("/") != -1:
        print(error("*** Invalid directory name: {}", d.dirname));
        sys.exit(-1);

    if d.skip(prefix, force):
        print(info("*** {} alreay installed, skipped".format(d.name)));
        continue;

    filename = download(d);
    unpack(filename);
    os.chdir(cwd + "/build/" + d.dirname);
    d.configure(prefix);
    d.make(make_opts);
    d.install();
    os.chdir(cwd + "/build");
    cleanup(d);

# install ffmpeg3
os.chdir(cwd);
ff = ffmpeg3();
print(highlight("### Process package {}".format(ff.name)));
if ff.skip(prefix, force):
    print(info("*** {} alreay installed, skipped".format(ff.name)));
    sys.exit(0);
filename = download(ff);
unpack(filename);
if len(ff.dirname) == 0: ff.dirname = guess_dirname(ff.url);
os.chdir(cwd + "/build/" + ff.dirname);
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
os.chdir(cwd + "/build");
cleanup(ff);

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
