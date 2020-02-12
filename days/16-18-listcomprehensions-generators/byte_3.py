# This is the third byte, based on the linux terminal, using generators.

import os
from glob import glob

"""
Turn the following unix pipeline into Python code using generators

$ for i in ../*/*py; do grep ^import $i|sed 's/import //g' ; done | sort | uniq -c | sort -nr
   4 unittest
   4 sys
   3 re
   3 csv
   2 tweepy
   2 random
   2 os
   2 json
   2 itertools
   1 time
   1 datetime
"""

def gen_files(path):
    for name in glob(path):
        yield name
    
def gen_lines(files, pattern):
    for file_name in files:
        with open(file_name) as f:
            for line in gen_grep(f, pattern):
                if not line.strip():
                    continue
                else:
                    yield line

def gen_grep(lines, pattern):
    for line in lines: 
        if pattern in line:
            yield line

def gen_count(lines):
    dict_lines = {}
    for line in lines:
        if line not in dict_lines.keys():
            dict_lines[line] = 1
        else:
            dict_lines[line] += 1
        #return [yield {key:value} for key, value in dict_lines.items()]
    for key, value in dict_lines.items():
        yield key, value

if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files('../*/*py')
    lines = gen_lines(files, "import")
    number_lines = gen_count(lines)
    for line in number_lines:
        print("{} {}".format(line[0], line[1]))
