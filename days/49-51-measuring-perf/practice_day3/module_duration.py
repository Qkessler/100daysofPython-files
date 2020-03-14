import re
from os import listdir
from os.path import isfile, isdir, join
import glob
import pathlib
from sys import argv
from datetime import timedelta
from tinytag import TinyTag

pat = re.compile(".+\.(mp3|mp4|m4a)")

def module_duration(list_argv):
    direcs = []
    files = []
    durations = []
    for direc in list_argv:
        if isdir(direc):
            direcs.append(direc)
    for d in direcs:
        files.clear()
        files = [f for f in listdir(d) if isfile(join(d, f))]
        music_files = [f for f in files if pat.search(f)]
        for m in music_files:
            joined = [d, m]
            tag = TinyTag.get("".join(joined))
            print(f'{d} - {m} : {tag.duration}')
            durations.append(timedelta(seconds=tag.duration))
    total = sum(durations, timedelta())
    return total


if __name__ == '__main__':
    list_argv = []
    for arg in argv:
        list_argv.append(arg)
    total = module_duration(list_argv)
    print('------------------------------')
    print(f'Total : {total}')
