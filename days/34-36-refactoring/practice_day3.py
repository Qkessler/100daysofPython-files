
personas = 'Mamá Papá David Quique'
familia = personas.split()
años_str = '54,50,66,20'
años = años_str.split(',')
diccionario_familia = dict(zip(familia, años))
print(diccionario_familia)

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

'''
with open('practice.py', 'w') as f:
    f.write("Lo que sea")
'''

# Lo bueno es que with lo cierra automáticamente.

print(min(diccionario_familia, key=lambda x: x[1]))

# Concatenamos de forma más eficiente con la función de stdlib 'join'.

print(':'.join(familia))

'''
La salida es:

Mamá:Papá:David:Quique
'''
