#!/bin/bash
#

# Fuentes para que se vea bien el tema agnoster
sudo apt-get install fonts-powerline

sudo apt-get install zsh -y
wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O - | sh

# changing the theme to agnoster

sudo sed -i 's/ZSH_THEME=\"robbyrussell\"/ZSH_THEME=\"agnoster\"/g' ~/.zshrc

# If above line did not work somehow. This is what you should do to enjoy the many themes.
# go find the hidden .zshrc file and look for ZSH_THEME="robbyrussell" (CTRL+H to find hidden files)
# change this to ZSH_THEME="random"

# Plugins
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# Activando plugins y configuraciones varias
#plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
## Nombre de usuario del prompt
#DEFAULT_USER=`whoami`
## PyEnv
#export PYENV_ROOT="$HOME/.pyenv"
#export PATH="$PYENV_ROOT/bin:$PATH"
#eval "$(pyenv init -)"
#eval "$(pyenv virtualenv-init -)"
##NVM
#export NVM_DIR="$HOME/.nvm"
#[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
#[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_comletion


# Establece la consola ZSH por defecto
sudo chsh $USER -s /bin/zsh
echo
echo
#echo
echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
#echo "This is for the script of ZSH - Colouring of your terminal"
#echo "You do not get the chance to type your password"
#echo "Retype this line again and fill in your own username"
#echo "sudo chsh username -s /bin/zsh, Ex: $USER"
#echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
#echo
#echo
echo "Cirra sesion o reinicia para que la nueva consola tenga efecto".
echo "----------------------------------------------------"


echo "################################################################"
echo "###################    zsh instalada     ######################"
echo "################################################################"
