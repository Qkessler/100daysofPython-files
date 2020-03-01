import research
import re
from re import match

def companies_under_50(data):
    return [company for company in data if company.Price <= 50]

def companies_div_over_4(data):
    return [company for company in data if company.DividendYield >= 4.00]


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
    
