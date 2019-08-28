#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

from file_handler import FileHandler


class FirstStep:
    APPLICATIONS = ''

    def __init__(self, default_file='defaults.json'):
        self.APPLICATIONS = FileHandler(default_file=default_file).get_pre_installations(to_string=True)

    def run(self):
        # 1. Actualiza repos y actualiza aplicaciones
        subprocess.call('sudo apt-get update', shell=True)
        subprocess.call('sudo apt-get upgrade', shell=True)
        # 2. Instala dependencias necesarias para continuar con el resto del script
        subprocess.call('sudo apt-get install -y ' + self.APPLICATIONS, shell=True)
        # 3. Instala PyENV y agrega python 3.7.4 como predeterminado python
        #subprocess.call('sh scripts/install-pyenv.sh', shell=True)


# Inicio del script
FirstStep().run()
