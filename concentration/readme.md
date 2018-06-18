# Riddler 06/15/2018

> I have a matching game app for my 4-year-old daughter. There are 10 different pairs of cards, each pair depicting the same animal. That makes 20 cards total, all arrayed face down. The goal is to match all the pairs. When you flip two cards up, if they match, they stay up, decreasing the number of unmatched cards and rewarding you with the corresponding animal sound. If they don’t match, they both flip back down. (Essentially like Concentration.) However, my 1-year-old son also likes to play the game, exclusively for its animal sounds. He has no ability to match cards intentionally — it’s all random.

> If he flips a pair of cards every second and it takes another second for them to either flip back over or to make the “matching” sound, how long should my daughter expect to have to wait before he finishes the game and it’s her turn again?

# Figuring things out:

I didn't have as much time on this so I just built a simulation. On average, the game takes 300 seconds (5 minutes) to finish.
> To run this do `./concentration.py`

# Hacking out the math

Average time it takes to get 10 pairs = average time it takes to get 1 pair with 10 remaining + average time it takes to get 1 pair with 9 pairs remaining + ...

> From here on out I'm going to ignore the factor of 3 present in the problem and just count each turn as 1 unit.

## Time it takes to get from 1 pair to no pairs

Time it takes to get 1 pair: 1 unit of time (no matter which tile you pick the other one you pick up will match)

## Time it takes to get from 2 pairs to 1 pair

Pick any tile. Now we have a 1 in 3 chance of getting its match. Expected time for this is `3` (?)

## Time it takes to get from 3 pairs to 2 pairs

Pick any tile. Now we have a 1 in 5 chance of getting its match. Expected time for this is `5` (?)

## Time it takes to get from n pairs to n-1 pairs

Pick any tile. Now we have a 1 in `(2*n)-1` chance of getting its match. Expected time for this is `2n-1` (?)

## Time it takes to get from 2 pairs to no pairs
3+1=4

## Time it takes to get from 3 pairs to no pairs
5+3+1=8

## Time it takes to get from 10 pairs to no pairs
19+17+15+13+11+9+7+5+3+1=100

## Time it takes to get from n pairs to no pairs
1. `2n-1 + 2(n-1)-1 + 2(n-2)-1... 2(n-n+3)-1 + 2(n-n+2)-1 + 2(n-n+1)-1`
1. `2n + 2(n-1) + 2(n-2)... 2(n-n+3) + 2(n-n+2) + 2(n-n+1)-n`
1. `2[n + (n-1) + (n-2)... (n-n+3) + (n-n+2) + (n-n+1)]-n`
1. _something happens_
    * > Sum of squares :)
1. `n**2`
