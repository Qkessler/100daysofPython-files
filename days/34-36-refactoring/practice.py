


dic = {}
personas = 'Quique Elena David Lara'.split()
años = '20 19 16 12'.split()

dic = dict(zip(personas, años))

# La mejor forma de acceder evitando if -else es con un diccionario.

def get_edad(persona):
    return dic.get(persona)

persona = 'Quique'
print(f'{persona} tiene {get_edad(persona)} años')
