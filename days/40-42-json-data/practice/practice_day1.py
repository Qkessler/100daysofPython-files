import json
import requests
from pprint import pprint
import re


API_key = 'e359a9fac7b8b71403adda4610d336c3c7707873'
URL = 'https://public-api.quickfs.net/v1/data/EPD/cf_cfo?api_key='
METRICS = ' https://public-api.quickfs.net/v1/metrics'
# companies = ' https://public-api.quickfs.net/v1/companies&api_key=e359a9fac7b8b71403adda4610d336c3c7707873'
URL_withAPI = URL + API_key
r = requests.get(URL_withAPI)
# r = requests.get(METRICS)
data = json.loads(r.text)

# pattern = re.compile('operating.*')

# for metric in data['data']:
#     if metric['statement_type'] == 'cash_flow_statement':
#     # if pattern.match(metric['metric']):
#         pprint(metric)
pprint(len(data['data'][9:19]))


# print(URL_withAPI)
