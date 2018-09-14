# RE on 09/14/2018

> Abby and Beatrix are playing a game with two six-sided dice. Rather than having numbers on the sides like normal dice, however, the sides of these dice are either red or blue. In the game they’re playing, Abby wins if the two dice land with the same color on top. Beatrix wins if the colors are not the same. One of the dice has five blue sides and one red side.

> If Abby and Beatrix have equal chances of winning the game, how many red and blue sides does the other die have?

# Notes
* `s/Blue/Green/`
    * > I don't want to have two B variables
* Variables:

    | Name | Abrv |
    | --- | --- |
    | Abby | A |
    | Beatrix | B |
    | Red | R |
    | Green (Blue) | G |

# Solution

Let's just enumerate everything.

## 1 Red 5 Green
```
X | R | G | G | G | G | G |
---------------------------
R | A | B | B | B | B | B |
---------------------------
G | B | A | A | A | A | A |
---------------------------
G | B | A | A | A | A | A |
---------------------------
G | B | A | A | A | A | A |
---------------------------
G | B | A | A | A | A | A |
---------------------------
G | B | A | A | A | A | A |
---------------------------
```

Nope.

## 2 Red 6 Green
```
X | R | G | G | G | G | G |
---------------------------
R | A | B | B | B | B | B |
---------------------------
R | A | B | B | B | B | B |
---------------------------
G | B | A | A | A | A | A |
---------------------------
G | B | A | A | A | A | A |
---------------------------
G | B | A | A | A | A | A |
---------------------------
G | B | A | A | A | A | A |
---------------------------
```

Nuh-uh.

## 3 Red 3 Green
```
X | R | G | G | G | G | G |
---------------------------
R | A | B | B | B | B | B |
---------------------------
R | A | B | B | B | B | B |
---------------------------
R | A | B | B | B | B | B |
---------------------------
G | B | A | A | A | A | A |
---------------------------
G | B | A | A | A | A | A |
---------------------------
G | B | A | A | A | A | A |
---------------------------
```

This looks symmetric here's the answer. I'm not going to bother with the other dice since we know this one works.
