#!/usr/bin/python

from random import sample

NUM_TESTS=10000
PAIRS=10

numToChr=lambda n : chr(ord("A")+n)

# I intended to build a histogram here but ran out of time
allGames=list()

for _ in range(NUM_TESTS):

    # build board
    board=set()
    for i in range(PAIRS):
        board.add(numToChr(i)+"0")
        board.add(numToChr(i)+"1")

    # play game
    gameDuration=0
    while board:

        # flip over two tiles and wait for cards to flip over/make animal noise
        # Happens in success and failure
        gameDuration+=3

        # set.pop() returns an _aribitary_ element not a random one.
        # flip over two tiles
        first, second = sample(board, 2)

        # remove tiles if they are a match
        # (they are implictly "flipped over" if we do nothing).
        if first[0] == second[0]:
            board.remove(first)
            board.remove(second)

    # keep running total of all games
    allGames.append(gameDuration)

# pls don't divide by 0 :)
average = sum(allGames)/len(allGames)
print(average)
