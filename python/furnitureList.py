#
# furnitureList: [door | window x 3, furniture1, furniture2, ...]
# furniture: (int: x1, int: y1, int: x2, int: y2, string: type)
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
    return furniture[2]

def getY1(furniture):
    return furniture[1]

def getY2(furniture):
    return furniture[3]

def getCenter(furniture):
    return ((getX1(furniture) + getX2(furniture)) // 2,
            (getY1(furniture) + getY2(furniture)) // 2)

################################################################
# Functions for getting information about the position of the 
# doors and windows.
################################################################

## Returns the free space on the left side of the 
## door/window on the wall.
## door/window -> space to the left
#def getFreeWallSpaceLeft(item):
#    pass
#
## Returns the free space on the right side of the 
## door/window on the wall.
## door/window -> space to the right
#def getFreeWallSpaceRight(item):
#    pass

# Returns whether door/window is vertical or not
def isVerticalDoorWindow(item):
    return getX1(item) != getX2(item)

# Maps the windows and the door onto the walls.
# furnitureList -> { wall1 : [door | windows], wall2 : ...}
def locateDoorsAndWindows(furnitureList):
    door = getDoor(furnitureList)
    items = getWindows(furnitureList)
    # items contain both the windows and the door
    items.append(door)
    wallmap = {}
    for wall in WALLS:
        for item in items:
            if isOnWall(wall, item) and (getType(item) == "door" or \
                    getType(item) == "window"):
                wallmap[wall] = item
    return wallmap

# wallmap -> wall with door
def getWallWithDoor(wallmap):
    for wall in WALLS:
        for item in wallmap[wall]:
            if getType(item) == "door":
                return wall
    raise Exception("No wall seem to have a door")

def numberOfWindowsOnWall(wall, wallmap):
    result = 0
    for item in wallmap[wall]:
        if getType(item) == "window":
            result += 1
    return result

################################################################
# Functions for getting information about the walls.
################################################################

def getCornerX(corner):
    return corner[0]

def getCornerY(corner):
    return corner[1]

def isVerticalWall(wall):
    return getCornerX(wall[0]) != getCornerX(wall[1])

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

# wall, furniture -> boolean
def isOnWall(wall, furniture):
    if isVerticalWall(wall):
        return getY1(furniture) == getCornerY(wall[0]) or \
                getY2(furniture) == getCornerY(wall[0])
    else:
        return getX1(furniture) == getCornerX(wall[0]) or \
                getX2(furniture) == getCornerY(wall[0])

################################################################
