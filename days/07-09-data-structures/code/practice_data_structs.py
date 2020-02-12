# This is the practice for day 7.

lista = ['Quique', 'Mickael', 'Cesar', 'Jose']

for nombre in lista:
    print('%s' % nombre)

Quique = list(lista[0])
for letter in Quique:
    print(letter)

Quique[0] = "d"
Quique.pop()
Quique.insert(0, 's')
Quique.append('s')
print(Quique)

nombres_con_edad = {'Quique': 20, 'Mickael': 20, 'Cesar': 20, 'Jose': 20}

for key, value in nombres_con_edad.items():
    if key == 'Quique':
        print("%s es el mejor companero de piso" % key)
