#!/usr/bin/env bash
#exit on error
set -o errexit

echo "Instalando dependencias do chrome"

apt-get update 
apt-get install -y git wget unzip \
    libglib2.0-0\
    libnss3\
    libgconf-2-4\
    libfontconfig1

echo "…Downloading Chrome"

wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -x ./google-chrome-stable_current_amd64.deb ./chrome

ln -sr ./chrome/opt/google/chrome/google-chrome /usr/bin/google-chrome

rm ./google-chrome-stable_current_amd64.deb

pip install -r requirements.txt
