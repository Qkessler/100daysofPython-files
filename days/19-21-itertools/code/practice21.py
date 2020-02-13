import itertools
from itertools import combinations, cycle, product

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]


def get_attendees():
    # listZIP = zip(names, locations, confirmed)
    # list_comb = product(listZIP)
    # for participant in list_comb:
    #     print(participant)
    # Voy a intentar a hacerlo de otra forma.
    trios = []
    for name in names:
        if len(locations) <= names.index(name):
            location = "-"
        else: 
            location = locations[names.index(name)]
        if len(confirmed) <= names.index(name):
            confirm = "-"
        else: confirm = confirmed[names.index(name)]
        trio = (name, location, confirm)
        trios.append(trio)
    return trios

if __name__ == '__main__':
    for participant in get_attendees():
        print(participant)