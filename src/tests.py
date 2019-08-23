import json
import os
import sys
from pprint import pprint

def dict_to_choices(dict):
    choices = []
    for (key, value) in dict.items():
        checked = False
        if 'checked' in value:
            checked = value['checked']
        choices.append({'name': key, 'checked': checked})

    return choices


def build_menu(applications):
    menu = []
    for (cat, m) in applications.items():
        if 'programs' not in m:
            menu.append({'type': 'confirm', 'name': cat, 'message': m['message1']})
        else:
            menu.append(
                {
                    'type': 'checkbox',
                    'name': cat,
                    'message': m['message2'],
                    'choices': dict_to_choices(m['programs']),
                    'when': lambda answers: answers[cat]
                }
            )

    return menu

path = os.path.dirname(os.path.realpath(sys.argv[0]))

name = 'menu.json'
f = open(f"{path}/{name}", 'r')

APPLICATIONS = json.load(f)

menu = build_menu(APPLICATIONS)
