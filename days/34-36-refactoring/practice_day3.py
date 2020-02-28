

familia = 'Mamá Papá David Quique'.split()
for i, persona in enumerate(familia, 1):
    print(f'Miembro {i}: {persona}')

'''
La salida por consola es la siguiente:

Miembro 1: Mamá
Miembro 2: Papá
Miembro 3: David
Miembro 4: Quique
'''

# Para tener cuidado con los ficheros cuando los abres para cerrarlos con
# cuidado de posibles excepciones.

with open('practice.py', 'w') as f:
    f.write("Lo que sea")

# Lo bueno es que with lo cierra automáticamente.

