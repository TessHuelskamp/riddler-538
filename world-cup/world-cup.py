!usr/bin/python3

"""
Calculate the number of possible different endings there are for the group stage of the world cup.

4 teams each play each other once.
Wins are 3 points.
Losses are 0.
Ties are 1.
"""


from itertools import *

TEAMS="ABCD"
topTwo=True

# grab the order of the games
games=[x for x in combinations(TEAMS, 2)]

# generate all possible W/L/T outcomes for each game
outcomes=[x for x in product("wlt", repeat=len(games))]

# store unique results
allPossibleResults=set()

# calculate and store scores
for outcome in outcomes:

    # clear out entry
    scores=dict()
    for team in TEAMS: scores[team]=0

    # run the tourney
    for gameNo, result in enumerate(outcome):

        # "play" the game
        teamOne=games[gameNo][0]
        teamTwo=games[gameNo][1]

        if result=="w":
            scores[teamOne]+=3
        elif result=="l":
            scores[teamTwo]+=3
        elif result=="t":
            scores[teamOne]+=1
            scores[teamTwo]+=1
        else:
            raise Exception("unknown result")

    # the uniqueness of the tourney is *all* of the teams
    stringRep="-".join([x+str(scores[x]) for x in TEAMS])

    # store result
    allPossibleResults.add(stringRep)


print(len(allPossibleResults))

