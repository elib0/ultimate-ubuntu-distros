#!/bin/bash

APPNAME="MySQL APT Repository"
FILENAME="mysql-apt-repository.deb"
URL="https://repo.mysql.com//mysql-apt-config_0.8.13-1_all.deb"

sudo rm /tmp/$FILENAME

echo "Descargando $APPNAME"
sudo wget $URL -O /tmp/$FILENAME
sudo dpkg -i /tmp/$FILENAME

sudo rm /tmp/$FILENAME

echo "################### $APPNAME instalado #################"
