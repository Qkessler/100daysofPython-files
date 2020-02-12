

dict_byte = {1: 'bob', 2: 'julian', 3: 'tim'}
set_byte = {2, 3}


def remove_set_from_dict():
    new_dict = {}
    for number in dict_byte.keys():
        if number not in set_byte:
            new_dict[number] = dict_byte[number]
    return new_dict


print(remove_set_from_dict())
