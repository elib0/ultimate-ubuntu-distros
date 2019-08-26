#!/bin/bash

# Clonando nvm
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash

# Variables de entorno
echo '#NVM' >> ~/.zshrc
echo 'export NVM_DIR="$HOME/.nvm"' >> ~/.zshrc
echo '[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm' >> ~/.zshrc
echo '[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_comletion' >> ~/.zshrc

# Recargamos configuracion de oh-my-zsh
source ~/.zshrc

# Instalamos ultima version LTS estable
nvm install --lts

echo "################# Python version management instalado ###################"