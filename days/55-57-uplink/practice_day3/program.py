import api
from collections import namedtuple
from datetime import timedelta


headers = 'imdb_code title director keywords'
headers += ' duration genres rating year imdb_score'
Movie = namedtuple('Movie', headers)


def define_movie(movie):
    return Movie(
        imdb_code=movie['imdb_code'],
        title=movie['title'],
        director=movie['director'],
        keywords=movie['keywords'],
        duration=timedelta(minutes=movie['duration']),
        genres=movie['genres'],
        rating=movie['rating'],
        year=movie['year'],
        imdb_score=movie['imdb_score']
        )


if __name__ == '__main__':
    msc = api.MovieSearchClient()
    question = 'Would you like to search by '
    options = '[k]eyword, [d]irector or [c]ode?\n'
    letter = input(question + options)
    letter_names = {'k': 'keyword', 'd': 'director', 'c': 'code'}
    input_name = input(f'Ok! Enter the {letter_names.get(letter)}!\n')
    print('------------------')
    return_options = {'k': msc.get_movies(input_name),
                      'd': msc.get_movies_by_director(input_name),
                      'c': msc.get_movies_by_imdbcode(input_name)}
    list_movies = return_options.get(letter).json()
    movies = []
    for movie in list_movies['hits']:
        movies.append(define_movie(movie))
    print(f'How would you like to sort them?')
    letter = input(f'[d]uration, [t]itle or [s]core\n')
    # keys = {'d': lambda movie: movie.duration,
    #         't': lambda movie: movie.title,
    #         's': lambda movie: movie.imdb_score}
    # sorted(movies, key=keys.get(letter))
    if letter == 'd':
        sorted(movies, key=lambda movie: movie.duration)
    elif letter == 't':
        sorted(movies, key=lambda movie: movie.title)
    elif letter == 's':
        sorted(movies, key=lambda movie: movie.imdb_score)
    [print(f'{movie.duration} - {movie.title}:{movie.imdb_score}')
     for movie in movies]
