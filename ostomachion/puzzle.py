#!/usr/bin/python3

#using the sizes provided from this tweet: https://twitter.com/MauMondragon/status/957339170422345728
# and the numbers from this one: https://twitter.com/horrocksmatt/status/956938641909125125


# brute force-able since with 14 spots and 4 colors there are only 38416 possible colorings (most of which are invalid)


class myNode():
    def __init__(self):
        self.size=0
        self.neighbors=set()

    def setNeighbors(self, n): self.neighbors=n
    def setSize(self, s): self.size=s


class Graph():
    nodes=dict()

# set up puzzle
puzzle=Graph()

neighbors=[[1, {2,5}], [2, {1,3,4,5,6}], [3, {4,6,2}], [4, {3,2,6}], [5, {1,2,7}], [6, {4,8,7,2}], [7, {6,5,9}],
        [8, {6,9,10}], [9, {7,8,12,11}], [10, {8,12}], [11, {9,14}], [12, {10,9,13}], [13, {12,14}], [14, {13,11}]]

for entry in neighbors:
    newNode=myNode()
    newNode.setNeighbors(entry[1])
    puzzle.nodes[entry[0]]=newNode

sizes=[[1,12],[2,12], [3,4.5], [4,3], [5,12], [6,22.5], [7,6], [8,6], [9,12], [10,12], [11,24] , [12,6], [13, 9], [14, 3]]

for entry in sizes:
    puzzle.nodes[entry[0]].setSize(entry[1])
