# ffmpeg3

Python FFmpeg build scripts

# Requirement

- Python3
- Python3 future package: pip3 install future
- Compilers: gcc, g++
- make and cmake

# Simplest Usage

- Run `make` or `./ffbuild.py` in the directory, and all files will be installed in **/usr/local/ffmpeg3**
- (optionally) copy `env-setup` to **/usr/local/ffmpeg3**
- (on Linux) add **/usr/local/ffmpeg3/lib** to ldconfig search path
- merge `env-setup` into your environemnt, and have fun!
