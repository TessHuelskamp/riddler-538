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
  1. Team A wins.
  1. Team B wins.
  1. The teams tie.
* So, there are only `3**6 (729)` different possibilities (which isn't too high
  of a number.
* To get all of the point totals I wrote a program in python that'll calculate
  that.
* And if you count the scores of _all_ the teams affecting the uniqueness of a
  game, you end up with 556 unique tournament outcomes.
  * > I did try running this by defining uniqueness as _just_ the scores of the
    top two teams but ran into a few cases where teams tied for second place. I
    decided not to deal with this case.
