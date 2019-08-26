#!/bin/bash

# Descargamos oh-my-zsh
wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O - | sh

# Cambia el tema por agnoster
sudo sed -i 's/ZSH_THEME=\"robbyrussell\"/ZSH_THEME=\"agnoster\"/g' ~/.zshrc

# Plugins
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# Activando plugins y configuraciones varias
sudo sed -i 's/plugins=(git)/plugins=(git zsh-autosuggestions zsh-syntax-highlighting)/g' ~/.zshrc
# Nombre de usuario del prompt
echo "DEFAULT_USER=`whoami`" >> ~/.zshrc

# Establece la consola ZSH por defecto
sudo chsh $USER -s /bin/zsh

# Recargamos configuracion de zsh
source ~/.zshrc

echo "################### zsh + oh-my-zsh instalada ######################"
