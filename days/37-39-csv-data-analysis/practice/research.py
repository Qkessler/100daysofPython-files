import csv
from collections import namedtuple
import re
from re import match

name_file = 'constituents-financials_csv.csv'
headers = "Symbol,Name,Sector,Price,PE,DividendYield,EarningsPerShare,WeekLow,WeekHigh,MarketCap,EBITDA,PS,PB,SECFilings"
Company = namedtuple('Company', headers)
data = []

def init(name=name_file):
    with open(name_file, 'r') as f:
        reader = csv.DictReader(f)
        data.clear()
        for row in reader:
            data.append(company_maker(row))


def company_maker(row):
    pattern = re.compile(r'-*\d+.\d+')
    if pattern.match(row['Price']):
        row['Price'] = float(row['Price'])
    else:
        row['Price'] = int(row['Price'])
    if pattern.match(row['PE']):
        row['PE'] = float(row['PE'])
    elif row['PE'] == '':
        row['PE'] = 0.00
    else:
        row['PE'] = int(row['PE'])
    if pattern.match(row['DividendYield']):
        row['DividendYield'] = float(row['DividendYield'])
    else:
        row['DividendYield'] = int(row['DividendYield'])
    if pattern.match(row['EarningsPerShare']):
        row['EarningsPerShare'] = float(row['EarningsPerShare'])
    else:
        row['EarningsPerShare'] = int(row['EarningsPerShare'])
    if pattern.match(row['WeekLow']):
        row['WeekLow'] = float(row['WeekLow'])
    else:
        row['WeekLow'] = int(row['WeekLow'])
    if pattern.match(row['WeekHigh']):
        row['WeekHigh'] = float(row['WeekHigh'])
    else:
        row['WeekHigh'] = int(row['WeekHigh'])
    if pattern.match(row['MarketCap']):
        row['MarketCap'] = float(row['MarketCap'])
    else:
        row['MarketCap'] = int(row['MarketCap'])
    if pattern.match(row['EBITDA']):
        row['EBITDA'] = float(row['EBITDA'])
    else:
        row['EBITDA'] = int(row['EBITDA'])
    if pattern.match(row['PS']):
        row['PS'] = float(row['PS'])
    else:
        row['PS'] = int(row['PS'])
    if pattern.match(row['PB']):
        row['PB'] = float(row['PB'])
    elif row['PB'] == '':
        row['PB'] = 0.00
    else:
        row['PB'] = int(row['PB'])
            
    company = Company(
        **row
    )
    
    return company

