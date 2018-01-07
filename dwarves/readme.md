# Riddler Classic Dwarves problem 1/5/17

# Descrption

Problem description from the website:

> Each of the seven dwarfs sleeps in his own bed in a shared dormitory. Every
> night, they retire to bed one at a time, always in the same sequential order,
> with the youngest dwarf retiring first and the oldest retiring last. On a
> particular evening, the youngest dwarf is in a jolly mood. He decides not to
> go to his own bed but rather to choose one at random from among the other six
> beds. As each of the other dwarfs retires, he chooses his own bed if it is not
> occupied, and otherwise chooses another unoccupied bed at random.

From that we then need to find:
1. The probability that the oldest dwarf sleeps in his own bed?
1. The expected number of dwarfs who do not sleep in their own beds?

# Solution Explanation
> NB: Instead of listing dwarves from oldest to youngest in terms of numbers
> (0-6, e.g.), I decided to name the dwarfs A-G with A being the youngest and G
> being the oldest. This made the most sense to me and was easy to spot check
> that things were going well.

I started by trying to list all of the decsions the dwarves could make by hand.
That strategy worked well when dwarf A happened to choose bed G (for that round,
dwarves B-F would choose their own bed and dwarf G would be left with dwarf A's
bed), but didn't when the dwarves happened to make decisions that would affect
other swarves' decisions.

Instead, starting with the 6 choices dwarf A could make, I decided to code up
all of the possible choices the dwarves could make and the likelhood that they
would happen. So, dwarf A could make 6 choices at the beginning (beds B-G) and
each of those choices have a 1/6.0 chance in occuring. Then, when B goes to
choose a bed, if B's bed isn't taken, B will take his own bed. If it isn't
however, B has an additional 6 choices to make (beds A or C-G). The 6 choices B
could make each have a 1/36 (1/6 from the choice dwarf A made times 1/6 from the
choices B can make). I store those arrangements and the probability they happen
and then move onto placing dwarves C-G in each of the arragements from the
previous step.

At the end, I calcuate the results using how likely each of the arrangements are
and where each dwarf is placed in that particular arrangement.


# Results

We were trying to find:
1. The probability that the oldest dwarf sleeps in his own bed?
    * 0.416
1. The expected number of dwarfs who do not sleep in their own beds?
    * 2.858

Also here's the percentage that each dwarf is in their own bed:
* A 0
* B 0.833
* C 0.805
* D 0.766
* E 0.708
* F 0.611
* G 0.416
