#!/bin/bash
#

rm /tmp/sublime-text_build-3176_amd64.deb

wget https://download.sublimetext.com/sublime-text_build-3176_amd64.deb -O /tmp/sublime-text_build-3176_amd64.deb

sudo dpkg -i /tmp/sublime-text_build-3176_amd64.deb

rm /tmp/sublime-text_build-3176_amd64.deb


##################################################################################################################

echo "################################################################"
echo "################      sublime text installed    ################"
echo "################################################################"

