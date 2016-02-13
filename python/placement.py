import furnitureList as fl
import warnArea
import constants

def addPlacedFurniture(placedFurniture, furniture, warnAreas):
    placedFurniture.append(furniture)
    
    #Add a warn area for the furniture
    warnArea.addWarnArea( warnAreas, 
            (
                fl.getCorner1(furniture), 
                fl.getCorner2(furniture)
            ),
            warnArea.getWarnLevelForFurniture(fl.getType(furniture))
        )


def placeFurniture(placedFurniture, availableFurniture, warnAreas):
    for i in warnAreas:
        print(i)
    freeSpace = fl.getFreeSpace(constants.WARNING_HARD, warnAreas)

    print("Free space", freeSpace);

def assessScore(furniture, warnArea):
    freeSpace = fl.getFreeSpace(constants.WARNING_HARD, warnAreas)
    if getType(furniture) == "bed":
        return assessBedScore(freeSpaces)
#    elif getType(furniture) == "couch":
#        return assessCouchScore(freeSpaces)
    elif getType(furniture) == "desk":
        return assessDeskScore(freeSpaces)
#    elif getType(furniture) == "chair":
#        return assessChairScore(freeSpaces)
    elif getType(furniture) == "tv":
        return assessTVScore(freeSpaces)
    elif getType(furniture) == "table":
        return assessTableScore(freeSpaces)
#    elif getType(furniture) == "rug":
#        return assessRugScore(freeSpaces)
    elif getType(furniture) == "shelf":
        return assessShelfScore(freeSpaces)

# Functions for assesing the scores of different pieces of
# furniture. TODO THIS MIGHT NOT WORK WITH THE TV AND COUCH GROUP
def assessBedScore(freeSpaces):
    pass

# TODO probably not applicable
def assessCouchScore(freeSpaces):
    pass

def assessDeskScore(freeSpaces):
    pass

# TODO probably not applicable
def assessChairScore(freeSpaces):
    pass

def assessTVScore(freeSpaces):
    spacesWithScore = []
    for space in freeSpaces:
        score = 100
        v1 = space[0]
        v2 = space[1]
        distance = get_distance(v1, v2)
        if distance < TV_SIZE[1]: # if the space does not fit tv...
            spacesWithScore.append(space + [0]) # score is 0
            continue
        score *= 1/distance
        if canPlaceCouch(space):
            score = 0
        spacesWithScore.append(space + [score])
    return spacesWithScore

# TODO probably not applicable
def assessTableScore(freeSpaces):
    pass

# TODO probably not applicable
def assessRugScore(freeSpaces):
    pass

def assessShelfScore(freeSpaces):
    pass

###################################################################
# Help functions
###################################################################


###################################################################
