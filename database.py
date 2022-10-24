import os
from termcolor import colored

username = os.getlogin()
title = colored(f'\n\t\t Welcome to Word To PDF converter {username}!\n', 'green', attrs=[])
print(title)

GUI = '''
[1] Convert files in your current working directory
[2] Search for files in default path (your Documents folder)
[3] Enter your desired path
[4] Exit
'''
