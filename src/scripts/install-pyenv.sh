#!/bin/bash

# Clonando pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# Variables de entorno
#echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
#echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
#echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
echo '# PyEnv' >> ~/.zshrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# Recargamos configuracion de bash por defecto
source ~/.zshrc

# Clonando plugin para enviroments y ultima version python
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv ~/.pyenv/plugins
#git clone https://github.com/momo-lab/pyenv-install-latest.git "$(pyenv root)"/plugins/pyenv-install-latest

# Variables de entorno plugins
#echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

# Recargamos configuracion de bash por defecto
source ~/.zshrc

# Instalamos version 3.7.4 de Python
pyenv install 3.7.4
pyenv global 3.7.4 # la establecemos como predeterminada
#pyenv install-latest

# Requerimientos de main.py script ##REF: https://realpython.com/what-is-pip/
#pip install PyInquirer emoji ansicolors pyfiglet
pip install -r ../../requirements.txt #Instalamos con archivo de requerimientos del cli

echo "#########################################################################"
echo "################# Python version management instalado ###################"
echo "#########################################################################"
