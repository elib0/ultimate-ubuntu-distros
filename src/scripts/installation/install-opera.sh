#!/bin/bash
#

rm /tmp/opera-stable_current_amd64.deb

echo "Descargando opera browser latest stable edition"
wget https://download3.operacdn.com/pub/opera/desktop/62.0.3331.99/linux/opera-stable_62.0.3331.99_amd64.deb -O /tmp/opera-stable_current_amd64.deb
sudo dpkg -i /tmp/opera-stable_current_amd64.deb

rm /tmp/opera-stable_current_amd64.deb

echo "################################################################"
echo "####################  opera browser installed ##################"
echo "################################################################"
