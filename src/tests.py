from questionary import prompt
from pprint import pprint

questions = [
    {
        'type': 'confirm',
        'message': 'Do you want to continue?',
        'name': 'test',
        'default': True
    },
    {
        'type': 'checkbox',
        'name': 'test',
        'message': 'Instala',
        'when': lambda answers: answers['test'],
        'choices': [
            {
                'name': 'Mozzarella',
                'checked': True
            },
            {
                'name': 'Cheddar',
                'checked': True
            },
            {
                'name': 'Parmesan'
            },
        ]
    }
]

answers = prompt(questions)
pprint(answers)