#!/bin/bash

APPNAME="Google Chrome"
FILENAME="google-chrome-stable_current_amd64.deb"
URL="https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"

sudo rm /tmp/$FILENAME

echo "Descargando $APPNAME stable"
sudo wget $URL -O /tmp/$FILENAME
sudo dpkg -i /tmp/$FILENAME

sudo rm /tmp/$FILENAME

echo "################### $APPNAME instalado #################"
