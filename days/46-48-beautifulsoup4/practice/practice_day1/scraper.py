import requests
import bs4

def pull_site(URL):
    r = requests.get(URL)
    r.raise_for_status()
    return r

def get_data(site):
    holdings = []
    scraper = bs4.BeautifulSoup(site.text, 'html.parser')
    data = scraper.select('.holding-code')
    for holding in data:
        holdings.append(holding.getText())
    for holding in holdings:
        print(holding)
    

if __name__ == '__main__':
    site = pull_site('https://portfolio.sharesight.com/portfolios/470306')
    get_data(site)
    
