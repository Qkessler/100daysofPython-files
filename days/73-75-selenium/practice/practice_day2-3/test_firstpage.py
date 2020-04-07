import pytest
from program import firstpage, pull_site


site = pull_site('https://pyplanet.herokuapp.com/')
header, navbar, link = firstpage(site)


def test_header():
    assert header[0] == 'PyBites 100 Days of Django'


def test_navbar():
    assert navbar == ['Login', 'Home']


def test_link():
    assert link == 'PyPlanet Article Sharer App'
