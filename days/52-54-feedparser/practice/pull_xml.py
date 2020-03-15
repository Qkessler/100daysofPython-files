import requests

def init(URL):
    r = requests.get(URL)
    print(r)
    # printf(r.json())
    with open('newsfeed.xml', 'wb') as f:
        f.write(r.content)


if __name__ == '__main___':
    URL = 'https://www.wsj.com/sitemap.xml'
    init(URL)
