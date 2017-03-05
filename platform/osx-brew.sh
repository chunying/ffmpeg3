#!/bin/bash

# install homebrew:
# $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

brew update
brew upgrade
brew install ffmpeg \
		--with-fdk-aac \
		--with-fontconfig \
		--with-freetype \
		--with-frei0r \
		--with-game-music-emu \
		--with-libass \
		--with-libbluray \
		--with-libbs2b \
		--with-libcaca \
		--with-libebur128 \
		--with-libgsm \
		--with-libmodplug \
		--with-libsoxr \
		--with-libssh \
		--with-libvidstab \
		--with-libvorbis \
		--with-libvpx \
		--with-opencore-amr \
		--with-openh264 \
		--with-openjpeg \
		--with-openssl \
		--with-opus \
		--with-rtmpdump \
		--with-rubberband \
		--with-schroedinger \
		--with-sdl2 \
		--with-snappy \
		--with-speex \
		--with-tesseract \
		--with-theora \
		--with-tools \
		--with-two-lame \
		--with-wavpack \
		--with-webp \
		--with-x265 \
		--with-xz \
		--with-zeromq \
		--with-zimg

