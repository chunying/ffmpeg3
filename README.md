# ffmpeg3

Python FFmpeg build scripts

# Requirement

- Python3
- Python3 future package: pip3 install future
- Compilers: gcc, g++
- make and cmake
- m4, autoconf, libtool
- freetype6-dev (libfrei0r)
- libfontconfig1-dev (libass)

# Quick Start Guide

- Choose your installation prefix (`$PREFIX`), the default is **/usr/local/ffmpeg**
- [optional] Run `./ffbuild.py -h` to see more options
- Run `make` or `./ffbuild.py` in the directory, and all files will be installed in `$PREFIX`
- Edit `env-setup` to setup your `$PREFIX`
- Copy `env-setup` to `$PREFIX`
- [on Linux] Add `$PREFIX` to ldconfig search path

# Usage

- Merge `env-setup` into your environment, and have fun!

# Note

- If you are working with MSYS2, install msys/python3 instead of those in mingw\* repositories

