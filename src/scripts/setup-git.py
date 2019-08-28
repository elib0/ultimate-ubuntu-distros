#!/usr/bin/env python
# -*- coding: utf-8 -*-

import emoji
#from colors import *  # ANSI colors
from subprocess import call
from os.path import exists
from os import environ
from questionary import confirm, text
from shutil import which

email=''
username=environ['USERNAME']
r=confirm('¿Deseas configurar GIT?').ask()

if(r):
	#global Config
	username = text("Escribe tu nombre de usuario(por defecto:" + username + "):").ask()
	if(not username):
		username = environ['USERNAME']
	email = text(f"Escribe tu correo electrónico:").ask()
	call('git config --global user.name' + username, shell=True)
	call('git config --global user.email' + email, shell=True)
	#Generar SSH
	file_name = 'id_ed25519.pub'
	if not exists(environ['HOME'] + "/" + file_name):
		r = confirm('NO Tienes clave ed25519 SSH, ¿Quieres generar una clave SSH para Github/Gitlab?')
		if (r):
			call('ssh-keygen -t ed25519 -C ' + email, shell=True)
			call('sudo apt-get install -y xclip', shell=True)
			call('xclip -sel clip < ~/.ssh/id_ed25519.pub', shell=True)
			print('Clave SSH copiada al porta papeles!' + emoji.emojize(':clipboard:'))


