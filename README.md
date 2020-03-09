# 100daysofPython-files
These are the files that reflect my progress on the 100 days of python Course.

[08/03/20]: Today I finished the group of search api, getting pretty the results of the dictionaries with namedtuples and openning the url selected by the user.

```python
def get_searches(list_keywords: List[str]) -> List[Search]:
    basic_url = ' https://search.talkpython.fm/api/search?q='
    for k in list_keywords:
        if k == list_keywords[-1]:
            basic_url += k
        else:
            basic_url += k + '-'
    r = requests.get(basic_url)
    r.raise_for_status()
    dicc = r.json()
    searches = []
    for key in dicc['results']:
        s = Search(key['category'], key['id'],
                   key['url'], key['title'], key['description'])
        searches.append(s)
		return searches
```
