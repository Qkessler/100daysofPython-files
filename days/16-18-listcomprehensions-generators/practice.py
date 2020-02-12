from collections import Counter
import calendar
import itertools
import random
import re
import string

import requests

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', ' brad pitt', 'matt damon', 'brad pitt']

NAMES_title = [name.title() for name in NAMES]
NAMES_swap = [name[::-1] for name in NAMES_title if NAMES_title.index(name) == 0 or NAMES_title.index(name) == (len(NAMES_title) - 1)]

def crear_pares():
    for _ in range(10):
        yield (NAMES_title[random.randrange(12)], NAMES_title[random.randrange(12)])

def crear_generador():
    for i in range(5):
        yield i


gen = crear_pares()
for _ in range(10):
    actual = next(gen)
    print("{} teams up with {}".format(actual[0], actual[1]))
