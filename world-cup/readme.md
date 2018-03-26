# World cup from Mar 23

Prompt:

> In the World Cup’s group stage, each group of four teams plays a round robin,
> with every team playing the other teams once each. A win is worth 3 points, a
> draw 1 point, and a loss 0 points. The points are tallied, and the top two
> teams in each group advance to the knockout stage. For a given group — let’s
> pick Group A, which includes Russia, Saudi Arabia, Egypt and Uruguay — how
> many different final standings, including point totals, are possible for the
> group stage?

# Breaking things down

* Each team plays each other team once (6 games in total).
* Each game can have one of 3 outcomes:
  1. Team 0 wins (3 points to team 0).
  1. Team 1 wins (3 points to team 1).
  1. The teams tie (1 point to each team).
* So, there are only `3**6 (729)` different possibilities (which isn't too high
  of a number to brute force.)
* To get all of the point totals I wrote a program in python that'll calculate
  that.
  * Per usual, I decided to name teams Russia, Saudi Arabia, Egypt, and Uruguay
    teams A, B, C, and D :).
  * Usage (assuming you have python3 installed): `python3 world-cup.py`
* And if you count the scores of _all_ the teams affecting the uniqueness of a
  game, you end up with *556* unique tournament outcomes.
  * > I did try running this by defining uniqueness as _just_ the scores of the
    top two teams but ran into a few cases where teams tied for second place. I
    decided not to deal with this case.
    * > For example, lets say all the teams tie each other. Then each would
      have scores at the end of the tourney of 3 (A3-B3-C3-D3) and I'm not sure
      how the organizers would handle that.
    * > Also, you could have team A win out. And then you could have teams B and C _both_
      beat team D and then tie each other for a final tourney result of A9-B4-C4-D0.
      In this case, it's not clear how we would resolve this.
