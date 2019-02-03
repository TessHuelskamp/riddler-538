# Problem
> You meet someone on a street corner who’s standing at a table on which there are three decks of playing cards. He tells you his name is “Three Deck Monte.” Knowing this will surely end well, you inspect the decks. Each deck contains 12 cards …

> Red Deck: four aces, four 9s, four 7s
> Blue Deck: four kings, four jacks, four 6s
> Black Deck: four queens, four 10s, four 8s

> The man offers you a bet: You pick one of the decks, he then picks a different one. You both shuffle your decks, and you compete in a short game similar to War. You each turn over cards one at a time, the one with a higher card wins that turn (aces are high), and the first to win five turns wins the bet. (There can’t be ties, as no deck contains any of the same cards as any other deck.)

# Solution
Simulated (`python three-decks.py`) 1000 games against each pairs of decks and got these stats:

```
('Red will beat blue ', 0.699, ' percent of the time')
('Red will beat black ', 0.281, ' percent of the time')
('Blue will beat black ', 0.713, ' percent of the time')
```

So (assuming Monte is playing to maximizes his chances of winning):
* If you pick the red deck, Monte will pick the black deck. You'll then have a ~30 percent chance of winning (2nd row).
* If you pick the blue deck, Monte will pick the red deck. He'll then beat you ~70 percent of the time. (1st row).
* If you pick the black deck, Monte will pick the blue deck. He'll then beat you ~70 percent of the time. (3rd row).

Essentially: Red beats blue, blue beats black, and black beats red (all ~70 percent of the time).

Doesn't sound like a game I'd play :shrug:
