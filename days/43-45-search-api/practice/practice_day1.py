import requests
import json
from pprint import pprint
import re

# For the next days I'll be working with the Santander API, which also makes sense, as I will be using it for my personal project.

# The API's name is Accounts v2. I couldn't log in on day 1, so I will keep working on quickfs API.

# def pre_step():
#     url = 

key_with_api = 'api_key=e359a9fac7b8b71403adda4610d336c3c7707873'
API_key = 'e359a9fac7b8b71403adda4610d336c3c7707873'
URL = 'https://public-api.quickfs.net/v1/data/EPD/cf_cfo?api_key='
URL_basic = 'https://public-api.quickfs.net/v1/data/'
METRICS = ' https://public-api.quickfs.net/v1/metrics'
BATCH_URL = ' https://public-api.quickfs.net/v1/data/batch'
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
    "mkt_cap" : {
        "Coca-Cola Co" : "QFS(KO:US,mkt_cap,FY-2:FY)",
      "PepsiCo" : "QFS(PEP:US,mkt_cap,FY-2:FY)"
     },
    "roic" : {
      "Coca-Cola Co" : "QFS(KO:US,roic,FY-2:FY)",
      "PepsiCo" : "QFS(PEP:US,roic,FY-2:FY)"
     }
  }
}

def batch_with_marketcap(list_companies):
    companies_batch = {
        "data" : {
            "companies" : {
            }
        }
    }
    for company in list_companies:
        companies_batch["data"]["companies"].update( {company : "QFS(" + company + ",mkt_cap, FY-2:FY)"} )
    return companies_batch

header = {'x-qfs-api-key': API_key}

def get_list_companies():
    url_companies = 'https://public-api.quickfs.net/v1/companies/US?'
    comp_api = "".join([url_companies, key_with_api])
    print(comp_api)
    r = requests.get(comp_api)
    print(r.status_code, r.reason)
    data = r.json()
    i = 0
    list_companies = []
    for company in data['data']:
        list_companies.append(company)
    return list_companies

def get_10_cap_data(batch_request):
    r = requests.post(BATCH_URL, json=batch_request, headers=header)
    data = r.json()
    return data


if __name__ == '__main__':
    # with open('metrics_file.txt', 'w') as f:
    #     f.write(str(get_metrics()))
    # get_cashflow_metrics()
    # pprint(test_batch)
    
    # pprint(get_10_cap_data('EPD'))
    # companies_batch = {
    #     "data" : {
    #         "companies" : "Hola"
    #     }
    # }

    # print(companies_batch["data"]["companies"])
    
    list_companies = get_list_companies()
    # print(list_companies)
    # print(companies_with_marketcap(list_companies))
    comp = batch_with_marketcap(list_companies)
    print(get_10_cap_data(comp))

    exit(0)

