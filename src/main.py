#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import json
import os
import subprocess
from pprint import pprint

import emoji
from PyInquirer import prompt
from colors import *  # ANSI colors
# Themes from PyInquirer
from examples import custom_style_3 as style3
from pyfiglet import Figlet

class Main:

    def distro_info(self):
        info = subprocess.check_output('lsb_release -a', shell=True)
        info = str(info) # Convierto a string normal y no binario
        info.replace('\\t', '')
        return info.splitlines()

    def read_menu(self):
        path = os.path.dirname(os.path.realpath(sys.argv[0]))  # Path to script
        name = 'menu.json'
        f = open(f"{path}/{name}", 'r')
        return json.load(f)

    APPLICATIONS = read_menu(None)

    def run(self):
        # answers = [cat for cat in self.APPLICATIONS.keys()]

        def dict_to_choices(dict):
            choices = []
            for (key, value) in dict.items():
                checked = False
                if 'checked' in value:
                    checked = value['checked']
                choices.append({'name': key, 'checked': checked})

            return choices

        def build_menu():
            menu = []
            for (cat, m) in self.APPLICATIONS.items():
                menu.append({'type': 'confirm', 'name': 'install', 'message': m['message1']})
                menu.append(
                    {
                        'type': 'checkbox',
                        'name': 'install',
                        'message': m['message2'],
                        'choices': dict_to_choices(m['programs']),
                        'when': lambda answers: answers.get('install', False)
                    }
                )

            return menu

        def process_selection(answers):
            program_list_selected_apt = ''
            program_list_selected_sh = []
            for cat in answers.keys():
                # program_list_selected = ' '.join(str(a) for a in answers[k])
                if isinstance(answers[cat], list):
                    for app in answers[cat]:
                        if app in self.APPLICATIONS[cat]:
                            # Primero corremos los sh por que algunos tienen PPAs nada mas
                            if 'script' in self.APPLICATIONS[cat][app]:
                                program_list_selected_sh.append(self.APPLICATIONS[cat][app]['script'])

                            if 'apt' in self.APPLICATIONS[cat][app]:
                                program_list_selected_apt += self.APPLICATIONS[cat][app]['apt'] + ' '

            return program_list_selected_sh, program_list_selected_apt

        # Limpia pantalla y muestra info del programa
        def show_info():
            subprocess.call('clear')
            f = Figlet(font='slant')

            print(emoji.emojize( f"""
    {f.renderText('by: elib0')}
    :question: Scrip para personalizar Linux, probando en: {color('Mint 19.2 y POP!_OS 19.04', 'red')}
    también debería funcionar correctamente con los derivados de {color('Ubuntu 18.04+', 'green')}""", use_aliases=True))

            print( emoji.emojize(f"""
    :exclamation: {color('ADVERTENCIA', 'red')}: este script descarga parte de los paquetes de sus paginas oficiales,
    en consecuencia no se garantiza que estén actualizados al dia; Sin embargo los paquetes
    agregan sus repositorios oficiales PPA por lo tanto mediante un simple:
    \'apt upgrade\' se actualizaran.""", use_aliases=True))

            print (f"""
    {color('TWITTER: ', '#1da1f2')}https://twitter.com/elib0
    {color('GITLAB:  ', '#e24329')}https://gitlab.com/elib0
    {color('GITHUB:  ', '#fff')}https://github.com/elib0
    {emoji.emojize('Code with :heart: and :coffee:', use_aliases=True)}
            """)  # Using string Interpolation / f-Strings Python 3.6+

        # Menu
        show_info()
        answers = prompt(build_menu(), style=style3)
        scripts, apts = process_selection(answers)
        # sh
        if (len(scripts) > 0):
            for script in scripts:
                subprocess.call(f"sh src/scripts/{script}", shell=True)
        # apt-get
        if (len(apts) > 0):
            # Ya se agregaron los repos nuevos actualizamos para poder instalar
            subprocess.call('sudo apt-get update', shell=True)
            # Instala dependencias necesarias para continuar con los demas
            subprocess.call(f'sudo apt-get install -y {apts}', shell=True)

# Inicio del CLi
Main().run()