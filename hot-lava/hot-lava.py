from copy import deepcopy

# Can we get to the 😊 in this maze?
# I essentially ran a depth first search from each point on the edge
# and found that there were 3 different ways to get to the 😊 of the maze

# Maze done by row, column:
# Surrounded maze with lava
# (also @ollie, can we start getting all of our puzzles in some sort of text format 😇?)

MAZE = (
  ( "X", "X", "X", "X", "X", "X", "X", "X", "X", "X" ),
  ( "X", "L", "U", "U", "?", "U", "L", "X", "L", "X" ),
  ( "X", "R", "L", "R", "L", "U", "😊","U", "U", "X" ),
  ( "X", "S", "L", "R", "L", "U", "L", "X", "R", "X" ),
  ( "X", "U", "R", "?", "R", "S", "L", "?", "R", "X" ),
  ( "X", "R", "U", "U", "R", "R", "R", "S", "L", "X" ),
  ( "X", "S", "?", "S", "L", "S", "S", "L", "R", "X" ),
  ( "X", "R", "L", "R", "?", "R", "L", "?", "L", "X" ),
  ( "X", "L", "R", "S", "R", "S", "L", "R", "L", "X" ),
  ( "X", "X", "X", "X", "X", "X", "X", "X", "X", "X" )
)

def lookup_maze(row, col): return MAZE[row][col]

# Places on board
# "enums" sorta
TURN_LEFT="L"
TURN_RIGHT="R"
DEAD="X"
STRAIGHT="S"
UTURN="U"
MAKE_ANY_MOVE="?"
WIN="😊"

# Directions we could have entered a square from
# (these are also "enums")
FROM_TOP=0
FROM_RIGHT=1
FROM_BOTTOM=2
FROM_LEFT=3

# map FROM enum to string
def from_dir_to_string(direction):
    if direction == FROM_TOP: return "top"
    elif direction == FROM_BOTTOM: return "bottom"
    elif direction == FROM_RIGHT: return "right"
    elif direction == FROM_LEFT: return "left"
    else: raise

# returns next move and direction
def uTurn (row, col, fromDirection):
    if fromDirection == FROM_TOP: return row-1, col, FROM_BOTTOM
    elif fromDirection == FROM_BOTTOM: return row+1, col, FROM_TOP
    elif fromDirection == FROM_LEFT: return row, col-1, FROM_RIGHT
    elif fromDirection == FROM_RIGHT: return row, col+1, FROM_LEFT
    else: raise "unkown from direction"

# returns next move and direction
def go_straight (row, col, fromDirection):
    if fromDirection == FROM_TOP: return row+1, col, FROM_TOP
    elif fromDirection == FROM_BOTTOM: return row-1, col, FROM_BOTTOM
    elif fromDirection == FROM_LEFT: return row, col+1, FROM_LEFT
    elif fromDirection == FROM_RIGHT: return row, col-1, FROM_RIGHT
    else: raise "unkown from direction"

# returns next move and direction
def turn_left (row, col, fromDirection):
    if fromDirection == FROM_TOP: return row, col+1, FROM_LEFT
    elif fromDirection == FROM_RIGHT: return row+1, col, FROM_TOP
    elif fromDirection == FROM_BOTTOM: return row, col-1, FROM_RIGHT
    elif fromDirection == FROM_LEFT: return row-1, col, FROM_BOTTOM
    else: raise "unkown from direction"

def turn_right (row, col, fromDirection):
    if fromDirection == FROM_TOP: return row, col-1, FROM_RIGHT
    elif fromDirection == FROM_RIGHT: return row-1, col, FROM_BOTTOM
    elif fromDirection == FROM_BOTTOM: return row, col+1, FROM_LEFT
    elif fromDirection == FROM_LEFT: return row+1, col, FROM_TOP
    else: raise "unkown from direction"

# returns list of moves
def makeAllMoves(row, col, direction):
    return (
            ( row-1, col, FROM_BOTTOM),
            ( row, col+1, FROM_LEFT),
            ( row+1, col, FROM_TOP),
            ( row, col-1, FROM_RIGHT)
            )

# set of visited squares with (row, column, from_direction)
# we don't want to visit a square twice _from the same direction_
seen=set()
winningMoves=[]

# previous_moves is a list of the moves someone took prior to getting to this square.
# This isn't the best way to store that information but it's not copying and pasting /too/ much information around :)
def visit(row, col, direction, previous_moves):

    seenKey=(row, col, direction)

    # There's a better way to keep track of this information...
    # ... this isn't production grade software so this will work :)
    previous_moves = deepcopy(previous_moves)
    previous_moves.append(seenKey)

    # short circuit if we've visited this space before (could be a loop)
    # otherwise note that we've been here
    if seenKey in seen: return
    else: seen.add(seenKey)

    currentLocation=lookup_maze(row, col)

    if currentLocation == DEAD:
        pass
    elif currentLocation == WIN:
        winningMoves.append(deepcopy(previous_moves))
    elif currentLocation == TURN_LEFT:
        nextRow, nextCol, nextDir = turn_left(row, col, direction)
        visit(nextRow, nextCol, nextDir, deepcopy(previous_moves))
    elif currentLocation == TURN_RIGHT:
        nextRow, nextCol, nextDir = turn_right(row, col, direction)
        visit(nextRow, nextCol, nextDir, deepcopy(previous_moves))
    elif currentLocation == STRAIGHT:
        nextRow, nextCol, nextDir = go_straight(row, col, direction)
        visit(nextRow, nextCol, nextDir, deepcopy(previous_moves))
    elif currentLocation == UTURN:
        nextRow, nextCol, nextDir = uTurn(row, col, direction)
        visit(nextRow, nextCol, nextDir, deepcopy(previous_moves))
    elif currentLocation == MAKE_ANY_MOVE:
        nextMoves=makeAllMoves(row, col, direction)

        for nextRow, nextCol, nextDir in nextMoves:
            visit(nextRow, nextCol, nextDir, deepcopy(previous_moves))

    else: raise "unexpected board"


def start_maze(row, column, direction):
    # For each search, clear out the "seen" entries.
    # It's possible that two paths could converge to the same ending
    seen.clear()
    visit(row, column, direction, [])

# start from each of the squares on the edge
for i in range(1, 8+1):
    start_maze(1, i, FROM_TOP)
    start_maze(i, 8, FROM_RIGHT)
    start_maze(8, i, FROM_BOTTOM)
    start_maze(i, 1, FROM_LEFT)


if len(winningMoves) == 0:
    print("no possible moves")
else:
    print("There are ", len(winningMoves), " possible paths")

    for path in winningMoves:
        print("You can start from (", path[0][0],",", path[0][1], ") and take ", len(path), " moves.")

    print("Here's the route of the shortest path:")
    print("row, column, maze value, enter from diection")
    for row, col, direction in min(winningMoves, key=len):
        print(row, col, lookup_maze(row, col), from_dir_to_string(direction))
