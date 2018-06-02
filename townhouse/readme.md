# Riddle Express from 06/01/2018
> You live in a row house, one of 36 like it on your side of the block. A disaster strikes, and the city has to be evacuated. Two years later, with everyone gone for good, the worst-maintained row house on your side of the block, battered by the elements for too long, collapses. Within two years, any row house neighboring the collapsed one also collapses — as does the second-worst-maintained home on the block, if it wasn’t next to the worst-maintained one.

> This contagion continues: Every two years, any row house next to one that’s already collapsed also becomes rubble, and houses continue to collapse in order of how badly maintained they are — the third-worst-maintained house falls in the third round, the fourth-worst-maintained in the fourth round, and so on, assuming they were still standing at the start of that round. (The maintenance rankings are set at the moment the city is evacuated and don’t change from round to round.) Assuming a random distribution of poorly maintained homes, what’s the longest your home can remain standing? What’s the fewest number of years it will take for all 36 row houses to collapse?

> Extra credit: How does either answer change for N rowhouses?

## Interpretations
The houses fall like I've depicted A and not like B. That is, after we order the houses in terms of damage, the houses are predetermined to fall at a certain time point and are unaffected by their updated ranking. E.g., in step 2, house 4 doesn't fall (even though it is then the weakest house on the block).

```
A:
0: 2137654
1: 2X37654
2: XXX7654
3: XXXX654
4: XXXXX5X

B:
0  : 2137654
1  : 2X37654
2.1: XXX7654
2.2: XXX765X
```

# Specific cases
## Best case scenario
Given N=36, the longest at least one house will stay on the block is 36 iterations (72 years). The block would have to be completely ordered in terms of damage in order to eliminate any domino-ing of already fallen houses. I've illustrated how that would look below:
```
y0 : 1,2,3,... 35,36
y2 : x,2,3,... 35,36
y4 : x,x,3,... 35,36
y6 : x,x,x,... 35,36
...
y70 : x,x,x,... x,36
y72 : x,x,x,... x, x
```
There are 2 possible configurations where this will happen (the houses are ordered in ascending and in descending order). The probability of that happening is basically 0 `2/36!`

## Worst case scenario
Here, we want to maximize the damage that happens when the houses "domino" against each other. I.e., we want to spread out the badly damaged houses on the block and want to cluster the pristine houses next to the dilapidated ones. The houses in this scenario take 12 years to completely be destroyed.

One setup I made to illustrate this case is below
```
y0 : 36, 35, 34, 33, 32, 1, 31, 30, 29, 28, 27, 26, 25, 24, 23, 2, 22, 21, 20, 19, 18, 17, 16, 3, 15, 14, 13, 12, 11, 4, 10, 9, 8, 5, 7, 6
y2 : 36, 35, 34, 33, 32, x, 31, 30, 29, 28, 27, 26, 25, 24, 23, 2, 22, 21, 20, 19, 18, 17, 16, 3, 15, 14, 13, 12, 11, 4, 10, 9, 8, 5, 7, 6
y4 : 36, 35, 34, 33,  x, x,  x, 30, 29, 28, 27, 26, 25, 24, 23, x, 22, 21, 20, 19, 18, 17, 16, 3, 15, 14, 13, 12, 11, 4, 10, 9, 8, 5, 7, 6
y6 : 36, 35, 34,  x,  x, x,  x,  x, 29, 28, 27, 26, 25, 24,  x, x,  x, 21, 20, 19, 18, 17, 16, x, 15, 14, 13, 12, 11, 4, 10, 9, 8, 5, 7, 6
y8 : 36, 35,  x,  x,  x, x,  x,  x,  x, 28, 27, 26, 25,  x,  x, x,  x,  x, 20, 19, 18, 17,  x, x,  x, 14, 13, 12, 11, x, 10, 9, 8, 5, 7, 6
y10: 36,  x,  x,  x,  x, x,  x,  x,  x,  x, 27, 26,  x,  x,  x, x,  x,  x,  x, 19, 18,  x,  x, x,  x,  x, 13, 12,  x, x,  x, 9, 8, x, 7, 6
y12:  x,  x,  x,  x,  x, x,  x,  x,  x,  x,  x,  x,  x,  x,  x, x,  x,  x,  x,  x,  x,  x,  x, x,  x,  x,  x,  x,  x, x,  x, x, x, x, x, x
```

## Probability of this happening
Here we notice that the structure of the first 6 buildings to fall on their own (and not due to neighboring buildings falling) looks like this:
```
[5]1[5].[4]2[4].[3]3[3].[2]4[2].[1]5[1].6
```
We have 6 different groupings where the center block maximizes the number of building that will fall due to dominoing.

There are `6!` ways we can organize these blocks (an example's below). Since it doesn't matter where the 30 remaining house are placed (it doesn't matter if house 7 or house 36 is placed next to house 1), for each `6!` configuation of blocks there are `30!` ways to arrange the reamining blocks.

```
[4]2[4].[2]4[2].[3]3[3].[1]5[1].6.[5]1[5]
```

The odds of the worst case scenario happening are `30!*6!/36!`, which, though they're close to 0, they're not *as* close to 0 as the best case scenario.

## Formula finding the minimum number of iterations this takes
I noticed the following pattern

| i | sketches | better sketches | result |
|---| -------- | --------------- | ------ |
| `0` | `0` | `0` | `0` |
| `1` | `0 + 0 + 1` | `2*(i-1) + T(i-1) + 1` | `1` |
| `2` | `1*2 + 1 + 1` | `2*(i-1) + T(i-1) + 1` | `4` |
| `3` | `2*2 + 4 + 1` | `2*(i-1) + T(i-1) + 1` | `9` |
| `4` | `3*2 + 9 + 1` | `2*(i-1) + T(i-1) + 1` | `16` |
| `5` | `4*2 + 16 + 1` | `2*(i-1) + T(i-1) + 1` | `25` |
| `6` | `5*2 + 25 + 1` | `2*(i-1) + T(i-1) + 1` | `36` |

`<commentary on recurrence relation>`
`<min is bounded by the next sqrt>`

## Average case scenario
Didn't know how to calculate this so I wrote a program to do it for me :)

### Explanation

Brute force it is again :)

Ran a bunch of simulations and calculated, on average, how long it takes the entire street to fall. Average takes around 21 years.

### Usage

Assuming python is installed on your system, running this program should "just work".

To play with the output I've added the following integer enviornment variables that you can `export` into your shell to alter the behavior of your code:
* `NUM_TESTS` -- Number of tests to run. Default is reasonable. Set to `1` if you toggle `silent`
* `NUM_HOUSES` -- Number of houses on the block. Default is `36`
* `YEARS` -- How long is each iteration. For some reason this problem sets each iteration to be 2 years
* `SILENT` -- Print out each iteration of the test. `1` is silent; `0` is not silent.
    * > This is really only useful if `NUM_TESTS` is set to `1` :)
* `STATS` -- Calculate the average and spit out a "histogram". `1` is run stats; `0` is don't run stats.
* `SPECIAL` -- Runs after all averages are calculated. Displays the best and worse case scenario. Default is `0`. `1` runs these cases; `0` doesn't.
> If you mess with anything and want to return variables to their default value, I'd recommend running `unset VAR`.
