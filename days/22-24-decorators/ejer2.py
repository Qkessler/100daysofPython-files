from functools import wraps

# Queremos una función que imprima por pantalla la función llamada
# con los parámetros llamados y el retorno.

def logged(function):
    @wraps(function)
    def wrapper(*args, **kargs):
        string = "Se ha llamado a la función %s" % (function.__name__)
        if len(args) > 0:
            string += str(args)
        string += " "
        if len(kargs) > 0:
            string += str(kargs)
        print(string)
        return_value = function(*args, **kargs)
        print("Devuelve " + str(return_value))
        return return_value
    return wrapper

@logged
def func(*args, **kargs):
    valor = 3 + len(args)
    return valor

valor = func(4, 4, 4, hola="hola")
print(valor)
