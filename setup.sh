#!/usr/bin/env bash
#exit on error
set -o errexit

STORAGE_DIR=/opt/render/project/.render
if [[ ! -d $STORAGE_DIR/chrome ]]; then
echo "…Downloading Chrome"
mkdir -p $STORAGE_DIR/chrome
cd $STORAGE_DIR/chrome
wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome
ln -sr /usr/bin/chrome
rm ./google-chrome-stable_current_amd64.deb
cd $HOME/project/src # Make sure we return to where we were
echo "Installed Chrome"
echo "Instalando o chromedriver"
wget -P ./ https://chromedriver.storage.googleapis.com/112.0.5615.49/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
echo "Chromedriver instalado "
else
echo "…Using Chrome from cache"
fi

pip install -r requirements.txt;
