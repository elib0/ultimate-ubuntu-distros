#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import json
import os
import subprocess
from pprint import pprint

import emoji
import click
from questionary import prompt
from colors import *  # ANSI colors
from pyfiglet import Figlet


class Main:
    APPLICATIONS = {}

    def __init__(self, menu_file='menu.json'):
        # Creamos menu con nombre por defecto del archivo "menu.json"
        self.APPLICATIONS = self.read_menu(menu_file)

    def read_menu(self, file_name):
        """Lee el archivo de menú que esta en la raíz del script"""
        path = os.path.dirname(os.path.realpath(sys.argv[0]))  # Path to script
        f = open(f'{path}/{file_name}', 'r')
        return json.load(f)

    def run(self):
        """Corre el cli"""
        def dict_to_choices(programs):
            """Convierte diccionario en selecciones para questionary"""
            choices = []
            for (key, value) in programs.items():
                checked = False
                if 'checked' in value:
                    checked = value['checked']
                choices.append({'name': key, 'checked': checked})

            return choices

        def build_menu():
            """Construye el menú a partir del archivo json"""
            menu = []
            for (cat, m) in self.APPLICATIONS.items():
                menu.append({'type': 'confirm', 'name': 'install', 'message': m['message1'], 'default': True})
                menu.append(
                    {
                        'type': 'checkbox',
                        'name': cat,
                        'message': m['message2'],
                        'choices': dict_to_choices(m['programs']),
                        'when': lambda answers: answers['install']
                    }
                )

            return menu

        def process_selection(answers):
            """Procesa las selecciones del usuario con el questionary"""
            _scripts = []; _posts = []; _apts = ''; _pips = ''
            for cat in answers.keys():
                # program_list_selected = ' '.join(str(a) for a in answers[k])
                if isinstance(answers[cat], list):
                    for app in answers[cat]:
                        if app in self.APPLICATIONS[cat]['programs'].keys():
                            # Primero corremos los scripts por que algunos tienen PPAs nada mas
                            if 'script' in self.APPLICATIONS[cat]['programs'][app]:
                                _scripts.append(self.APPLICATIONS[cat]['programs'][app]['script'])

                            if 'apt' in self.APPLICATIONS[cat]['programs'][app]:
                                _apts += self.APPLICATIONS[cat]['programs'][app]['apt'] + ' '

                            if 'pip' in self.APPLICATIONS[cat]['programs'][app]:
                                _pips += self.APPLICATIONS[cat]['programs'][app]['pip'] + ' '

                            if 'post' in self.APPLICATIONS[cat]['programs'][app]:
                                _posts.append(self.APPLICATIONS[cat]['programs'][app]['post'])

            return _scripts, _apts, _pips, _posts

        def show_info():
            """Limpia pantalla y muestra info del programa"""
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
        answers = prompt(build_menu())
        scripts, apts, pips, post_scripts = process_selection(answers)
        #pprint(apts); exit();
        # sh
        if (len(scripts) > 0):
            for script in scripts:
                subprocess.call(f"sh src/scripts/{script}", shell=True)
        # apt-get
        if (len(apts) > 0):
            # Ya se agregaron los repos nuevos actualizamos para poder instalar
            subprocess.call('sudo apt-get update', shell=True)
            subprocess.call(f'sudo apt-get install -y {apts}', shell=True)
        # Package manager for Python(pip)
        if (len(pips) > 0):
            subprocess.call(f'pip install {pips}', shell=True)

#click
@click.command()
@click.option('-f', '--menu-file', default='menu.json', help='Archivo JSON para el menú.')
def run(menu_file):
    return Main(menu_file).run()

# Inicio del CLi ## REF: https://es.stackoverflow.com/questions/32165/qué-es-if-name-main
if __name__ == '__main__':
    run()