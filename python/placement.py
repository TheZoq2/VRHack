import furnitureList as fl
import warnArea

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


def placeDesksAndChairs(furnitureList, availableFurniture):
    pass

def placeCouchesTablesAndTv(furnitureList, availableFurniture):
    # maps the doors and windows to corresponding walls
    wallmap = locateDoorsAndWindows(furnitureList)
    # we should place the TV on opposite sides of the 
    # windows and preferably on the same side as the door
    wallWithDoor = getWallWithDoor(wallmap)
    if wallmap[wallWithDoor]:
        pass

def placeBeds(furnitureList, availableFurniture):
    pass

def placeShelves(furnitureList, availableFurniture):
    pass

def placeRugs(furnitureList, availableFurniture):
    pass

###################################################################
# Help functions
###################################################################


###################################################################
