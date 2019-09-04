#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import environ
from os.path import exists
from questionary import confirm, text

packages_file = 'Package Control.sublime-settings'
config_path = '/.config/sublime-text-3/Packages/User/'
config_file = ''
bashrc = '.bashrc' # or .zshrc
home_path = environ['HOME']

r = confirm('¿Deseas configurar Sublime Text 3?').ask()

if r:
    try:
        r = confirm('¿Quieres agregar un alias para abrir sublime desde la terminal? (Recomendado)').ask()

        if r:
            alias = text('cual sera el nombre del alias para sublime text 3(Por defecto: sublime):').ask() or 'sublime'

            if exists(home_path + '/' + '.zshrc'):
                bashrc = '.zshrc'

            f = open(home_path + '/' + bashrc, 'a')
            f.write('alias '+alias+'="/opt/sublime_text/sublime_text"\n')
            f.close()

        # Packages
        r = confirm('¿Desea instalar los packages mas populares? (Recomendado)').ask()
        if r:
            with open(home_path + config_path + packages_file, 'w+') as f:
                # TODO: corregir verificacion de carpeta si no crear rutas mas file
                lines = '{\n\t"bootstrapped": true,\n\t"in_process_packages":\n\t[\n\t],\n\t"installed_packages":\n\t[\n\t\t"A File Icon",\n\t\t"AdvancedNewFile",\n\t\t"Alignment",\n\t\t"Anaconda",\n\t\t"AutoFileName",\n\t\t"Autoprefixer",\n\t\t"Bootstrap 4 Snippets",\n\t\t"BracketHighlighter",\n\t\t"cdnjs",\n\t\t"Color Highlighter",\n\t\t"ColorPicker",\n\t\t"Djaneiro",\n\t\t"DocBlockr",\n\t\t"Emmet",\n\t\t"GitGutter",\n\t\t"Gitignore",\n\t\t"Google Spell Check",\n\t\t"HTML-CSS-JS Prettify",\n\t\t"HTML5",\n\t\t"HTMLAttributes",\n\t\t"Icon Fonts",\n\t\t"Icon Fonts (Legacy)",\n\t\t"JavaScript & NodeJS Snippets",\n\t\t"jQuery",\n\t\t"jQuery Snippets pack",\n\t\t"Laravel 5 Artisan",\n\t\t"Laravel 5 Snippets",\n\t\t"Laravel Blade Highlighter",\n\t\t"Laravel Blade Spacer",\n\t\t"LaravelCollective HTML Form Snippets",\n\t\t"Material Theme",\n\t\t"Modific",\n\t\t"Nodejs",\n\t\t"Package Control",\n\t\t"Pretty JSON",\n\t\t"Sass",\n\t\t"SideBarEnhancements",\n\t\t"Stylus",\n\t\t"Sublime Bookmarks",\n\t\t"SublimeCodeIntel",\n\t\t"SublimeGit",\n\t\t"SublimeLinter",\n\t\t"SublimeLinter-json",\n\t\t"SublimeLinter-pylint",\n\t\t"Sublimerge 3",\n\t\t"TabsExtra",\n\t\t"Terminal",\n\t\t"Text Pastry",\n\t\t"TrailingSpaces",\n\t\t"Vue Syntax Highlight",\n\t\t"Vuejs Snippets",\n\t\t"Vuetify"\n\t]\n}\n'
                # Escribimos configuración final...
                f.write(lines)
    except PermissionError:
        print('¡Error con los permisos del archivo:' + packages_file + '!')
    except FileNotFoundError:
        print('¡Error, el archivo no existe!')
