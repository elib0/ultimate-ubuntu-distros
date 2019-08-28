# noinspection PyUnresolvedReferences
from prompt_toolkit.validation import Validator, ValidationError

from .prompt import prompt

# import the shortcuts to create single question prompts
from .prompts.checkbox import checkbox
from .prompts.confirm import confirm