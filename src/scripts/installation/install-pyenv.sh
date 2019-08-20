#!/bin/bash
# Este script tiene que correr depues de instalar zsh

# Clonando pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# Variables de entorno
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc

# Recargamos configuracion de oh-my-zsh
source ~/.zshrc

# Clonadno plugin para enviroments y ultima version python
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv ~/.pyenv/plugins
#git clone https://github.com/momo-lab/pyenv-install-latest.git "$(pyenv root)"/plugins/pyenv-install-latest


# Variables de entorno plugins
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

# Recargamos configuracion de oh-my-zsh
source ~/.zshrc

# Instalamos version 3.7.4 de Python
pyenv install 3.7.4
pyenv global 3.7.4 # la establecemos como predeterminada
#pyenv install-latest

# Recargamos configuracion de oh-my-zsh
source ~/.zshrc

# Requerimientos de main script
# pip install PyInquirer emoji ansicolors pyfiglet

echo "#########################################################################"
echo "################# Python version management instalado ###################"
echo "#########################################################################"