#!/bin/bash
#

# Installing the GPG key
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -

# Selecting the channel to use
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

##################################################################################################################

echo "################################################################"
echo "################      sublime text instalado    ################"
echo "################################################################"

