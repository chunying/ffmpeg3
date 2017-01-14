#!/usr/bin/env python3
# need 'future' package: pip3 install future
import os
import sys
import getopt
from tools import *
from past.builtins import execfile

DEFAULT_PREFIX = "/usr/local/ffmpeg3";
deps = [];          # store inscance of activated modules
modules = [];       # store activated modules
make_opts = "-j10"; # make options
force = False;
rebuild = [];       # list of rebuild modules
modules_built = 0;

prefix = "";
if 'FFMPEG' in os.environ.keys(): prefix = os.environ['FFMPEG'];
else:                             prefix = DEFAULT_PREFIX;

os.environ["PATH"] = prefix + "/bin:" + os.environ["PATH"];
os.environ["PKG_CONFIG_PATH"] = prefix + "/lib/pkgconfig:/opt/local/lib/pkgconfig:/usr/lib/i386-linux-gnu/pkgconfig/:/usr/lib/pkgconfig";

modules = all_modules; # all_modules defined in tools.py

print(highlight("Python FFmpeg build script: use -h option to see more options"));

opts = []
args = []
try:
    opts, args = getopt.getopt(sys.argv[1:], "h", ["help", "rebuild=", "prefix=", "modules=", "make=", "force"]);
except getopt.GetoptError as e:
    print(error("Bad option: " + str(e)));
    usage();
    dump_modules(all_modules);
    sys.exit(2);

for x in opts:
    optname, optarg = x;
    if optname == "-h" or optname == "--help":
        usage();
        dump_modules(all_modules);
        sys.exit(0);
    elif optname == "--prefix":  prefix = optarg;
    elif optname == "--force":   force = True;
    elif optname == "--make":    make_opts = optarg;
    elif optname == "--modules": modules = optarg.split(",");
    elif optname == "--rebuild": rebuild = optarg.split(",");

print(info("prefix [{}], make [{}], force={}".format(prefix, make_opts, "true" if force else "false")));
if len(modules) > 0: dump_modules("Activated modules:", modules);
else:                dump_modules("Available modules:", all_modules);
if len(rebuild) > 0: dump_modules("Rebuild modules:", rebuild);

# start build and install
for m in modules:
    execfile("module/{}.py".format(m));
execfile("module/ffmpeg3.py");

create_dir("./cached");
create_dir("./build");
cwd = os.getcwd();

for d in deps:
    myname = type(d).__name__;
    os.chdir(cwd);
    print(highlight("### Process module {} ".format(d.name)), end='');

    if len(d.dirname) == 0:
        d.dirname = guess_dirname(d.url);
        print(ok("[{}*] ".format(d.dirname)), end='');
    else:
        print(ok("[{}] ".format(d.dirname)), end='');

    if len(d.dirname) == 0 or d.dirname.find("/") != -1:
        print('... ' + error("Bad directory name: {}", d.dirname));
        sys.exit(-1);

    if myname not in rebuild and d.skip(prefix, force):
        print('... ' + info("skipped"));
        continue;

    print('...');

    filename = download(d);
    unpack(filename);
    os.chdir(cwd + "/build/" + d.dirname);
    d.configure(prefix);
    d.make(prefix, make_opts);
    d.install(prefix);
    os.chdir(cwd + "/build");
    cleanup(d);
    modules_built = modules_built + 1;

# build and install ffmpeg3
os.chdir(cwd);
ff = ffmpeg3();

myname = type(ff).__name__;
print(highlight("### Process package {} ({}) ".format(myname, ff.name)), end='');
if modules_built == 0 and myname not in rebuild and ff.skip(prefix, force):
    print('... ' + info("skipped"));
    sys.exit(0);
if len(ff.dirname) == 0: ff.dirname = guess_dirname(ff.url);
print(ok("[{}] ".format(ff.dirname)) + '...');

filename = download(ff);
unpack(filename);
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
ff.make(prefix, make_opts);
ff.install(prefix);
os.chdir(cwd + "/build");
cleanup(ff);

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4