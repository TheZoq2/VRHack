from furnitureList import *

def placeDesksAndChairs(furnitureList, availableFurniture):
    pass

def placeCouchesTablesAndTv(furnitureList, availableFurniture):
    # maps the doors and windows to corresponding walls
    wallmap = locateDoorsAndWindows(furnitureList)
    # we should place the TV on opposite sides of the 
    # windows and preferably on the same side as the door
    wallWithDoor = getWallWithDoor(wallmap)
    if wallmap[wallWithDoor]

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
