from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import bs4
import typing


testing_dict = {}


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


def testing_link(link_app):
    driver = webdriver.Chrome()
    link = 'http://pyplanet.herokuapp.com/'
    driver.get(link)
    driver.find_element_by_link_text(link_app).click()
    title_text = driver.find_element_by_tag_name('th').text
    testing_dict['title_text'] = title_text
    link_table = driver.find_elements_by_tag_name('tr')
    td_elements = [driver.find_elements_by_tag_name('td')
                   for elem in link_table]
    testing_dict['len_table'] = len(td_elements) - 1
    driver.close()


def return_dict():
    return testing_dict


if __name__ == '__main__':
    site = pull_site('https://pyplanet.herokuapp.com/')
    header, navbar, link = firstpage(site)
    testing_link(link)
    print(return_dict())
