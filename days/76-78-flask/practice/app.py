from flask import Flask, request, render_template
from data import trabajo
import os
import requests
from typing import Dict
from collections import namedtuple

BOOKS_KEY = os.environ['BOOKS_KEY']
API_LINK = '&key=' + BOOKS_KEY
BASE_LINK = 'https://www.googleapis.com/books/v1/volumes?q='
Book = namedtuple('Book', 'A B C D E F G')
app = Flask(__name__)
books = []
text = ""


def get_data(term):
    request = BASE_LINK + term + API_LINK
    data = requests.get(request)
    json_data = data.json()
    items = json_data['items']
    counter = 2
    for info in items:
        volume_info = info['volumeInfo']
        book = create_book(volume_info)
        books.append(book)
        counter += 1


def create_book(volume_info: Dict):
    book = Book(A=volume_info['title'], B=volume_info['authors'],
                C=volume_info['language'], D=volume_info['categories'],
                E=volume_info['pageCount'], F=volume_info['printType'],
                G=volume_info['publishedDate'])
    return book


@app.route('/')
def index():
    return render_template('index.html', trabajo=trabajo)


@app.route('/', methods=['POST'])
def input_box():
    text = request.form['u']
    return text

if __name__ == '__main__':
    get_data(text)
    app.run()
