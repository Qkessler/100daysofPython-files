from functools import wraps


def base_datos_UM(function):
    @wraps(function)
    def wrapper():
        # antes
        diccionario = {"Universidad": "UMU"}
        nombre, edad, location = function()
        diccionario["Nombre"] = nombre
        diccionario["Edad"] = edad
        diccionario["Location"] = location
        return diccionario
    return wrapper

@base_datos_UM
def get_datos():
    nombre = input("- ¿Cómo te llamas? \n")
    edad = input("- ¿Cuándo naciste? \n")
    location = input("- ¿Dónde vives? \n")
    return nombre, edad, location

diccionario = get_datos()
print([diccionario[key] for key in diccionario.keys() if key == "Nombre" or key == "Edad"])
