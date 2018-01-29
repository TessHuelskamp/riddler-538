#!/usr/bin/python3

#using the sizes provided from this tweet: https://twitter.com/MauMondragon/status/957339170422345728
# and the numbers from this one: https://twitter.com/horrocksmatt/status/956938641909125125
# number 14 is number 0 here.


# brute force-able since with 14 spots and 4 colors there are only 38416 possible colorings (most of which are invalid)


class myNode():
    def __init__(self):
        self.size=0
        self.neighbors=set()

    def setNeighbors(self, n): self.neighbors=n
    def setSize(self, s): self.size=s


class Graph():
    nodes=dict()

    #coloring is a list of colors.
    #index in list is the color(0,1,2,3) that node would be assigned
    def validColoring(self, coloring):

        #check to see if the sizes are all equal (they should all be six)
        sizeSums=[0,0,0,0]

        for node, color in enumerate(coloring):
            sizeSums[color]+=self.nodes[node].size

        for result in sizeSums:
            if result!=36: False


        #now check to make sure that no two nodes have the same neighbor
        for node, color in enumerate(coloring):
            for neighbor in self.nodes[node].neighbors:
                if color == coloring[neighbor]: return False

        return True


# set up puzzle
puzzle=Graph()

neighbors=[[1, {2,5}], [2, {1,3,4,5,6}], [3, {4,6,2}], [4, {3,2,6}], [5, {1,2,7}], [6, {4,8,7,2}], [7, {6,5,9}],
        [8, {6,9,10}], [9, {7,8,12,11}], [10, {8,12}], [11, {9,0}], [12, {10,9,13}], [13, {12,0}], [0, {13,11}]]

for entry in neighbors:
    newNode=myNode()
    newNode.setNeighbors(entry[1])
    puzzle.nodes[entry[0]]=newNode

sizes=[[1,12],[2,12], [3,6], [4,3], [5,12], [6,21], [7,6], [8,6], [9,12], [10,12], [11,24] , [12,6], [13, 9], [0, 3]]

for entry in sizes:
    puzzle.nodes[entry[0]].setSize(entry[1])


blue=0
red=1
yellow=2
green=3

validColoring=[green, blue, yellow, blue, red, green, green, blue, blue, yellow, yellow, red, blue, red]
wrongSize=[green, blue, yellow, green, red, green, green, blue, blue, yellow, yellow, red, blue, red] #the sizes don't add up
invalidColoring=[green, blue, green, blue, red, green, green, blue, blue, yellow, yellow, red, blue, red] #colors are touching


assert puzzle.validColoring(validColoring)
assert not puzzle.validColoring(wrongSize)
assert not puzzle.validColoring(invalidColoring)


