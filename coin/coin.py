from itertools import combinations
from copy import copy

MAX_AMOUNT=99
ALL_AMOUNTS={c for c in range(1, MAX_AMOUNT+1)}
MINT_SIZE=4

def mintsGen():
  # Each solution must have a penny in it. (otherwise it won't be able to make change for a penny)
  # This saves a little bit of computation time (99c4 v 98c3) and prevents us from having to check if a mint is valid
  penny=1
  for mint in combinations(ALL_AMOUNTS^{penny}, MINT_SIZE-1):
    mint=set(mint)
    mint.add(penny)
    yield mint

def checkmint(mint):
  # /Dynamic Programming/
  #
  # Start with all of the changes we can make with only one coin
  # Then, we calculate the changes we can make with two coins.
  #   To do this we take all of the changes we could make with 1 coin and create the changes you could make from adding another coin to that set.
  #   we don't record anything we've seen before
  # From the changes we've found with 2 coins, we then build the chagnes we can make with 3 coins...
  # ... Were done when we've made change for each amount we need to support (1-99)
  #
  # I didn't choose to store how many coins each amount takes and which combination of coins makes that change but you could add that information in.

  seen = set()
  Round=0
  prevRound=set()
  currentRound=set()

  # While we haven't created all of changes we need
  while ALL_AMOUNTS - seen:
    Round+=1

    prevRound=copy(currentRound)
    currentRound.clear()

    # If this is the first round, the only change we can make is the coins in our mint.
    if Round==1:
      for coin in mint:
        seen.add(coin)
        currentRound.add(coin)
      continue

    # All other rounds build from the previous round
    for change in prevRound:
      for coin in mint:

        currentChange = change + coin

        # Ignore changes higher than a dollar.
        # Ignore coins we've seen before
        if currentChange > MAX_AMOUNT or currentChange in seen: continue

        currentRound.add(currentChange)
        seen.add(currentChange)

    # if we haven't made new changes, something's wrong
    assert not len(currentRound) == 0

  return Round

bestMints=None
smallestNumberOfCoins=None

for mint in mintsGen():

  answer = checkmint(mint)

  if not smallestNumberOfCoins or answer < smallestNumberOfCoins:
    bestMints = [mint]
    smallestNumberOfCoins = answer
  elif answer == smallestNumberOfCoins:
    bestMints.append(mint)

print(smallestNumberOfCoins)
for mint in bestMints: print(mint)
