import re
import requests
import bs4

def pull_site(URL):
    r = requests.get(URL)
    r.raise_for_status()
    return r

body = re.compile('body=[(.*?)]')

def get_data(site):
    scraper = bs4.BeautifulSoup(site.text, 'html.parser')
    data_id = scraper.select('.snapshot-td2-cp')
    data_values = scraper.select('.snapshot-td2')
    data = zip(data_id, data_values)
    info = {}
    for item in data:
        info[item[0].string] = item[1].string    
    return info

def main(stock):
    site = pull_site('https://finviz.com/quote.ashx?t='+stock)
    return get_data(site)

if __name__ == '__main__':
    print(main('TXRH'))
