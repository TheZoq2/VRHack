from furnitureList import *

def placeDesksAndChairs(furnitureList, availableFurniture):
    pass

def placeCouchesTablesAndTv(furnitureList, availableFurniture):
    # maps the doors and windows to corresponding walls
    wallmap = locateDoorsAndWindows(furnitureList)
    # we should place the TV on opposite sides of the 
    # windows and 

def placeBeds(furnitureList, availableFurniture):
    pass

def placeShelves(furnitureList, availableFurniture):
    pass

def placeRugs(furnitureList, availableFurniture):
    pass

###################################################################
# Help functions
###################################################################

# furnitureList -> { wall1 : [door | windows], wall2 : ...}
def locateDoorsAndWindows(furnitureList):
    door = getDoor(furnitureList)
    items = getWindows(furnitureList)
    # items contain both the windows and the door
    items.append(door)

    wallmap = {}

    for wall in WALLS:
        for item in items:
            if isOnWall(wall, item):
                wallmap[wall] = item
    return wallmap

###################################################################
