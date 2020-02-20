import re

movies = '''1. Citizen Kane (1941)
2. The Godfather (1972)
3. Casablanca (1942)
4. Raging Bull (1980)
5. Singin' in the Rain (1952)
6. Gone with the Wind (1939)
7. Lawrence of Arabia (1962)
8. Schindler's List (1993)
9. Vertigo (1958)
10. The Wizard of Oz (1939)'''

pat = re.compile(r"^\d+\.\s+[A-za-z]+\s+[A-za-z']+\s+\(\d+\)$", re.VERBOSE)
for movie in movies.split('\n'):
    print(movie, pat.match(movie))
