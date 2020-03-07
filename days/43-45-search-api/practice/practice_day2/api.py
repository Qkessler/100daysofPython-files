import requests
import json


def get_dictionaries(list_keywords):
    basic_url = ' https://search.talkpython.fm/api/search?q='
    for k in list_keywords:
        if k == list_keywords[-1]:
            basic_url += k
        else:
            basic_url += k + '-'
    r = requests.get(basic_url)
    r.raise_for_status()
    dicc = r.json()
    titles = []
    for key in dicc['results']:
        titles.append(key['title'])
    return titles
