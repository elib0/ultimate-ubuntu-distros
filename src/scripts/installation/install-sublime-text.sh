#!/bin/bash
#

#rm /tmp/sublime-text_amd64.deb

#wget https://download.sublimetext.com/sublime-text_build-3208_amd64.deb -O /tmp/sublime-text_amd64.deb

#sudo dpkg -i /tmp/sublime-text_amd64.deb

#rm /tmp/sublime-text_amd64.deb

# Installing the GPG key
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -

# Selecting the channel to use
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

sudo apt-get update

sudo apt-get install sublime-text -y


##################################################################################################################

echo "################################################################"
echo "################      sublime text installed    ################"
echo "################################################################"

