#!/usr/bin/env python
# -*- coding: utf-8 -*-

from colors import *  # ANSI colors
from subprocess import call
from os.path import exists
from os import environ
from questionary import confirm, text

r = confirm('¿Deseas instalar Yarn? (Muy Recomendado)').ask()

if r:
  call('curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -', shell=True)
  call('echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list', shell=True)
  call('sudo apt-get update && sudo apt-get install --no-install-recommends yarn', shell=True)

  r = confirm('¿Quieres instalar: cordova, stylus, less, sass, vue-cli, typescript?').ask()
  if r:
    call('yarn global add cordova stylus less sass @vue/cli typescript', shell=True)
