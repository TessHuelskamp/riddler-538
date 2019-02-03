# Maze

Is it possible to reach the center of this maze (below) using these rules:

> You move between boxes in a grid: up, down, left or right, but never diagonally.
> Your goal is to arrive in the finish square, designated here by a “☺.”
> Your movement is dictated by the symbol inside the square you have just moved to, and each direction is relative to where you’d be facing if you were physically walking the maze. “S” means you continue straight, “R” means you turn right, “L” means you turn left, “U” means you make a U-turn, and “?” gives you the option of any of those four directions.
> An “X” ends your game in failure — think hot lava. (But hey, you can always start over!)
> If you are forced to exit the maze’s grid, you lose — more hot lava.

![maze](https://fivethirtyeight.com/wp-content/uploads/2019/01/Screen-Shot-2019-01-31-at-3.56.04-PM.png?w=1150)

# Answer
Did a DFS search on the maze using python (usage: `python3 hot-lava.py`).

Found through my program that there are  3  possible paths starting from ( 2 , 1 ), ( 1 , 4 ), and ( 6 , 8 ).

After looking at each of the routes, I noticed that there are technically infinitely many paths :); e.g., you can start from square (1,4) and bounce between that and (1,3) as many times as you want before heading on into square (2,4) :)
