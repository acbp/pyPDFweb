#!/usr/bin/env bash
# exit on error
set -o errexit

STORAGE_DIR=/opt/render/project/.render

if [[ ! -d $STORAGE_DIR/chrome ]]; then
echo "...Downloading Chrome"
mkdir -p $STORAGE_DIR/chrome
cd $STORAGE_DIR/chrome
wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get install -y libglib2.0-0=2.50.3-2 \
libnss3=2:3.26.2-1.1+deb9u1 \
libgconf-2-4=3.2.6-4+b1 \
libfontconfig1=2.11.0-6.7+b1 \
chromium-browser
sudo dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome
rm ./google-chrome-stable_current_amd64.deb
cd $HOME/project/src # Make sure we return to where we were
echo "Chrome at $STORAGE_DIR/chrome"
else
echo "...Using Chrome from cache"
fi

pip install --upgrade pip
pip install -r requirements.txt
