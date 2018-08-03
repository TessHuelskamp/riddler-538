import random
def coinToss(): return "HEAD" if random.randint(0,1) else "TAIL"

NUM_TOSSES=10000
NUM_GAMES=1000

def playGame():
    tossNo=0
    headsInARow=0
    totalTails=0

    while tossNo < NUM_TOSSES:
        tossNo+=1

        result=coinToss()

        if result == "TAIL":
            # Tail resets progress
            totalTails+=1
            headsInARow=0
        else:
            headsInARow+=1

        if headsInARow > totalTails: return True

    return False

wins=0
for _ in range(NUM_GAMES):
    if playGame():
        wins+=1

print("Percentage: ", wins/float(NUM_GAMES))
