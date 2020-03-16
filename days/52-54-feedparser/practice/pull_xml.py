import requests

def init(URL):
    r = requests.get(URL)
    print(r)
    with open('elpais.xml', 'w') as f:
        f.write(r.content)


if __name__ == '__main___':
    URL = 'https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/portada'
    init(URL)
