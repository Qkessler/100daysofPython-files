from openpyxl import load_workbook
import os
import requests
from pprint import pprint

# I'm gonna try to get data from the APIs we have been working on and
# populate a spreadsheet with the data collected.
BOOKS_KEY = os.environ['BOOKS_KEY']
API_LINK = '&key=' + BOOKS_KEY
BASE_LINK = 'https://www.googleapis.com/books/v1/volumes?q='
WB = load_workbook('books.xlsx')
WS = WB['api']


# I'm getting the basic volumes from the google Books API, based on a
# search term given by the user.
def get_data(term):
    request = BASE_LINK + term + API_LINK
    data = requests.get(request)
    json_data = data.json()
    items = json_data['items']
    for i in items:
        pprint(i)
        break


if __name__ == '__main__':
    get_data('investing')
