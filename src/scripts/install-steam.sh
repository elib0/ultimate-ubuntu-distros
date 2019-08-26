#!/bin/bash

APPNAME="Steam"
FILENAME="steam-latest.deb"
URL="http://repo.steampowered.com/steam/archive/precise/steam_latest.deb"

sudo rm /tmp/$FILENAME

echo "Descargando $APPNAME latest"
sudo wget $URL -O /tmp/$FILENAME
sudo dpkg -i /tmp/$FILENAME

sudo rm /tmp/$FILENAME

echo "################### $APPNAME instalado #################"