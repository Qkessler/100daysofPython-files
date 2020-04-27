from openpyxl import load_workbook
import os
import requests
from typing import Dict
from collections import namedtuple
from pprint import pprint
from gooey import GooeyParser, Gooey

# I'm gonna try to get data from the APIs we have been working on and
# populate a spreadsheet with the data collected.
BOOKS_KEY = os.environ['BOOKS_KEY']
API_LINK = '&key=' + BOOKS_KEY
BASE_LINK = 'https://www.googleapis.com/books/v1/volumes?q='
WB = load_workbook('books.xlsx')
WS = WB['api']
Book = namedtuple('Book', 'A B C D E F G')


def get_params():
    parser = GooeyParser()
    parser.add_argument('search_term', help='The search term')
    args = parser.parse_args()
    return args.search_term


# I'm getting the basic volumes from the google Books API, based on a
# search term given by the user.
def get_data(term):
    request = BASE_LINK + get_params() + API_LINK
    data = requests.get(request)
    json_data = data.json()
    items = json_data['items']
    counter = 2
    for info in items:
        volume_info = info['volumeInfo']
        book = create_row(volume_info)
        insert_row(book, counter)
        counter += 1


def create_row(volume_info: Dict):
    book = Book(A=volume_info['title'], B=volume_info['authors'],
                C=volume_info['language'], D=volume_info['categories'],
                E=volume_info['pageCount'], F=volume_info['printType'],
                G=volume_info['publishedDate'])
    pprint(book)
    return book


def insert_row(book: Book, counter):
    WS['A'+str(counter)] = str(book.A)
    WS['B'+str(counter)] = str(book.B)
    WS['C'+str(counter)] = str(book.C)
    WS['D'+str(counter)] = str(book.D)
    WS['E'+str(counter)] = str(book.E)
    WS['F'+str(counter)] = str(book.F)
    WS['G'+str(counter)] = str(book.G)
    WB.save('books.xlsx')


@Gooey(program_name='Searching books',
       program_description='Search books on the google Books API')
def main():
    get_data('investing')


if __name__ == '__main__':
    main()
