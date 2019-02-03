from random import shuffle


NUM_TESTS=1000

RED_DECK = [ 14, 14, 14, 14, 9, 9, 9, 9, 7, 7, 7, 7]
BLUE_DECK = [ 13, 13, 13, 13, 11, 11, 11, 11, 6, 6, 6, 6]
BLACK_DECK = [ 12, 12, 12, 12, 10, 10, 10, 10, 8, 8, 8, 8]

def play_game(deck0, deck1):
    # 0 if deck0 wins; 1 if deck1 wins
    # Could probably do something more "correct" with these types :)

    shuffle(deck0)
    shuffle(deck1)

    deck0Wins=0
    deck1Wins=0

    for i, deck0Card in enumerate(deck0):
        deck1Card = deck1[i]

        if deck0Card > deck1Card:
            deck0Wins+=1
        else:
            deck1Wins+=1

        if deck0Wins >= 5:
            return 0
        elif deck1Wins >= 5:
            return 1


    # someone should've won by now :)
    assert False

redAgainstBlueWins, redAgainstBlackWins, blueAgainstBlackWins = 0, 0, 0

for _ in range(NUM_TESTS):
    # if right side wins, it will return 1
    # 0 if the left side wins.
    # The += is a nice hack of how I stiched together a win :)

    redAgainstBlueWins += play_game(BLUE_DECK, RED_DECK)
    redAgainstBlackWins += play_game(BLACK_DECK, RED_DECK)
    blueAgainstBlackWins += play_game(BLACK_DECK, BLUE_DECK)

print("Red will beat blue ", redAgainstBlueWins/float(NUM_TESTS), " percent of the time")
print("Red will beat black ", redAgainstBlackWins/float(NUM_TESTS), " percent of the time")
print("Blue will beat black ", blueAgainstBlackWins/float(NUM_TESTS), " percent of the time")



