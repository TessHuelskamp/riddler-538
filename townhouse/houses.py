#!/usr/bin/python

# 538 Riddler Express

# Given a row of N houses, they're ordered randomly from 1 to N 

# For each interval (delta of 2 years), the following houses fall
# House i (where i is #interval)
# All houses next to a house that is already fallen

# What is the average time it takes the entire street to fall?

from random import shuffle
from copy import copy

from math import log10, floor
width = lambda x : int(floor(log10(x))+1)

from os import getenv
getint = lambda x, y : int(getenv(x,y))

# global configuration variables
NUM_TESTS=getint("NUM_TESTS", 1000)
NUM_HOUSES=getint("NUM_HOUSES", 36)
YEARS=getint("YEARS", 2)

# hacked booleans out of ints
SILENT=False if getint("SILENT", 1)==0 else True
STATS=False if getint("STATS", 1)==0 else True
SPECIAL=False if getint("SPECIAL", 0)==0 else True

# "enum"
DESTROYED="X"

class street:
    N=36
    houses=list()
    stringWidth=-1
    intervals=-1

    def __init__(self, num, specific=None):
        self.N=num
        self.stringWidth=width(num)

        if specific == None:
            self._buildStreet()
        else:
            self.houses=copy(specific)


    def _buildStreet(self):
        self.houses=[i+1 for i in range(self.N)]
        shuffle(self.houses)

    def __repr__(self):
        result="N: "+str(self.N)+"\n"
        result+=self.__str__()
        result+="\n"
        return result

    def __str__(self):
        return",".join([self._padString(x) for x in self.houses])

    def _destroyed(self):
        return all([house == DESTROYED for house in self.houses])

    def howManyIntervals(self):
        if self.intervals==-1: self._runSimulation()
        return self.intervals

    def _runSimulation(self):
        i=0
        if not SILENT: print self._padString(i),":", self
        while not self._destroyed():
            i+=1
            self._runOneRound(i)
            if not SILENT: print self._padString(i),":", self
        self.intervals=i

    def _runOneRound(self, roundNo):
        indiciesToDestroy=set()

        #gather houses near fallen houses
        for idx, house in enumerate(self.houses):

            # Check if it's this house's round to die
            if house==roundNo:
                indiciesToDestroy.add(idx)

            # check left. Only add *new* instances
            if idx-1 >= 0 and self.houses[idx]!=DESTROYED and self.houses[idx-1]==DESTROYED:
                indiciesToDestroy.add(idx)

            # check right. Only add *new* instances
            if idx+1 < len(self.houses) and self.houses[idx]!=DESTROYED and self.houses[idx+1]==DESTROYED:
                indiciesToDestroy.add(idx)

        # each round, one or more houses should fall, if not, something's wrong
        assert len(indiciesToDestroy) > 0

        # destroy all of the houses for this round
        for idx in indiciesToDestroy: self.houses[idx]=DESTROYED

    def _padString(self, x):
        if x==DESTROYED: return DESTROYED*self.stringWidth
        else: return format(x, "0"+str(self.stringWidth))


#[numIntervals]:#occurances
results=dict()

for _ in range(NUM_TESTS):
    test=street(NUM_HOUSES)
    result=test.howManyIntervals()

    if result not in results: results[result]=0

    results[result]+=1

if STATS:
    # print out "histogram"
    # This does help visualize results

    # sort on result
    data=[ (x,y) for x,y in results.items() ]
    sorted(data, key=lambda point: point[0])

    print "time to fall, occurances"
    for point in data:
        print point[0]*YEARS,",", point[1]

if STATS:
    average=sum([ result*occurances*YEARS for result, occurances in results.items() ])/float(NUM_TESTS)
    print "average", average

if SPECIAL:
    SILENT=False

    print "best case"
    bestCase=street(36,[i+1 for i in range(36)])
    bestCase.howManyIntervals()

    print "worst case"
    worstCaseList=[36, 35, 34, 33, 32, 1, 31, 30, 29, 28, 27, 26, 25, 24, 23, 2, 22, 21, 20, 19, 18, 17, 16, 3, 15, 14, 13, 12, 11, 4, 10, 9, 8, 5, 7, 6]
    worstCase=street(36, worstCaseList)
    worstCase.howManyIntervals()
