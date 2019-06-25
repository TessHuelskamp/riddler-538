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

# Edit

Turns out that my "issue" with this problem was that I didn't know how baseball worked.


Updated my code to match real life, and got something close to the answer:

## Raw results
```
0.2 will beat the streak with 3200 games 0 percent of the time
0.25 will beat the streak with 3200 games 0 percent of the time
0.3 will beat the streak with 3200 games 0.01 percent of the time
0.35 will beat the streak with 3200 games 0.58 percent of the time
0.4 will beat the streak with 3200 games 10.35 percent of the time
0.5 will beat the streak with 1600 games 90.84 percent of the time
```

