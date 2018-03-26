"""
Calculate the number of possible different endings there are for the group stage of the world cup.

4 teams each play each other once.
Wins are 3 points.
Losses are 0.
Ties are 1.
"""

from itertools import *

TEAMS="ABCD"

# generate order of  matches
# AB, AC, AD, BC, BD, CD
matches=[ x for x in combinations(TEAMS, 2)]

# generate all possible W/L/T outcomes for each match
# wwwwww, wwwwwl, wwwwwwt, wwwwlw, .....
outcomes=[x for x in product("wlt", repeat=len(matches))]

# store unique results
allPossibleResults=set()

# calculate and store scores
for outcome in outcomes:

    # clear out scores for this instance of a tourney
    scores=dict()
    for team in TEAMS: scores[team]=0

    # run the tourney
    for gameNo, result in enumerate(outcome):

        # "play" the game
        teamOne=matches[gameNo][0]
        teamTwo=matches[gameNo][1]

        if result=="w":
            scores[teamOne]+=3
        elif result=="l":
            scores[teamTwo]+=3
        elif result=="t":
            scores[teamOne]+=1
            scores[teamTwo]+=1
        else:
            raise Exception("unknown result")

    # The uniqueness of the tourney is *all* of the teams
    # See justification in readme for this choice.
    # I looked into _just_ picking the top two things but didn't want to deal
    # with that
    stringRep="-".join([team+str(scores[team]) for team in TEAMS])

    # store result
    allPossibleResults.add(stringRep)


# Display all unique tourney results if you really want to.
if False: for result in allPossibleResults: print(result)

# Print number of unique tourney results
print(len(allPossibleResults))

