from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve


User = namedtuple('User', 'name age role')
user1 = User(name='Quique', age=20, role='Coder')
print(user1.name + " has " + str(user1.age) + " years and is a " + user1.role)

# Supposing you are given a list of tuples --> challenges_done =
# [('mike', 10), ('julian', 7), ('bob', 5), ('mike', 11),
# ('julian', 8), ('bob', 6)]. Let's make a default dict.

challenges_done = [('mike', 10), ('julian', 7), ('bob', 5),
                   ('mike', 11), ('julian', 8), ('bob', 6)]
print(challenges_done)
challenges = defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenge)
print(challenges)

# Let's work now with a big text. We could either loop through
# so we can see which words are repeated the most. We have a better way.

words = """Lorem Ipsum is simply dummy text of the printing and
typesetting industry. Lorem Ipsum has been the industry's standard
dummy text ever since the 1500s, when an unknown printer
took a galley of type and scrambled it to make a type
specimen book. It has survived not only five centuries, but
also the leap into electronic typesetting, remaining essentially
unchanged. It was popularised in the 1960s with the release of Letraset
sheets containing Lorem Ipsum passages, and more recently with
desktop publishing software like Aldus PageMaker including versions
of Lorem Ipsum""".split()

print(Counter(words).most_common(6))

# Deques are lists a bit more efficient when inserting and deleting.
