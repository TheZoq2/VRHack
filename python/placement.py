import furnitureList as fl
import warnArea
import constants

def addPlacedFurniture(placedFurniture, furniture, warnAreas):
    placedFurniture.append(furniture);

    #Add a warn area for the furniture
    warnArea.addWarnArea( warnAreas, 
            (
                fl.getCorner1(furniture), 
                fl.getCorner2(furniture)
            ),
            warnArea.getWarnLevelForFurniture(fl.getType(furniture))
        )


def placeFurniture(placedFurniture, availableFurniture, warnAreas):
    freeSpace = fl.getFreeSpace(constants.WARNING_HARD, warnAreas)

    print("Free space", freeSpace);

def canPlaceCouch(span, warnArea):
    #Check the coordinates
    if span[0].x == span[1].x:
        if span[0].x == 500:
            span[0].x = span[1].x = 0
        else:
            span[0].x = span[1].x = 500

        for i in range(span[0].y, span[1].y + 1)):
            warnArea.getWarnLevel(Vector2(i, span[0].x))
    else:
        if span[0].y == 500:
            span[0].y = span[1].y = 0
        else:
            span[0].y = span[1].y = 500

        for i in range(span[0].x, span[1].x + 1)):
            warnArea.getWarnLevel(Vector2(span[0].x, i))





###################################################################
# Help functions
###################################################################


###################################################################
