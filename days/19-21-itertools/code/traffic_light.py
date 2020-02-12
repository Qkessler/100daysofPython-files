import random
import itertools
import time
import sys


colors = 'green ambar red'.split()
ciclo = itertools.cycle(colors)


while True:
    sys.stdout.write('\r' + next(ciclo))
    sys.stdout.flush()
    time.sleep(random.randint(1, 3))
