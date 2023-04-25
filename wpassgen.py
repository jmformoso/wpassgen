# -*- coding: utf-8
# v0.2.1
# by jtmeros

import sys
import os
import string
import random

especiales_general = '!@#$%&*-'
especiales_symfony = '%&-;[]'
caracteres = string.ascii_letters + string.digits + especiales_general
random.seed(os.urandom(1024))

longitud = 12
opcion = None

if len(sys.argv) >= 2:
    try:
        longitud = int(sys.argv[1])
        if len(sys.argv) >= 3:
            opcion = sys.argv[2]
    except ValueError:
        opcion = sys.argv[1]

if opcion:
    opciones = {
        "-l": string.ascii_letters,
        "-ll": string.ascii_lowercase,
        "-lL": string.ascii_uppercase,
        "-n": string.digits,
        "-s": especiales_general,
        "-p": string.punctuation,
        "-h": string.hexdigits,
        "-nl": string.digits + string.ascii_letters,
        "-ns": string.digits + especiales_general,
        "-ls": string.ascii_letters + especiales_general,
        "-sy": string.ascii_letters + string.digits + string.hexdigits + especiales_symfony
    }
    caracteres = opciones.get(opcion, caracteres)

print(''.join(random.choice(caracteres) for _ in range(longitud)))
