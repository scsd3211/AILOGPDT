#!/usr/bin/python
# Filename:dtree.py
# TODO: * exception handling: display the number of errors encountered
# * more user arguments
# * support path that ends with '/'

import os
import stat
import sys

PREF = ' '
DELM = '|'
DELM2 = '----'


def dtree(prefix, path):
    files = os.listdir(path)
    errors = 0
    suffix = ' '
    for f in files:
        try:
            mode = os.stat(path + '/' + f)[stat.ST_MODE]
            if stat.S_ISLNK(mode):
                suffix = '(->)'
            if stat.S_ISDIR(mode):  # process directories
                print
                prefix + DELM + DELM2 + '+' + f + suffix
                errors = errors + dtree(prefix + DELM + PREF, path + '/' + f)
            else:  # process files
                print
                prefix + DELM + DELM2 + f + suffix
        except OSError:
            errors = errors + 1
    return errors


# program entry

argPath = ''
if len(sys.argv) < 2:
    argPath = os.getcwd()
else:
    argPath = sys.argv[1]
    if argPath == '.':
        argPath = os.getcwd()

print('Path:' + argPath)
errors = dtree('', argPath)
print
print(str(errors) + ' error(s) ingonored')