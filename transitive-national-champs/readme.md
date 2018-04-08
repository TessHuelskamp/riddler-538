# Prompt

> On Monday, Villanova won the NCAA men’s basketball national title. But I
> recently overheard some boisterous Butler fans calling themselves the
> “transitive national champions,” because Butler beat Villanova earlier in the
> season. Of course, other teams also beat Butler during the season and their
> fans could therefore make exactly the same claim.2

> How many transitive national champions were there this season? Or, maybe more
> descriptively, how many teams weren’t transitive national champions?

> (All of this season’s college basketball results are
> [here](https://www.masseyratings.com/scores.php?s=298892&sub=12801&all=1). To
> get you started, Villanova lost to Butler, St. John’s, Providence and
> Creighton this season, all of whom can claim a transitive title. But
> remember, teams beat those teams, too.)

# Cleaning up the data

1. I downloaded the data from the website using `curl`.
1. I manually removed the html form to get the data.
1. I used the following command to get the data in a more reasonable format :)
  * `cut -c13-36,37-39,42-65,66-68 --output-delimiter=, data.txt | sed "s/[ ]*,/,/g" | sed "s/,[ ]*/,/g" > data.csv`
  * > Found the fields through trial and error :)
  * > The sed commands remove the excess whitespace.

# Explanation

* To find all of the transitive national champions, we need to create a
  directed graph where the losers point to the winners for all of the games.
* Then, starting with Villanova, we do a search (either DFS or BFS works) to
  find all of the teams that can be reached from Villanova.
* Once that terminates, we have our set of transitive national champs!

# Results

Thankfully, Michigan State is a transitive national champion!

There are 1185 transitive national champions out of 1362 total teams (87 percent).

177 teams out of the set weren't transitive national champions :(
