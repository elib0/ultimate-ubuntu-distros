#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess, sys, os

class FirstStep:

  def read_default_apps(self):
        name = 'default.txt'
        path = os.path.dirname(os.path.realpath(sys.argv[0]))  # Path to script
        # Si borran el archivo o x
        lines = [
            'make', 'build-essential', 'git', 'libssl-dev', 'zlib1g-dev', 'libbz2-dev', 'libreadline-dev',
            'libsqlite3-dev', 'wget', 'curl', 'llvm', 'libncurses5-dev', 'libncursesw5-dev', 'xz-utils', 'tk-dev', 'libffi-dev'
        ]
        if os.path.exists(path + "/" + name):
            f = open(path + "/" + name)
            lines = [line.replace('\n', '') for line in f.readlines()] # Remplazo final de linea '\n' con ''
            f.close()
        return lines

  def run(self):
    # 1. Actualiza repos y arma dependencias necesarias
    program_list_selected = ' '.join(str(a) for a in self.read_default_apps())
    subprocess.call('sudo apt-get update', shell=True)
    subprocess.call('sudo apt-get upgrade', shell=True)
    # 2. Instala dependencias necesarias para continuar con el resto del script
    subprocess.call('sudo apt-get install -y ' + program_list_selected, shell=True)
    # 3. Instala oh-my-zsh ¿Alfin y al cabo, a quien no le gusta una consola bonita?
    #subprocess.call('sh src/scripts/install-zsh.sh', shell=True)
    # 4. Instala PyENV y agrega python 3.7.4 como predeterminado python
    subprocess.call('sh src/scripts/install-pyenv.sh', shell=True)
    # 5. Corre Script principal
    subprocess.call('python src/main.py', shell=True)

# Inicio del script
FirstStep().run()
