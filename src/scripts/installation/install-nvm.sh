#!/bin/bash
#

# Clonando nvm
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash

# Variables de entorno

# Recargamos configuracion de oh-my-zsh
source ~/.zshrc

# Instalamos ultiima version LTS estable
nvm install --lts

echo "#########################################################################"
echo "################# Python version management instalado ###################"
echo "#########################################################################"