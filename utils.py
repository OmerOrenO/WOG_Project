import os
import platform

SCORES_FILE_NAME = os.path.join(os.getcwd(),'scores.txt')
BAD_RETURN_CODE = -1

def screen_cleaner():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

