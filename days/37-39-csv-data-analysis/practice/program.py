import research
import re
from re import match

def companies_under_50(data):
    return [company for company in data if company.Price <= 50]

def companies_div_over_4(data):
    return [company for company in data if company.DividendYield >= 4.00]

def companies_close_to_WeekLow(data):
    # Let's say close is a 10% over it or less.
    return [company for company in data if company.WeekLow >= 0.95*company.Price]


if __name__ == '__main__':
    research.init()    
    print('Companies under 50$:')
    print()
    for company in companies_under_50(research.data):
        print(f'{company.Symbol}: {company.Price}')
    print()
    print('Companies with div yield over 4:')
    print()
    for company in companies_div_over_4(research.data):
        print(f'{company.Symbol}: {company.DividendYield}')
    print()
    print(len(companies_close_to_WeekLow(research.data)))
    for company in companies_close_to_WeekLow(research.data):
        print(f'{company.Symbol}: {company.Price} - {company.WeekLow}')
    
