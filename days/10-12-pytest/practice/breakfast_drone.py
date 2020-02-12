#
# [1, 3, 4, 5, 6, 1, 4, 5, 6] -> 3
#


def stolen_drone(int_list):
    dict_values = {}
    for i in int_list:
        if i not in dict_values:
            dict_values[i] = 1
        else:
            dict_values[i] += 1
    for v in dict_values:
        if dict_values[v] == 1:
            return v


int_list = [1, 3, 4, 5, 6, 1, 4, 5, 6]
print stolen_drone(int_list)
