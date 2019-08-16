from __future__ import print_function, unicode_literals
import os
import subprocess
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt, Separator
from pyfiglet import Figlet
import emoji

# Themes from PyInquirer
from examples import custom_style_3 as style3


class Main:
    def dict_to_choices(dict):
        choices = []
        for (key, value) in dict.items():
            if 'checked' in value:
                checked =  value['checked']
            else:
                checked = False
            choices.append({'name': key, 'checked': checked})

        return choices

    APPLICATIONS = {
        'UTILES': {
            'openshot': {'name': 'openshot'},
            'plank': {'name': 'plank', 'checked': True},
            'variety': {'name': 'variety', 'checked': True, 'script': 'install-variety.sh'},
            'ppa-purge': {'name': 'ppa-purge', 'checked': True},
            'shutter': {'name': 'shutter'},
            'dconf-tools': {'name': 'dconf-tools', 'checked': True}
        },
        'COMPRESION': {
            'p7zip-rar': {'name': 'p7zip-rar', 'checked': True},
            'p7zip-full': {'name': 'p7zip-full', 'checked': True},
            'unace': {'name': 'unace', 'checked': True},
            'unrar': {'name': 'unrar', 'checked': True},
            'zip': {'name': 'zip', 'checked': True},
            'unzip': {'name': 'unzip', 'checked': True},
            'sharutils': {'name': 'sharutils', 'checked': True},
            'rar': {'name': 'rar', 'checked': True},
            'uudeview': {'name': 'uudeview', 'checked': True},
            'mpack': {'name': 'mpack', 'checked': True},
            'arj': {'name': 'arj', 'checked': True},
            'cabextract': {'name': 'cabextract', 'checked': True},
            'file-roller': {'name': 'file-roller', 'checked': True}
        },
        'BROWSERS': {
            'Google Chrome(Stable Channel)': {'name': None, 'checked': True, 'script': 'install-google-chrome.sh'},
            'Opera Browser(Stable Channel)': {'name': None, 'checked': True, 'script': 'install-opera.sh'},
            'Vilvadi Browser(Stable Channel)': {'name': 'vivaldi-stable', 'script': 'install-vivaldi.sh'}
        },
        'DEVELOPER': {
            'Visual Studio Code(Stable Channel)': {'name': None, 'checked': True},
            'Sublime Text 3(Stable Channel)': {'name': 'sublime-text', 'checked': True},
            'Node Version Manager': {'name': None},
            'Python version management': {'name': None},
            'Apache 2': {'name': None},
            'Php 7.2 (Con extensiones importantes)': {'name': None},
            'MySQL': {'name': None, 'checked': True},
        }
    }
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
            'choices': dict_to_choices(APPLICATIONS['UTILES']),
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
            'choices': dict_to_choices(APPLICATIONS['COMPRESION']),
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
            'choices': dict_to_choices(APPLICATIONS['BROWSERS']),
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
            'choices': dict_to_choices(APPLICATIONS['DEVELOPER']),
            'when': lambda answers: answers['develop']
        }
    ]

    def run(self):
        # Titulo
        subprocess.call('clear')
        f = Figlet(font='slant')
        print(f.renderText('by: elib0'))

        print(
            emoji.emojize(
    """
    :question: Scrip para personalizar Linux Mint 19.2,
    también deberia funcionar correctamebnte con los deribados de Ubuntu 18.04    
    """, use_aliases=True
            )
        )

        print(
            emoji.emojize(
    """
    :exclamation: ADVERTENCIA: este script descarga gran parte de los paquetes de sus paginas oficiales,
    por en consecuencia no se garantiza que esten actualizados al dia; Sin embargo los paquetes
    agregan sus repositorios oficiales PPA por lo tanto mediante un simple \'apt upgrade\' se actualizaran.   
    """, use_aliases=True
            )
        )

        # Menu
        answers = prompt(self.questions, style=style3)
        pprint(answers)

# Inicio del CLi
Main().run()