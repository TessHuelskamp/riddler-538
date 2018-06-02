# Riddler from 06/01/2018
## Prompt 

> Consider four towns arranged to form the corners of a square, where each side is 10 miles long. You own a road-building company. The state has offered you $28 million to construct a road system linking all four towns in some way, and it costs you $1 million to build one mile of road. Can you turn a profit if you take the job?

> Extra credit: How does your business calculus change if there were five towns arranged as a pentagon? Six as a hexagon? Etc.?

## Assumptions/Transformation
4 points on a square 10 units apart. Want to connect all 4 points with less than 28 units of line.

# Thought process
## Thought 1 : The stapler
Build a normal square and the remove one of the edges to save distance. Unfortuneately, this doesn't work as the total length is 30 (`3*10`). Diagram below.

```
._.
| |
. .
```

## Thought 2 : The X
Connect the cities through the center point of the square (diagram below). This also doesn't work: `2*sqrt(2*10**2)=20*sqrt(2)~=20*1.414=28.279`
```
.  .
 \/
 /\
.  .
```

## Thought 3 : The TIE Fighter/Holden Hall
The X reminded me of TIE fighters which also reminded me of [Holden Hall](https://maps.msu.edu/interactive/index.php?location=RIRZ) at MSU. Thought it would be worth checking to see if something like that would work. Diagram below:
```
.      .
 \    /
xx----
 /    \
.      .
```

If we take `x` to be the distance from the side diagonals go left/right into the center line of the square (indicated on the diagram), then we can find a formula for the total length of the connecting lines. The middle line's length is `10-2x` and each of the 4 diagonals has a length of `sqrt(x**2+(10/2)**2)`. The length of the entire line is then `10-2x+4*sqrt(x**2+5**2)`.

To see if it's possible to have the entire line take less than 28 units, we want to find the minimum of this line. I haven't done this in a while, :), but here's the derivative of the length of the line given x:
1. `length(x)=10-2x+4*sqrt(x**2+5**2)`
1. `length(x)=10-2x+4*sqrt(x**2+25)`
1. `d/dx=-2+4*(1/2)(x**2+25)^(-1/2)*2x`
    * > I had to look up how to use the chain rule here :)
1. `d/dx=-2+4x/sqrt(x**2+25)`
1. To find the minimums of `length(x)`, find where the derivative is 0.
1. `0=-2+4x/sqrt(x**2+25)`
1. `2=4x/sqrt(x**2+25)`
1. `sqrt(x**2+25)=2x`
1. `x**2+25=4x**2`
1. `25=3x**2`
1. `25/3=x**2`
1. `x=+/-sqrt(25/3)`
1. `x=+/-2.886`
1. `x=+2.886`
    * > A negative x is nonsensical. I introduce that by squaring the equation a few steps ago. There's probably a correct way to solve for x without doing that but I haven't done math like this in a while :)
1.  Then plugging x back into `length(x)` we get:
    * `length(2.886)=10-2*2.886+4*sqrt(2.86**2+25)=27.26`
1. And this is less than 28 !
