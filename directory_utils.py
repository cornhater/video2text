from parameters import *

import os


def remove(filename: str) -> None:
    '''removes file from current directory'''
    os.system(f'rm {filename}')


def clear_workspace(func) -> None:
    '''decorator, cleaning workspace while main function working'''
    def wrapper():
        for file in [PARSED_TEXT, PARSED_SPEECH]:
            if file in os.listdir(os.getcwd()):
                remove(file)
        func()
        remove(PARSED_SPEECH)
    return wrapper