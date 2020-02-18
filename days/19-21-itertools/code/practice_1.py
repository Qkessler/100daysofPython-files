import itertools
import sys
import time
import random


# Pruebo las funciones que hemos visto dentro del paquete de itertools: cycle,
# products, combinations, iterations.

# ciclo = itertools.cycle('\/')
espacios = 0
while True:
    fin = ""
    imp_espacios = ""
    if espacios == 80:
        fin = "\n"
        espacios = 0
    # for _ in range(espacios):
    #     imp_espacios += " "
    if random.randrange(2) == 0:
        symbol = '\\'
    else:
        symbol = '/'
    imprimir = fin + " " + symbol
    sys.stdout.flush()
    sys.stdout.write(imprimir)
    time.sleep(0.1)
    # espacios += 1
