#!/bin/bash
#

# Selecting the channel to use
sudo add-apt-repository 'deb http://repo.vivaldi.com/archive/deb/ stable main'

# Installing the GPG key
wget -qO- http://repo.vivaldi.com/archive/linux_signing_key.pub | sudo apt-key add -


##################################################################################################################

echo "################################################################"
echo "###################     vivaldi instalado    ###################"
echo "################################################################"


