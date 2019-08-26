#!/bin/bash

APPNAME="Opera Browser"
FILENAME="opera-stable_current_amd64.deb"
URL="https://download3.operacdn.com/pub/opera/desktop/62.0.3331.99/linux/opera-stable_62.0.3331.99_amd64.deb"

sudo rm /tmp/$FILENAME

echo "Descargando $APPNAME stable"
sudo wget $URL -O /tmp/$FILENAME
sudo dpkg -i /tmp/$FILENAME

sudo rm /tmp/$FILENAME

echo "################### $APPNAME instalado #################"
