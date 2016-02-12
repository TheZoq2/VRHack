#
# furnitureList: [door | window x 3, furniture1, furniture2, ...]
# furniture: (int: x1, int: x2, int: y1, int: y2, string: type)
#

################################################################
# Functions for getting information about a furniture item.
################################################################

def getX(furniture):
    return (furniture[0], furniture[2])

def getY(furniture):
    return (furniture[1], furniture[3])

def getType(furniture):
    return furniture[4]

def getX1(furniture):
    return furniture[0]

def getX2(furniture):
    return furniture[1]

def getY1(furniture):
    return furniture[2]

def getY2(furniture):
    return furniture[3]

################################################################
# Functions for getting information about the placement of
# furniture in the room.
################################################################

# furnitureList -> door
def getDoor(furnitureList): 
    for furniture in furnitureList:
        if getType(furniture) == "door":
            return furniture
    raise Exception("Door not found")

# furnitureList -> [window, window]
def getWindows(furnitureList):
    windows = []
    for furniture in furnitureList:
        if getType(furniture) == "window":
            windows.append(furniture)
    if len(windows) != 2:
        raise Exception("Two windows not found")
    return windows

################################################################
