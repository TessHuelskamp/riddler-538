# ostomachion

Color this with 4 colors such that the area each color covers is equal.

![ostomachion](https://espnfivethirtyeight.files.wordpress.com/2018/01/ostomachion-svg.png)

# Explanation

Brute force wins again ¯\\_(ツ)_/¯

I encoded this ostomachion as a graph and then checked all possible colorings
(making sure that each color covered the correct amount of area an making sure
that no two of the same colors touched).

I named the puzzle piexes off of
[this](https://twitter.com/horrocksmatt/status/956938641909125125) tweet
(renaming the 14th piece to be piece 0) and I got the areas of the pieces from
[this](https://twitter.com/MauMondragon/status/957339170422345728) tweet. Thank
you both!!!

The search space was relatively small (`4^14=268435456`) and there was only a
quarter of a million different colorings to check. I was able to set this
program running while I made myself dinner and [`time`](time.out) reported that
it "only" took twenty minutes :) Adding in just one more piece to the puzzle
would result in around a billion colorings to check which is _just_ outside the
limit I'd be willing to let my laptop run. If a similar problem like that comes
up again I'll actually have to solve it :).

# Solution

It turns out that there are [120 different ways](solutions.txt) to color this
graph. That reduces down to [5 unique sets of pieces ](unique.txt) that can be
colored (those 5 sets of pieces can each be colored `4!` different ways).

I've tweeted the 5 configs [here](https://twitter.com/TessHuelskamp/status/957824917537357829).
