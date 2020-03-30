import pyperclip
import re

# Tenemos varias funciones que vamos a usar:

# pyperclip.paste()
# pyperclip.copy(whatever : str)

# Let's try to get something going, I'm gonna try to get a script
# to everytime I try to copy a time, it converts it to AM - PM time.

# Tests:
# 12:02
# 21:03


def copy_time():
    # This controls if the copied item is a time.
    pat = re.compile(r'\d+:\d+')
    copied = pyperclip.paste()
    time = pat.findall(copied)
    if time:
        return time[0]
    else:
        return None


# The format from which I will be transalating is the 24hr time format
def translate_time(time):
    time_list = time.split(':')
    hours = int(time_list[0])
    minutes = time_list[1]
    if hours / 12 > 1:
        translated = f'{hours % 12}:{minutes} PM'
    else:
        translated = f'{hours}:{minutes} AM'
    return translated


if __name__ == '__main__':
    time = copy_time()
    if time:
        translated = translate_time(time)
        pyperclip.copy(translated)
    else:
        print(f'The string copied is not valid')
