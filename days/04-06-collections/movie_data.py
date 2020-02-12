from collections import defaultdict, namedtuple
from csv import DictReader
from urllib.request import urlretrieve

movie_data = 'https://raw.githubusercontent.com/pybites/challenges/'
movie_data += 'solutions/13/movie_metadata.csv'
movies_csv = 'movies.csv'
urlretrieve(movie_data, movies_csv)

# Aqui en vez de hacer un objeto Movie, hacemos una namedtuple.
Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(csvfile=movies_csv):
    directors = defaultdict(list)
    with open(csvfile) as f:
        for line in DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue
            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)
    return directors


directors = get_movies_by_director()
print(directors['Christopher Nolan'])
