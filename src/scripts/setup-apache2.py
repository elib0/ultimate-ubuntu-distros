#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import environ
from os.path import exists
from questionary import confirm, text
from subprocess import call

config_file = 'apache2.conf'
config_path = '/etc/apache2/'
home_path = environ['HOME']

r = confirm('¿Deseas configurar Apache 2?').ask()

if r:
    try:
        r = confirm('¿Quieres cambiar el directorio www de /var/www/html a otra carpeta?').ask()

        if r:
            alias = text('cual sera la nueva ruta de la carpeta (Por defecto' + home_path + '/www/):').ask() or home_path + '/www'

            if exists(config_path + config_file):
                f = open(config_path + config_file, 'w+')
                lines = f.read()
                lines = lines.replace('<Directory /var/www/>', '<Directory ' + home_path + '/www/')
                f.write(lines)
                f.close()

                f = open('/etc/apache2/sites-available/000-default.conf', 'w+')
                lines = f.read()
                lines = lines.replace('DocumentRoot /var/www/html', 'DocumentRoot ' + home_path + '/www')
                f.write(lines)
                f.close()

                call('sudo systemctl restart apache2.service', shell=True)
    except PermissionError:
        print('¡Error con los permisos del archivo:' + config_file + '!')
    except FileNotFoundError:
        print('¡Error, el archivo no existe!')
