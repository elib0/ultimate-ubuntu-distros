#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import os, sys
import subprocess
from pprint import pprint
from pathlib import Path

import emoji
import click
from oquestionary import prompt
from colors import *  # ANSI colors
from pyfiglet import Figlet

from file_handler import FileHandler


class SecondStep:
    # Constantes para prioridad de categoría a instalar
    class STEP:
        PRE = '1'
        APT = '2'
        PIP = '3'
        POST = '4'

    SCRIPT_PATH = os.path.dirname(os.path.realpath(sys.argv[0]))
    APPLICATIONS={}

    def __init__(self, menu_file='menu.json'):
        # Creamos menu con nombre por defecto del archivo "menu.json"
        self.APPLICATIONS = FileHandler(menu_file=menu_file).get_menu()

    def run(self):
        """Corre el cli"""

        STEP = self.STEP

        def run_with(name_file):
            """Define que comando se corre en SH o PYTHON o cualquier otro de acuerdo a su extensión"""
            cmd = 'sh'
            cmd = Path(script).suffix.replace('.', '')
            if(cmd == 'py'):
                cmd = 'python'
            return cmd


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
            r = {STEP.PRE: [], STEP.APT: '', STEP.PIP: '', STEP.POST: []}
            for cat in answers.keys():
                if isinstance(answers[cat], list):
                    for app in answers[cat]:
                        if app in self.APPLICATIONS[cat]['programs'].keys():
                            if 'pre' in self.APPLICATIONS[cat]['programs'][app]:
                                r[STEP.PRE].append(self.APPLICATIONS[cat]['programs'][app]['pre'])
                            if 'apt' in self.APPLICATIONS[cat]['programs'][app]:
                                r[STEP.APT] += self.APPLICATIONS[cat]['programs'][app]['apt'] + ' '
                            if 'pip' in self.APPLICATIONS[cat]['programs'][app]:
                                r[STEP.PIP] += self.APPLICATIONS[cat]['programs'][app]['pip'] + ' '
                            if 'post' in self.APPLICATIONS[cat]['programs'][app]:
                                r[STEP.POST].append(self.APPLICATIONS[cat]['programs'][app]['post'])

            return r

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
        steps = process_selection(answers)
        # Post(paso 4) Instalación requerida por algunas dependencias por defecto
        steps[STEP.POST] = FileHandler(default_file='defaults.json').get_post_installations() + steps[STEP.POST]
        #exit(pprint(steps))
        for [step, installations] in steps.items():
            if len(installations) > 0:
                if isinstance(installations, list):
                    updatable = False # Comprobar si hace falta apt-get update después de un script
                    for script in installations:
                        cmd = run_with(script)
                        if 'addrepo' in script: # Si algún script agrega a repo
                            updatable = True    # entonces es updatable.
                        file = f"{self.SCRIPT_PATH}/scripts/{script}" # Path absoluto para que funcione el script solo
                        if os.path.exists(file):
                            subprocess.call(cmd + ' ' + file, shell=True)

                    if updatable:
                        subprocess.call("sudo apt-get update", shell=True)
                elif is_string(installations):
                    cmd = 'sudo apt-get install -y'
                    if step == STEP.PIP:
                        cmd = 'pip install'
                    subprocess.call(f"{cmd} {installations}", shell=True)

#click
@click.command()
@click.option('-f', '--menu-file', default='menu.json', help='Archivo JSON para el menú.')
def run(menu_file):
    """
    Menú principal para Ultimate Ubuntu Distros,
    Instala programas marcados por el usuario de una manera fácil y rápida.
    """
    return SecondStep(menu_file).run()

# Inicio del CLi ## REF: https://es.stackoverflow.com/questions/32165/qué-es-if-name-main
if __name__ == '__main__':
    run()