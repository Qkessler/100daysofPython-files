import itertools
import sys
import time


# Pruebo las funciones que hemos visto dentro del paquete de itertools: cycle,
# products, combinations, iterations.

ciclo = itertools.cycle('_\|/')
espacios = 0
while True:
    fin = ""
    imp_espacios = ""
    if espacios == 30:
        fin = "\n"
        espacios = 0
    for _ in range(espacios):
        imp_espacios += " "
    imprimir = '\r' + fin + imp_espacios + next(ciclo)
    sys.stdout.write(imprimir)
    time.sleep(0.1)
    espacios += 1
