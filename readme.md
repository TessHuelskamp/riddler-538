# Darts Riddler for 538

What is the number of different ways you could throw a "perfect" game of darts?

The number of throws I originally picked to be the minimum number needed to win
a perfect game was incorrect (I thought it would take 11 throws (assuming that
50 was the highest number of points you could score on a turn) and a perfect
game is actually 9 throws).

Even though I didn't get the correct answer in on time (at the time of
submission, my code was "correct" but with the wrong parameters _shrug_), I had
fun working on this problem and might turn this repo into a collection of 538
riddler attempts.

# Assumptions

I decided to double, triple, or quadruple count some ways to score points as
"different" ways to take a turn. For example, there's 4 different ways to score
a 6. You could hit either of the single 6's (the wedge near the bullseye and the
wedge near the edge), you could hit the double 3 wedge, or you could hit the
triple 2 edge.

I messed around with collapsing all of these different ways to score and it
didn't affect the answer. I'm assuming that the perfect game just happens to
only use spaces that occur once on the board.

# How I did this

When I was pressed for time (I forgot to account that midnight EST is 10pm
here), I just coded up a recursive solution that lazily stored answers in a
cache (without the cache, I couldn't compute the answer). Later, I built up the
answer from the ground up using dynamic programming which was a fun exercise.
