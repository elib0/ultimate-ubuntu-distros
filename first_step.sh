#!/usr/bin/env python
# -*- coding: utf-8 -*-


import subprocess, sys, os


class FirstStep:

  path = os.path.dirname(os.path.realpath(sys.argv[0]))  # Path to script

  def run(self):
    print(self.path)

# Inicio del script
FirstStep().run()
