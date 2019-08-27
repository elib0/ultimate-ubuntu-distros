#!/bin/bash

APPNAME="Discord"
FILENAME="discord_lastes.deb"
URL="https://discordapp.com/api/download?platform=linux&format=deb"

sudo rm /tmp/$FILENAME

echo "Descargando $APPNAME stable"
sudo wget $URL -O /tmp/$FILENAME
sudo dpkg -i /tmp/$FILENAME

sudo rm /tmp/$FILENAME

echo "################### $APPNAME instalado #################"
