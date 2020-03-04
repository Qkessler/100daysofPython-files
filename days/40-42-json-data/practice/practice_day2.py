import json
import requests
from pprint import pprint
import re


API_key = 'e359a9fac7b8b71403adda4610d336c3c7707873'
URL = 'https://public-api.quickfs.net/v1/data/EPD/cf_cfo?api_key='
URL_basic = 'https://public-api.quickfs.net/v1/data/'
METRICS = ' https://public-api.quickfs.net/v1/metrics'
# companies = ' https://public-api.quickfs.net/v1/companies&api_key=e359a9fac7b8b71403adda4610d336c3c7707873'
URL_withAPI = URL + API_key
# r = requests.get(METRICS)
r = requests.get(URL_withAPI)
data = json.loads(r.text)

def get_metrics():
    r = requests.get(METRICS)
    data = json.loads(r.text)
    return data


# pattern = re.compile('operating.*')

# for metric in data['data']:
#     if metric['statement_type'] == 'cash_flow_statement':
#     # if pattern.match(metric['metric']):
#         pprint(metric)

    pprint(len(data['data'][9:19]))

# TODO: try to get 10 cap data out of API, and get a list of the companies.

# def get_10_cap_data(data, API_key):
#     URL_10cap = 
#     URL_request = URL_basic


if __name__ == '__main__':
    with open('metrics_file.txt', 'w') as f:
        f.write(str(get_metrics()))
    exit(0)
    print(get_10_cap_data())
