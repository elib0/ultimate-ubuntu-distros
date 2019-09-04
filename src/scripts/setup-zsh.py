#!/usr/bin/env python
# -*- coding: utf-8 -*-

from colors import *  # ANSI colors
from subprocess import call
from os.path import exists
from os import environ
from questionary import confirm, text

zshrc = '.zshrc'
home_path = environ['HOME']

r = confirm('¿Deseas instalar el framework Oh My ZSH? (Muy Recomendado)').ask()

if r:
    call('wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O - | sh', shell=True)

    if exists(home_path + '/' + '.oh-my-zsh/') and exists(home_path + '/' + zshrc):
        r = confirm('¿Deseas configurar ZSH y OH MY ZSH?').ask()

        if r:
            try:
                with open(home_path + '/' + zshrc, 'r') as f:
                    lines = f.read()
                    # Cambio de tema
                    r = confirm('¿Desea cambiar el tema random por Agnoster? (Recomendado)').ask()
                    if r:
                        lines = lines.replace('ZSH_THEME="robbyrussell"', 'ZSH_THEME="agnoster"')
                        print('¡Recuerda cambiar la fuente de tu consola a una compatible con Powerline!')
                        # Nombre Corto
                        r = confirm('¿Desea cambiar el identificador de usuario al corto? (Recomendado)').ask()
                        if r:
                            if "DEFAULT_USER=`whoami`\n" not in lines:
                                lines += "\n#User Name\nDEFAULT_USER=`whoami`\n"
                    # Plugins
                    r = confirm('¿Quieres instalar los plugins: "autosuggestions" y "syntax-highlighting"? (Muy '
                                'Recomendado)').ask()
                    if r:
                        call('git clone https://github.com/zsh-users/zsh-autosuggestions ${'
                             'ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions', shell=True)
                        call('git clone https://github.com/zsh-users/zsh-autosuggestions ${'
                             'ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions', shell=True)
                        lines = lines.replace('plugins=(git)', 'plugins=(git zsh-autosuggestions zsh-syntax-highlighting)')
                    # Entorno y Aliases
                    if exists(home_path + '/' + '.pyenv/'):
                        line = 'export PYENV_ROOT="$HOME/.pyenv"\nexport PATH="$PYENV_ROOT/bin:$PATH"\neval ' \
                               '"$(pyenv init -)"\neval "$(pyenv virtualenv-init -)"\n'
                        if line not in lines:
                            lines += '\n# PyEnv\n' + line
                    if exists(home_path + '/' + '.nvm'):
                        line = 'export NVM_DIR="$HOME/.nvm"\n[ -s "$NVM_DIR/nvm.sh" ] && \\. "$NVM_DIR/nvm.sh"  # This ' \
                               'loads nvm\n[ -s "$NVM_DIR/bash_completion" ] && \\. "$NVM_DIR/bash_completion"  # This ' \
                               'loads nvm bash_completion\n'
                        if line not in lines:
                            lines += '\n#NVM\n' + line
                    # Iterprestes python
                    ipython_installed = exists(home_path + '/' + '.ipython')
                    ptpython_installed = exists(home_path + '/' + '.ptpython')
                    if ipython_installed and ptpython_installed:
                        r = confirm('Hemos detectado que tienes instalado los interpretes iPython y Ptpython, ¿Quieres '
                                    'agregar un alias para abrir el interprete rápidamente(Recomendado)?').ask()
                        if r:
                            alias = text('Cual sera el nombre del alias(Predeterminado: pyt):').ask() or 'pyt'
                            line = 'alias '+alias+'="ptipython"\n'
                            if line not in lines:
                                lines += '\n# Aliases\n' + line
                    else:
                        if ipython_installed:
                            pass
                        if ptpython_installed:
                            pass
                    # Escribimos configuración final...
                    with open(home_path + '/' + zshrc, 'w') as f:
                        f.write(lines)
            except PermissionError:
                print('¡Error con los permisos del archivo:' + zshrc + '!')
            except FileNotFoundError:
                print('¡Error, el archivo no existe!')

        r = confirm('¿Quieres que ZSH sea tu bash por defecto?').ask()
        if r:
            call('chsh -s $(which zsh)', shell=True)

        print(color('corre el comando: ', 'red') + 'source ' + home_path + '/' + zshrc)
