# I'm trying to practice a bit more of my collections. I'm gonna find a dataset
# and try to get some cool info out of it.
# I found a data set of the fifa20 players with all the information.

from collections import namedtuple, defaultdict
from csv import DictReader, DictWriter

campos = 'short_name age dob height_cm weight_kg'
Player = namedtuple('Player', campos)
players_csv = 'players_20.csv'

# def get_movies_by_director(csvfile=movies_csv):
#     directors = defaultdict(list)
#     with open(csvfile) as f:
#         for line in DictReader(f):
#             try:
#                 director = line['director_name']
#                 movie = line['movie_title'].replace('\xa0', '')
#                 year = int(line['title_year'])
#                 score = float(line['imdb_score'])
#             except ValueError:
#                 continue
#             m = Movie(title=movie, year=year, score=score)
#             directors[director].append(m)
#     return directors


def get_player_by_club(data=players_csv):
    clubs = defaultdict(list)
    with open(data) as f:
        for line in DictReader(f):
            try:
                club_name = line['club']
                player_name = line['short_name']
                age = line['age']
                birth = line['dob']
                height_cm = line['height_cm']
                weight_kg = line['weight_kg']
            except ValueError:
                continue
            p = Player(short_name=player_name, age=age, dob=birth,
                       height_cm=height_cm, weight_kg=weight_kg)
            clubs[club_name].append(p)
    return clubs

# Ahora tengo la opcion de buscar sobre los clubes, para encontrar
# los jugadores como yo quiera.


def filter_older_players(club):
    older_players = []
    for p in club:
        if int(p.age) > 30:
            older_players.append(p)
    return older_players


def players_bigger_than_me(club):
    bigger_players = []
    for p in club:
        if int(p.height_cm) > 188:
            bigger_players.append(p)
    return bigger_players


clubs = get_player_by_club()
bigger_players = defaultdict(list)
for c in clubs:
    players_bigger = players_bigger_than_me(clubs[c])
    bigger_players[c].append(len(players_bigger))

with open('players_bigger.csv', mode='w') as csv_file:
    fieldnames = ['club', 'number']
    writer = DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for data in bigger_players:
        writer.writerow(data)
