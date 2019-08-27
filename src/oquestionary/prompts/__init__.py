from . import confirm
from . import checkbox

AVAILABLE_PROMPTS = {
    "confirm": confirm.confirm,
    "checkbox": checkbox.checkbox
}


def prompt_by_name(name):
    return AVAILABLE_PROMPTS.get(name)
