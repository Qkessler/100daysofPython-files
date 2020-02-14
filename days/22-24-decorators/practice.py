from functools import wraps
import time


def intime(function):
    @wraps(function)
    def wrapper(*arg, **kargs):
        """ Esto es la cantidad de código antes de la función """
        start = time.time()
        """ aquí ejecutamos la función. """
        valor = function()
        """ Aquí ejecutamos el código después de la función"""
        end = time.time()
        print('---- Final del timer: %d, valor= %d---'.format(int(end-start),
                                                              valor))


@intime
def function():
    print("Dentro de la función.")
    return 1


print(function())
