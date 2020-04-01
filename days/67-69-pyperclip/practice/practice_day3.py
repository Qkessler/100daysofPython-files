import pyperclip
from typing import Dict
import json


# Today I'm gonna try to build a rough password vault.
# The steps that come to mind are the following:
# DONE: Create a data base (will use a json file to simplify).
# DONE: Get the link where the user is at the moment
# (The link that has copied).
# DONE: Get the password back from the file.

def return_password():
    link = pyperclip.paste()
    link = link.strip('\n')
    with open('vault.json', 'r') as f:
        vault = f.read()
        json_file = json.loads(vault)
        data = json_file['data']
        for l in data:
            if link == l:
                pyperclip.copy(data.get(l))


def get_data(file_data='data.txt') -> Dict:
    info_dict = {}
    with open(file_data, 'r') as f:
        # Lines here will be "link password"
        for line in f.readlines():
            info = line.split()
            info_dict[info[0]] = info[1]
    create_json(info_dict)


def create_json(info: Dict):
    data = {}
    data["data"] = info
    with open("vault.json", "w+") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    dict_info = get_data()
    return_password()
