#!/usr/bin/python

import random

NUM_TESTS=100
PAIRS=10

numToChr=lambda n : chr(ord("A")+n)

totalTime=0
for _ in range(NUM_TESTS):

    # build board
    board=set()
    for i in range(PAIRS):
        board.add(numToChr(i)+"0")
        board.add(numToChr(i)+"1")


    # play game
    time=0
    while board:

        # flip over two tiles and wait for cards to flip over/make animal noise
        # Happens in both success and failure
        time+=3

        first, second = random.sample(board, 2)

        # remove elements if they are a match
        if first[0] == second[0]:
            board.remove(first)
            board.remove(second)

    # could have kept a running total and divided at end but this make more sense to me
    totalTime+=time

# print avg
print(totalTime/float(NUM_TESTS))

