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
    for i in warnAreas:
        print(i)
    freeSpace = fl.getFreeSpace(constants.WARNING_HARD, warnAreas)

    print("Free space", freeSpace);




###################################################################
# Help functions
###################################################################


###################################################################
