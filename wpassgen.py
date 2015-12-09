# -*- coding: utf-8
# v0.1.0
# by jtmeros

import sys, os, string, random

caracteres = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))


if len(sys.argv) >= 2:
	longitud = int(sys.argv[1])

else:
	longitud = 10
	

print ''.join(random.choice(caracteres) for i in range(longitud))