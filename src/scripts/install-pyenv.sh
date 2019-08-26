#!/bin/bash

# Variables
BASHPATH=$HOME/.bashrc # or .zshrc

# Clonando pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# Clonando plugin para enviroments y ultima version python
git clone https://github.com/pyenv/pyenv-virtualenv.git $HOME/.pyenv/plugins/pyenv-virtualenv ~/.pyenv/plugins

# Variables de entorno plugins
echo '# PyEnv' >> $BASHPATH
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> $BASHPATH
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> $BASHPATH
echo 'eval "$(pyenv init -)"' >> $BASHPATH
echo 'eval "$(pyenv virtualenv-init -)"' >> $BASHPATH

# Recargamos configuracion de bash por defecto
source $BASHPATH

# Instalamos version 3.7.4 de Python
pyenv install 3.7.4
pyenv global 3.7.4 # la establecemos como predeterminada

# Requerimientos de main.py script ##REF: https://realpython.com/what-is-pip/
pip install -r requirements.txt #Instalamos con archivo de requerimientos del cli

echo "################# Python version management instalado ###################"
