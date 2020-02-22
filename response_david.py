from collections import defaultdict

string_default = "abba"

def first_repeated_letter(string=string_default):
    letter_dict = defaultdict()
    for letter in string:
        if letter not in letter_dict.keys():
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    for letter in letter_dict.keys():
        if letter_dict[letter] >= 1:
            return letter



if __name__ == '__main__':
    string = 'abab'
    print(first_repeated_letter(string))
