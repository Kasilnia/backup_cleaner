#!/usr/bin/python3

import os
import re

try:
    extension = input('Enter files extension, e.g. "gz": ')
    every_number = int(
        input('Remove every ... file (please, enter a number): '))
    last_number = int(
        input('Do not remove last ... files (please, enter a number): '))
    last_number = last_number * -1 if last_number else None
except:
    print ('Wrong input format. Please, try again.')
    quit()

files = os.listdir()
r = re.compile('^.+\.{}$'.format(extension))
matched_files = sorted([file for file in filter(r.match, files)])
remove_files = matched_files[every_number - 1:last_number:every_number]


for file in remove_files:
    os.remove(file)
