
graph=dict()
allTeams=set()

# Decided to read csvs without the library since this is simple
with open("data.csv", "r") as f:
    for line in f:
        teamA, scoreA, teamB, scoreB = line.split(",")
        scoreA=int(scoreA)
        scoreB=int(scoreB)

        #create entries when we see new teams
        if teamA not in graph:
            graph[teamA]=list()
            allTeams.add(teamA)
        if teamB not in graph:
            graph[teamB]=list()
            allTeams.add(teamB)

        if scoreA > scoreB:
            # team A wins
            # if teamB happens to be a TNC then teamA will be
            # So, B "points to" A
            graph[teamB].append(teamA)
        else:
            graph[teamA].append(teamB)


# starting with Villanova do a search (This is neither DFS or BFS since we
# traverse the graph randomly with sets) to see who all can claim to be a
# Transitive National Champion

seen=set()
toVisit=set()

for team in graph["Villanova"]:
    toVisit.add(team)
    seen.add(team)

while toVisit:

    # grab a random entry from the teams we need to visit
    visiting=toVisit.pop()

    # for all of the teams that this team lost to, add them if we haven't seen them yet
    for team in graph[visiting]:
        if team not in seen:
            seen.add(team)
            toVisit.add(team)


#The transitive national champs are all of the teams we saw on our walk.
tncs=seen

# Only thing I care about :)
if "Michigan St" in tncs:
    print("Michigan State is a transitive national champion!")

# Not going to check on Michigan because, since we lost to them this year...
# twice, if we're a seen they are too :(

print("There are {} transitive national champions out of {} total teams ({} percent).".format(\
        len(tncs), len(allTeams), int(100*len(tncs)/float(len(allTeams)))))
print("{} teams weren't transitive national champions :(".format(len(allTeams)-len(tncs)))
