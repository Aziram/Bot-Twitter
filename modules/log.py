from sys import stderr

__all__ = ["bold", "underline",
           "debug", "note",
           "info", "success",
           "error", "warn"]

colors = {
    'reset':     '\033[0m',
    'bold':      '\033[1m',
    'underline': '\033[4m',
    'black':     '\033[30m',
    'red':       '\033[31m',
    'green':     '\033[32m',
    'yellow':    '\033[33m',
    'blue':      '\033[34m',
    'magenta':   '\033[35m',
    'cyan':      '\033[36m',
    'white':     '\033[37m'
}

def bold(string):
    """Print text with bold."""
    if string:
        print('{reset}{bold}{text}{reset}'.format(
            reset=colors['reset'],
            bold=colors['bold'],
            text=string
        ))

def underline(string):
    """Print text with underline."""
    if string:
        print('{reset}{bold}{underline}{text}{reset}'.format(
            reset=colors['reset'],
            bold=colors['bold'],
            underline=colors['underline'],
            text=string
        ))

def debug(string):
    """Print debug text."""
    if string:
        print('{reset}{bold}{cyan}Debug:{reset} {white}{text}{reset}'.format(
            reset=colors['reset'],
            bold=colors['bold'],
            cyan=colors['cyan'],
            white=colors['white'],
            text=string
        ))

def note(string):
    """Print note text."""
    if string:
        print('{reset}{bold}{cyan}Note:{reset} {white}{text}{reset}'.format(
            reset=colors['reset'],
            bold=colors['bold'],
            cyan=colors['cyan'],
            white=colors['white'],
            text=string
        ))

def info(string):
    """Print info text."""
    if string:
        print('{reset}{bold}{white}\u279c{reset} {white}{text}{reset}'.format(
            reset=colors['reset'],
            bold=colors['bold'],
            white=colors['white'],
            text=string
        ))

def success(string):
    """Print success text."""
    if string:
        print('{reset}{bold}{white}[{green}+{white}]{reset} {white}{text}{reset}'.format(
            reset=colors['reset'],
            bold=colors['bold'],
            white=colors['white'],
            green=colors['green'],
            text=string
        ))

def error(string):
    """Print error text."""
    if string:
        print('{reset}{bold}{white}[{red}!{white}]{reset} {white}{text}{reset}'.format(
            reset=colors['reset'],
            bold=colors['bold'],
            white=colors['white'],
            red=colors['red'],
            text=string
        ), file=stderr)

def warn(string):
    """Print warn text."""
    if string:
        print('{reset}{bold}{white}[{yellow}?{white}]{reset} {white}{text}{reset}'.format(
            reset=colors['reset'],
            bold=colors['bold'],
            white=colors['white'],
            yellow=colors['yellow'],
            text=string
        ))
