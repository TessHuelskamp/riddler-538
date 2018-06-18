# Riddler 06/15/2018

> I have a matching game app for my 4-year-old daughter. There are 10 different pairs of cards, each pair depicting the same animal. That makes 20 cards total, all arrayed face down. The goal is to match all the pairs. When you flip two cards up, if they match, they stay up, decreasing the number of unmatched cards and rewarding you with the corresponding animal sound. If they don’t match, they both flip back down. (Essentially like Concentration.) However, my 1-year-old son also likes to play the game, exclusively for its animal sounds. He has no ability to match cards intentionally — it’s all random.

> If he flips a pair of cards every second and it takes another second for them to either flip back over or to make the “matching” sound, how long should my daughter expect to have to wait before he finishes the game and it’s her turn again?

# Thoughts

Average time it takes to get 10 pairs = average time it takes to get 1 pair with 10 remaining + average time it takes to get 1 pair with 9 pairs remaining + ...

# Figuring things out:

I didn't have as much time on this so I just built a simulation. On average, the game takes 300 seconds (5 minutes) to finish.
> To run this do `./concentration.py`
