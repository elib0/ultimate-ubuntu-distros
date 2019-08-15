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
    APT_PREFIX = 'apt'
    COMMANDS_APT = {'upd': 'update', 'upg': 'upgrade', 'ins': 'install', 'rmv': 'remove'}
    UTILES_CHOICES = [
        Separator('UTILARIOS'),
        {'name': 'openshot'},
        {'name': 'plank', 'checked': True},
        {'name': 'ppa-purge', 'checked': True},
        {'name': 'shutter'},
        {'name': 'synapse', 'checked': True},
        {'name': 'dconf-tools', 'checked': True},
    ]
    COMPRESION_CHOCIES = [
        Separator('COMPRESION'),
        {'name': 'p7zip-rar', 'checked': True},
        {'name': 'p7zip-full', 'checked': True},
        {'name': 'unace', 'checked': True},
        {'name': 'unrar', 'checked': True},
        {'name': 'zip', 'checked': True},
        {'name': 'unzip', 'checked': True},
        {'name': 'sharutils', 'checked': True},
        {'name': 'rar', 'checked': True},
        {'name': 'uudeview', 'checked': True},
        {'name': 'mpack', 'checked': True},
        {'name': 'arj', 'checked': True},
        {'name': 'cabextract', 'checked': True},
        {'name': 'file-roller', 'checked': True},
    ]
    BROWSER_CHOICES = [
        Separator('Navegadores'),
        {'name': 'Google Chrome(Stable Channel)', 'checked': True},
        {'name': 'Opera Browser(Stable Channel)', 'checked': True},
        {'name': 'Vilvadi Browser(Stable Channel)'},
    ]
    DEVELOPER_CHOICES = [
        Separator('Desarrollo'),
        {'name': 'Visual Studio Code(Stable Channel)', 'checked': True},
        {'name': 'Sublime Text 3(Stable Channel)', 'checked': True},
        {'name': 'Node Version Manager'},
        {'name': 'Python version management'},
        {'name': 'Apache 2', 'checked': True},
        {'name': 'Php 7.2 (Con extensiones importantes)', 'checked': True},
        {'name': 'MySQL', 'checked': True},
    ]
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
            'choices': UTILES_CHOICES,
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
            'choices': COMPRESION_CHOCIES,
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
            'choices': BROWSER_CHOICES,
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
            'choices': DEVELOPER_CHOICES,
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
  :exclamation: ADVERTENCIA: este script descarga gran parte de los paquetes de sus paginas oficiales,
  por lo tanto no se garantiza que esten actualizados al dia; Sin embargo los paquetes
  agregan sus repositorios oficiales por lo tanto mediante un simple \'apt upgrade\' se actualizaran.   
  """, use_aliases=True
            )
        )

        # Menu
        answers = prompt(self.questions, style=style3)
        pprint(answers)

# Inicio del CLi
Main().run()