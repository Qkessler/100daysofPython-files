import itertools
import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])

def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    # return [word for word in _get_permutations_draw(draw) if word in DICTIONARY]
    back = []
    for word in _get_permutations_draw(draw):
        if " ".join(word) in DICTIONARY:
            back.append(word)
    return back

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    perm = itertools.permutations(draw)
    return perm

# print([word for word in _get_permutations_draw("D, A, C, E, T, G".split(", "))])
print(get_possible_dict_words("D, A, C, E, T, G".split(", ")))