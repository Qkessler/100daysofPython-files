
dic = {}
personas = 'Quique Elena David Lara'.split()
años = '20 19 16 12'.split()

dic = dict(zip(personas, años))

# La mejor forma de acceder evitando if -else es con un diccionario.


def get_edad(persona):
    return dic.get(persona)


persona = 'Quique'
print(f'{persona} tiene {get_edad(persona)} años')

# Para mejorar el counter, usamos los enumerates.

# El uno que ponemos detrás de personas es para indicar dónde empieza el index.
for i, persona in enumerate(personas, 1):
    print(f'Persona {i}: {persona}')

# Para manejar los contextos teníamos varias opciones: Una era usar try-except, pero daba error
# dejando por ejemplo el fichero abierto. Nos interesa usar with, que cierra automáticamente.

def funcion_yield(personas=personas):
    for persona in enumerate(personas, 1):
        yield i, persona


gen = funcion_yield()
for _ in range(1, 4, 1):
    j, actual = next(gen)
    print(f'Persona número {j}: {actual}')

# with open('practica.py', 'w') as fichero:
#     fichero.write('')
#     raise Exception

print(max(dic, key=lambda x: x[1]))
