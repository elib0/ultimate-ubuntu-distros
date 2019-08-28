#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, json


class FileHandler:
    menu = {}
    defaults = {}
    SCRIPT_PATH = os.path.dirname(os.path.realpath(sys.argv[0]))

    def __init__(self, **kwargs):
        if 'menu_file' in kwargs:
            self.menu = self.open(kwargs['menu_file'])
        if 'default_file' in kwargs:
            self.defaults = self.open(kwargs['default_file'])

    def open(self, file_name):
        r = []
        try:
            #https://deibit.com/2011/04/04/la-sentencia-with-de-python/
            with open(self.SCRIPT_PATH + '/' + file_name, 'r') as f:
                r = json.load(f)
        except PermissionError:
            print('¡Error con los permisos del archivo:' + file_name + '!')
        except FileNotFoundError:
            print('¡Error, el archivo no existe!')
        return r

    def get_menu(self):
        return self.menu or None

    def get_pre_installations(self, to_string=False):
        if 'pres' in self.defaults:
            if to_string:
                return ' '.join(str(app) for app in self.defaults['pres'])
            else:
                return self.defaults['pres']
        return None

    def get_post_installations(self, to_string=False):
        if 'posts' in self.defaults:
            if to_string:
                return ' '.join(str(app) for app in self.defaults['posts'])
            else:
                return self.defaults['posts']
        return None
