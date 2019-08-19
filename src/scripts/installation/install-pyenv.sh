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
git clone https://github.com/momo-lab/pyenv-install-latest.git "$(pyenv root)"/plugins/pyenv-install-latest


# Variables de entorno
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

# Recargamos configuracion de oh-my-zsh
source ~/.zshrc

# Instalamos ultima version de Python 3
pyenv install-latest

echo "#########################################################################"
echo "################# Python version management instalado ###################"
echo "#########################################################################"