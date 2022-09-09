FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noniteractive

RUN apt-get update
RUN  apt-get install -y wget gnupg libgtk-3-0 curl \
                 zip libarchive13 libgl1 libnss3 libxss1 libasound2-dev \
		cpio xvfb git python3 npm libgbm1




RUN git clone https://github.com/junlinp/unity-activate.git

RUN cd unity-activate && npm install && npm run build && npm link

ADD server.py /server.py
ADD encode_decode.py /encode_decode.py


