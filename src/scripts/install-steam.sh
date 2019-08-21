#!/bin/bash

rm /tmp/steam-stable.deb

echo "Descargando steam"
wget http://repo.steampowered.com/steam/archive/precise/steam_latest.deb -O /tmp/steam-stable.deb
sudo dpkg -i /tmp/steam-stable.deb

rm /tmp/steam-stable.deb

echo "################################################################"
echo "########################  Steam instalado ######################"
echo "################################################################"
