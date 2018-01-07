import copy

#a global var...
allEntries={"A", "B", "C", "D", "E", "F", "G"}

class Beds:
    beds=dict()
    def __init__(self, otherBed=None):
        if otherBed==None:
            for entry in "ABCDEFG": self.beds[entry]=""
        elif type(otherBed)==Beds:
            self.beds=copy.deepcopy(otherBed.beds)
        else:
            raise Exception("I don't know how to handle this")

    def __repr__(self):
        result=""
        for entry in "ABCDEFG":
            result+=entry+":"+self.beds[entry]+"\n"
        return result

    def __str__(self):
        result=""
        for entry in "ABCDEFG":
            if self.beds[entry]=="": result+="_"
            else: result+=self.beds[entry]
        return result

    def full(self):
        # A cannot take his own bed
        if self.beds["A"]=="A": return False

        seen=set()

        for bed, dwarf in self.beds.items():
            # make sure data didn't get messed up
            if bed not in allEntries: return False

            # make sure bed isn't empty and that things are valid
            if dwarf not in allEntries: return False

            # make sure we only see each dwarf once
            if dwarf in seen : return False
            else: seen.add(dwarf)

        # Check to make sure we've seen all of the dwarves
        if seen != allEntries: return False

        # If we pass everything, we're good
        return True

    def numDisplaced(self):
        if not self.full(): raise Exception("Can't run calculation if beds aren't correct")
        return sum([ 1 for bed, dwarf in self.beds.items() if bed != dwarf])

    def numEmpty(self):
        return len(self.emptyBeds())

    def emptyBeds(self):
        return [bed for bed, dwarf in self.beds.items() if dwarf==""]

    def GinBed(self):
        return self.xInOwnBed("G")

    def xInOwnBed(self, bedID):
        # error checking
        if not self.full(): raise Exception("Can't run calculation if beds aren't correct")
        elif bedID not in allEntries: raise Exception("Invalid bedID given")

        return self.beds[bedID]==bedID

    # returns list of possible states the dwarf could've chosen
    # if the dwarf's bed isn't taken, it'll chose that.
    # else, it'll chose from the random unEmpty beds
    def placeDwarf(self, dwarfID):
        if dwarfID=="A": raise Exception("Cannot use this method with Dwarf A")

        #if our own bed is empty, take it
        if self.beds[dwarfID]=="":
            self.beds[dwarfID]=dwarfID
            return [self]
        else:
            #choose uniformly from the remaining beds
            result=list()
            for bed in self.emptyBeds():
                newbed=Beds(self)
                newbed.beds[bed]=dwarfID
                result.append(newbed)

            return result

    # set things up for dwarfA
    def placeA(self):
        #cannot choose his own bed
        validSpots=copy.deepcopy(allEntries)
        validSpots.remove("A")

        result=list()
        for bed in validSpots:
            newbed=Beds(self)
            newbed.beds[bed]="A"
            result.append(newbed)
        return result

#compute everything
#set up things for dwarf A
first=Beds()
origArrangements=first.placeA()

prevTurn=list()

#prevTurn is tuples of arrangements and the probabilities th happen
origProb=1.0/float(len(origArrangements))
for arrangment in origArrangements:
    pair=(arrangment, origProb)
    prevTurn.append(pair)

#set up stack of dwarves to place
toPlace=["B", "C", "D", "E", "F", "G"]

#place to put our results
final=list()

for dwarf in toPlace:

    #set up place to put intermediates
    nextTurn=list()

    for arrangement, prob in prevTurn:

        #list of new arrangements after placing another dwarf
        possibleChoices=arrangement.placeDwarf(dwarf)

        # the dwarf could go into his own bed, no need for decision making here
        if len(possibleChoices)==1:
            pair=(possibleChoices[0], prob)
            nextTurn.append(pair)

        # the dwarf couldn't get his own bed
        # we need to deal with the possible choices made
        # if there were three choices the dwarf could've made,
        # we enter each into the possible arrangements and "split"
        # the probability the parent had three ways
        else:
            factor=1.0/float(len(possibleChoices))
            for choice in possibleChoices:
                pair=(choice, prob*factor)
                nextTurn.append(pair)

    #set up the next run
    prevTurn=nextTurn

    #set up final variable if we're done
    if dwarf=="G": final=nextTurn

printAllBoards=False
if printAllBoards:

    print(len(nextTurn), "different arrangements")
    print("arrangement, probability that happened")

    for entry in final:
        print(entry[0], entry[1])
    print()

mostLeastCommon=False
if mostLeastCommon:
    #sort on probability
    final.sort(key=lambda x:x[1])
    print("most common arrangement:", final[-1][0], final[-1][1])
    print("least common arrangement:", final[0][0], final[0][1])
    print()

#Average number of dwarves displaced
dwarvesDisplaced=sum([x[1]*x[0].numDisplaced() for x in final])
print("Average number of dwarves displaced:", dwarvesDisplaced)

#percent everyone else is in own bed
print("Percentage X dwarf is in their own bed")
for dwarf in "ABCDEFG":
    percentDisplaced=sum([x[1] for x in final if x[0].xInOwnBed(dwarf)])
    print(dwarf, percentDisplaced)
