import selenium
import requests
import bs4
import pytest
import typing


def pull_site(URL):
    r = requests.get(URL)
    r.raise_for_status()
    return r


def test_firstpage(site: str):
    scraper = bs4.BeautifulSoup(site.text, 'html.parser')
    print(scraper.find_all('h1'))
    


if __name__ == '__main__':
    site = pull_site('https://pyplanet.herokuapp.com/')
    test_firstpage()
