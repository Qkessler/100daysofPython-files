import api
from pprint import pprint
from collections import namedtuple


headers = 'imdb_code title director keywords'
headers += ' duration genres rating year imdb_score'
Movie = namedtuple('Movie', headers)


def define_movie(movie):
    return Movie(
        imdb_code=movie['imdb_code'],
        title=movie['title'],
        director=movie['director'],
        keywords=movie['keywords'],
        duration=int(movie['duration']),
        genres=movie['genres'],
        rating=movie['rating'],
        year=movie['year'],
        imdb_score=movie['imdb_score']
        )


if __name__ == '__main__':
    msc = api.MovieSearchClient()
    keyword = input('Which is the keyword you are searching for?\n')
    list_movies = msc.get_movies(keyword).json()
    movies = []
    for movie in list_movies['hits']:
        movies.append(define_movie(movie))
    pprint(f'{movies}')
