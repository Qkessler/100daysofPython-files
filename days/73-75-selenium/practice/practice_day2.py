import selenium
import requests
import bs4
import typing


def pull_site(URL):
    r = requests.get(URL)
    r.raise_for_status()
    return r


def firstpage(site: str):
    scraper = bs4.BeautifulSoup(site.text, 'html.parser')
    header = [header.string for header in scraper.h1]
    navbar = [login.string for login in scraper.find_all('a')][:2]
    link = scraper.main.a.text
    return header, navbar, link


if __name__ == '__main__':
    site = pull_site('https://pyplanet.herokuapp.com/')
    firstpage(site)
