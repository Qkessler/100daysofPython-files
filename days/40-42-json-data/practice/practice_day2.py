import json
import requests
from pprint import pprint
import re


API_key = 'e359a9fac7b8b71403adda4610d336c3c7707873'
URL = 'https://public-api.quickfs.net/v1/data/EPD/cf_cfo?api_key='
URL_basic = 'https://public-api.quickfs.net/v1/data/'
METRICS = ' https://public-api.quickfs.net/v1/metrics'
BATCH_URL = ' https://public-api.quickfs.net/v1/data/batch?api_key=e359a9fac7b8b71403adda4610d336c3c7707873'
# companies = ' https://public-api.quickfs.net/v1/companies&api_key=e359a9fac7b8b71403adda4610d336c3c7707873'
URL_withAPI = URL + API_key
# r = requests.get(METRICS)
r = requests.get(URL_withAPI)
data = json.loads(r.text)

# pattern = re.compile('operating.*')

def get_cashflow_metrics():
    r = requests.get(METRICS)
    data = json.loads(r.text)
    metrics = []
    for metric in data['data']:
        if metric['statement_type'] == 'cash_flow_statement':
            pprint(metric)
    return metrics


# for metric in data['data']:
#     if metric['statement_type'] == 'cash_flow_statement':
#     # if pattern.match(metric['metric']):
#         pprint(metric)

# pprint(len(data['data'][9:19]))

# TODO: try to get 10 cap data out of API, and get a list of the companies.

# Json batch test.
test_batch = {
  "data": {
    "roa" : {
      "Coca-Cola Co" : "QFS(KO:US,roa,FY-2:FY)",
      "PepsiCo" : "QFS(PEP:US,roa,FY-2:FY)"
     },
    "roic" : {
      "Coca-Cola Co" : "QFS(KO:US,roic,FY-2:FY)",
      "PepsiCo" : "QFS(PEP:US,roic,FY-2:FY)"
     }
  }
}


def get_10_cap_data(company):
    # URL_10cap = ' https://public-api.quickfs.net/v1/data/'+ company +'/capex&cf_cfo?api_key=e359a9fac7b8b71403adda4610d336c3c7707873'

    # TRYING TO GET BATCH REQUEST WORKING.
    r = requests.post(BATCH_URL, data=test_batch)
    # r = requests.get(URL_10cap)
    data = json.loads(r.text)
    return data


if __name__ == '__main__':
    # with open('metrics_file.txt', 'w') as f:
    #     f.write(str(get_metrics()))
    # get_cashflow_metrics()
    pprint(test_batch)
    print(get_10_cap_data('EPD'))

    exit(0)
