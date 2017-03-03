#!/bin/sh

pacman -Syuu
pacman -S --needed autoconf automake \
	mingw64/mingw-w64-x86_64-gcc \
	mingw64/mingw-w64-x86_64-cmake \
	mingw64/mingw-w64-x86_64-nasm \
	mingw64/mingw-w64-x86_64-yasm \
	mingw64/mingw-w64-x86_64-fdk-aac \
	mingw64/mingw-w64-x86_64-libtool \
	mingw64/mingw-w64-x86_64-libgcrypt \
	mingw64/mingw-w64-x86_64-openh264 \
	mingw64/mingw-w64-x86_64-SDL2 \
	mingw64/mingw-w64-x86_64-twolame \
	mingw64/mingw-w64-x86_64-ffmpeg
pacman -R mingw-w64-x86_64-ffmpeg
