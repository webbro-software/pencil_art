from .pencil_art import pencil_art

__all__ = ['pencil_art']

def __call__(*args, **kwargs):
    return pencil_art(*args, **kwargs)