#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import subprocess, sys, os, json
from pprint import pprint
from colors import * # ANSI colors
from PyInquirer import style_from_dict, Token, prompt, Separator
from pyfiglet import Figlet
import emoji

# Themes from PyInquirer
from examples import custom_style_3 as style3

class Main:
    def read_default_apps(self):
        name = 'default.txt'
        path = os.path.dirname(os.path.realpath(sys.argv[0]))  # Path to script
        # Si borran el archivo o x
        lines = [
            'make', 'build-essential', 'git', 'libssl-dev', 'zlib1g-dev', 'libbz2-dev', 'libreadline-dev',
            'libsqlite3-dev', 'wget', 'curl', 'llvm', 'libncurses5-dev', 'libncursesw5-dev', 'xz-utils', 'tk-dev', 'libffi-dev'
        ]
        if os.path.exists(f"{path}/{name}"):
            f = open(f"{path}/{name}", 'r')
            lines = [line.replace('\n', '') for line in f.readlines()] # Remplazo final de linea '\n' con ''
            f.close()
        return lines

    def read_menu(self):
        name = 'menu.json'
        path = os.path.dirname(os.path.realpath(sys.argv[0]))  # Path to script
        f = open(f"{path}/{name}", 'r')
        return json.load(f)

    def dict_to_choices(dict):
        choices = []
        for (key, value) in dict.items():
            checked = False
            if 'checked' in value:
                checked =  value['checked']
            choices.append({'name': key, 'checked': checked})

        return choices

    APPLICATIONS = read_menu(None)
    questions = [
        {
            'type': 'confirm',
            'name': 'utiles',
            'message': '¿Quieres instalar Utilidades?'
        },
        {
            'type': 'checkbox',
            'name': 'utiles',
            'message': '¿Que Utilidades deseas instalar?',
            'choices': dict_to_choices(APPLICATIONS['utiles']),
            'when': lambda answers: answers['utiles']
        },
        {
            'type': 'confirm',
            'name': 'compressors',
            'message': '¿Quieres instalar Des/Compresores?'
        },
        {
            'type': 'checkbox',
            'name': 'compressors',
            'message': '¿Que Des/Compresores deseas instalar?',
            'choices': dict_to_choices(APPLICATIONS['compressors']),
            'when': lambda answers: answers['compressors']
        },
        {
            'type': 'confirm',
            'name': 'browsers',
            'message': '¿Quieres instalar Navegadores Web?'
        },
        {
            'type': 'checkbox',
            'name': 'browsers',
            'message': '¿Que Navegadores Web deseas instalar?',
            'choices': dict_to_choices(APPLICATIONS['browsers']),
            'when': lambda answers: answers['browsers']
        },
        {
            'type': 'confirm',
            'name': 'develop',
            'message': '¿Quieres instalar herramientas de desarrollo?'
        },
        {
            'type': 'checkbox',
            'name': 'develop',
            'message': '¿Que herramientas de desarrollo deseas instalar?',
            'choices': dict_to_choices(APPLICATIONS['develop']),
            'when': lambda answers: answers['develop']
        }
    ]

    def run(self):

        def process_selection(answers):
            program_list_selected_apt = ''
            program_list_selected_sh = []
            for cat in answers.keys():
                # program_list_selected = ' '.join(str(a) for a in answers[k])
                if isinstance(self.APPLICATIONS[cat], list):
                    for app in answers[cat]:
                        if app in self.APPLICATIONS[cat]:
                            # Primero corremos los sh por que algunos tienen PPAs nada mas
                            if 'script' in self.APPLICATIONS[cat][app]:
                                program_list_selected_sh.append(self.APPLICATIONS[cat][app]['script'])

                            if 'apt' in self.APPLICATIONS[cat][app]:
                                program_list_selected_apt += self.APPLICATIONS[cat][app]['apt'] + ' '


            return program_list_selected_apt, program_list_selected_sh

        # Limpia pantalla y muestra info del programa
        def show_info():
            subprocess.call('clear')
            f = Figlet(font='slant')

            print(emoji.emojize( f"""
    {f.renderText('by: elib0')}
    :question: Scrip para personalizar Linux Mint 19.2,
    también debería funcionar correctamente con los derivados de Ubuntu 18.04.""", use_aliases=True))

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

        # Inicio del script
        show_info()

        # Instalar librerías necesarias para el script
        program_list_selected = ' '.join(str(a) for a in self.read_default_apps())
        subprocess.call('sudo apt-get update', shell=True)
        subprocess.call('sudo apt-get upgrade', shell=True)
        subprocess.call('sudo apt-get install ' + program_list_selected, shell=True) # Instala dependencias necesarias para continuar con los demas
        # Menu
        show_info()
        answers = prompt(self.questions, style=style3)
        apts, scripts = process_selection(answers)
        # sh
        if (len(scripts) > 0):
            pprint(scripts) #TODO: Faltan recorrer los ssh
        # apt-get
        if (len(apts) > 0):
            # Ya se agregaron los repos nuevos actualizamos para poder instalar
            subprocess.call('sudo apt-get update', shell=True)
            # Instala dependencias necesarias para continuar con los demas
            subprocess.call('sudo apt-get install ' + apts, shell=True)

# Inicio del CLi
Main().run()