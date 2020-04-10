from flask import Flask, request, render_template
import os
import requests
from typing import Dict
from collections import namedtuple

BOOKS_KEY = os.environ['BOOKS_KEY']
API_LINK = '&key=' + BOOKS_KEY
BASE_LINK = 'https://www.googleapis.com/books/v1/volumes?q='
Book = namedtuple('Book', 'A B C E F G')
app = Flask(__name__)


def get_data(term):
    books = []
    request = BASE_LINK + term + API_LINK
    data = requests.get(request)
    json_data = data.json()
    items = json_data['items']
    for info in items:
        volume_info = info['volumeInfo']
        book = create_book(volume_info)
        books.append(book)
    return books


def create_book(volume_info: Dict):
    book = Book(A=volume_info['title'], B=volume_info['authors'],
                C=volume_info['language'],
                E=volume_info['pageCount'], F=volume_info['printType'],
                G=volume_info['publishedDate'])
    return book


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        term = request.form['term']
        books = get_data(term)
        return render_template('search.html', term=term, books=books)


if __name__ == '__main__':
    app.run()
