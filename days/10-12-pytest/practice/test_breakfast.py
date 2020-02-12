from breakfast_drone import stolen_drone

#
# [1, 3, 4, 5, 6, 1, 4, 5, 6] -> 3
#
# def stolen_drone(int_list):
#     dict_values = {}
#     for i in int_list:
#         if i not in dict_values:
#             dict_values[i] = 1
#         else:
#             dict_values[i] += 1
#     for v in dict_values:
#         if dict_values[v] == 1:
#             return v
# Este es el cod que voy a practicar usando pytest.

test_array = [1, 3, 4, 5, 6, 1, 4, 5, 6]


def test_breakfast_drone():
    expected = 3
    assert stolen_drone(test_array) == expected
    array = [1, 2, 1]
    expected = 2
    assert stolen_drone(array) == expected
