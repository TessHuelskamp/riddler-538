# Riddler - Fri May 10 12:54:15 PDT 2019

[link](https://fivethirtyeight.com/features/can-the-riddler-bros-beat-joe-dimaggios-hitting-streak/)

Given a batting average of X and Y number of games, how likely is it that a player will break a 56 game hitting streak over thier career?

# Key points:

* An at bat is either a hit or an out (no walks, balls, etc.)
* 4 at bats per game
* 160 games a season
* .200, .250, .300, .350, and .400 all have 20 seasons.
    * .500 has 10 seasons
* Streaks can span multiple seasons

# Explanation
Instead of doing math, 😇, I wrote some [code](./hitting-streak.js) (usage: `node hitting-streak.js`) to simulate players batting through their careers.

| Also, decided to learn javascript this weekend so no guarentees on this being Good Code :)

# Results

Looks like the player with the batting average of `.200` will break Joe DiMaggio's streak 96 percent of the time.
Everyone else will break his streak 100 percent of the time

## Raw results

```
0.1 will beat the streak with 3200 games 0 percent of the time
0.125 will beat the streak with 3200 games 0 percent of the time
0.15 will beat the streak with 3200 games 4 percent of the time
0.175 will beat the streak with 3200 games 50 percent of the time
0.2 will beat the streak with 3200 games 96 percent of the time
0.25 will beat the streak with 3200 games 100 percent of the time
0.3 will beat the streak with 3200 games 100 percent of the time
0.35 will beat the streak with 3200 games 100 percent of the time
0.4 will beat the streak with 3200 games 100 percent of the time
0.5 will beat the streak with 1600 games 100 percent of the time
```
