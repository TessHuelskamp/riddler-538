
"""
Smallest number of coins to make change for 1-99 cents

Assuming that this is smallest for any transaction max (num coins for each number 1 through 99) not the average (which assumes each number 1 through 99 is equally likely).

Max is 4 coins.

We need to have a penny (1 cent coin) because we need to be able to make change for a penny. That limits the thing we need to check.

Then we have 99c3 choices to try (100**3 which isn't bad)

Then from that we need to calculate the number of coins to make things work (I have script for this somewhere I need to plug in)

Then we're done
thanks
Writing this here since online python IDEs suck
"""
from itertools import combinations
from copy import copy

MAX_AMOUNT=99
ALL_AMOUNTS={c for c in range(1, MAX_AMOUNT+1)}
MINT_SIZE=4

def mintsGen():
#hard coding penny in to save time
  penny=1
  for mint in combinations(ALL_AMOUNTS^{penny}, MINT_SIZE-1):
    mint=set(mint) #:)
    mint.add(penny)
    yield mint

def checkmint(mint):
# /Dynamic Programming/
# 
# walk through how to do this
# Recursion starting with 99
# we start all of the changes we can make with only one coin
# Then, we calculate the changes we can make with two coins. To do this we take all of the changes we could make with 1 coin and see the coins you can make by adding each coin from the mint with that coin.
# we don't record anything we've seen before 
# From the purses we can make with 2 coins we then make all the amounts we can make with 3 coins and so on
# were done when we've made change for each amount  we need to make (we see 1-99)
# I didn't choose to store how many coins each amount makes but you could add that j formation in. 

  Seen = set()
  Round=0
  PrevRound=set()
  CurentRound=set()

  while ALL_AMOUNTS - Seen:
    Round+=1

    PrevRound=copy(currentRound)
    CurrentRound.clear()

    if Round==1:
#load in mint
      for coin in mint:
        Seen.add(coin)
        CurrentRound.add(coin)
      continue

#product??
    for amount in PrevRound:
      for coin in mint:
        CurChange = amount + coin:
        if CurChange > MAX_AMOUNT or CurChange in Seen: continue
        
        CurrentRound.add(CurChange)

    assert not CurrentRound.empty()

  return Round

BestMint=None
SmallestCoin=None

for mint in mintsGen():
  cur=checkmint(mint)

  if not SmallestCoin or cur < smallestCoin:
    BestMint = mint
    SmallestCoin = cur

print(BestMint)
print(SmallestCoin)
