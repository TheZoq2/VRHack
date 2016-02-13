import furnitureList as fl
import random
import warnArea
import constants
from vector import *

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


def canPlaceCouch(span, warnAreas):
    #Check the coordinates
    if span[0].x == span[1].x:
        if span[0].x == 500:
            span[0].x = span[1].x = 0
        else:
            span[0].x = span[1].x = 500

        for i in range(span[0].y, span[1].y + 1):
            if warnArea.getWarnLevel(Vector2(span[0].x, i), warnAreas):
                return False
    else:
        if span[0].y == 500:
            span[0].y = span[1].y = 0
        else:
            span[0].y = span[1].y = 500

        for i in range(span[0].x, span[1].x + 1):
            if warnArea.getWarnLevel(Vector2(i, span[0].y), warnAreas):
                return False

    return True

def assessScore(furniture, warnAreas):
    freeSpaces = fl.getFreeSpace(constants.WARNING_HARD, warnAreas)

    if furniture == "bed":
        return assessBedScore(freeSpaces)
#    elif getType(furniture) == "couch":
#        return assessCouchScore(freeSpaces)
    elif furniture == "desk":
        return assessDeskScore(freeSpaces)
#    elif getType(furniture) == "chair":
#        return assessChairScore(freeSpaces)
    elif furniture == "tv":
        return assessTVScore(freeSpaces, warnAreas)
    elif furniture == "table":
        return assessTableScore(freeSpaces)
#    elif getType(furniture) == "rug":
#        return assessRugScore(freeSpaces)
    elif furniture == "shelf":
        return assessShelfScore(freeSpaces)

# Functions for assesing the scores of different pieces of
# furniture. TODO THIS MIGHT NOT WORK WITH THE TV AND COUCH GROUP
#def assessBedScore(freeSpaces):
#    spacesWithScore = []
#    for space in freeSpaces:
#        score = 100
#        v1 = space[0]
#        v2 = space[1]
#        distance = get_distance(v1, v2)
#        score *= 1/distance
#        if space[0].y != ROOM_WIDTH: #if we are
#
#        corner1 = space[0]
#        corner2 = space[0].
#        if isFree()
#            score = 0
#        spacesWithScore.append(space + [score])
#        
#    return spacesWithScore

def bruteForce(placedFurniture, availableFurniture, warnAreas):
    for furniture in availableFurniture:
        maxIt = 100 # maximum number of tests
        numberOfItems = availableFurniture[furniture]
        while maxIt and numberOfItems:
            maxIt -= 1
            fW = FURNITURE_SIZES[furniture][0]
            fH = FURNITURE_SIZES[furniture][1]
            randx = random.randint(0, ROOM_WIDTH - fW)
            randy = random.randint(0, ROOM_WIDTH - fH)
            v1 = Vector2(randx, randy)
            v2 = Vector2(randx + fW, randy + fH)
            if isFree(v1, v2, warnAreas):
                numberOfItems -= 1
                addPlacedFurniture(placedFurniture, \
                        createFurniture(v1, v2, furniture), warnArea)
    
    


def createFurniture(vec1, vec2, type_):
    return (vec1.x, vec1.y, vec2.x, vec2.y, type_)
# TODO probably not applicable
def assessCouchScore(freeSpaces):
    pass

def assessDeskScore(freeSpaces):
    pass

# TODO probably not applicable
def assessChairScore(freeSpaces):
    pass

def assessTVScore(freeSpaces, warnAreas):
    spacesWithScore = []
    for space in freeSpaces:
        score = 100
        v1 = space[0]
        v2 = space[1]
        distance = get_distance(v1, v2)
        if distance < constants.TV_SIZE[1]: # if the space does not fit tv...
            spacesWithScore.append(space + [0]) # score is 0
            continue
        score *= 1/distance
        if not canPlaceCouch(space, warnAreas):
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


def placeFurnitureInSpan(furnitureName, span, placedFurniture, warnAreas):
    furnitureSize = constants.FURNITURE_SIZES[furnitureName];

    print("Span: ", span);

    width = furnitureSize[0]
    height = furnitureSize[1];
    
    pos0 = Vector2(0,0)
    pos1 = Vector2(0,0)
    #Calculating the direction of the furniture
    if span[0].y == span[1].y:
        middle =  span[0].x + (span[1].x - span[0].x) / 2;

        if(span[0].y == 0):
            pos0.x = middle - width / 2;
            pos0.y = span[0].y;

            pos1.x = middle + width / 2;
            pos1.y = span[0].y + height

        else:
            pos0.x = middle + width / 2;
            pos0.y = span[0].y;

            pos1.x = middle - width / 2;
            pos1.y = span[0].y - height
    else:
        middle =  span[0].y + (span[1].y - span[0].y) / 2;

        if(span[0].x == 0):
            pos0.x = span[0].x
            pos0.y = middle + width / 2

            pos1.x = span[0].x + height
            pos1.y = middle - width / 2
        else:
            pos0.x = span[0].x
            pos0.y = middle - width / 2

            pos1.x = span[0].x - height
            pos1.y = middle + width

    addPlacedFurniture(placedFurniture, (pos0.x, pos0.y, pos1.x, pos1.y, furnitureName), warnAreas);
    

###################################################################
# Help functions
###################################################################


###################################################################
