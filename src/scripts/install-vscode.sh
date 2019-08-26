#!/bin/bash

APPNAME="Steam"
FILENAME="vscode-stable_current_amd64.deb"
URL="https://az764295.vo.msecnd.net/stable/2213894ea0415ee8c85c5eea0d0ff81ecc191529/code_1.36.1-1562627527_amd64.deb"

sudo rm /tmp/$FILENAME

echo "Descargando $APPNAME latest stable edition"
sudo wget $URL -O /tmp/$FILENAME
sudo dpkg -i /tmp/$FILENAME

sudo rm /tmp/$FILENAME

echo "################### $APPNAME instalado #################"
