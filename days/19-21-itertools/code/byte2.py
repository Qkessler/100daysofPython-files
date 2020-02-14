import itertools

def friends_teams(friends, team_size=2, order_does_matter=False):
    if order_does_matter == True:
        return itertools.permutations(friends, r=team_size)
    else:
        return itertools.combinations(friends, r=team_size)

friends = "Mick Quique Juan imaili".split()
[print(friend) for friend in friends_teams(friends, 3, True)]

