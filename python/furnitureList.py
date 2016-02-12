#
# furnitureList: [furniture1, furniture2, ...]
# furniture: (int: x1, int: x2, int: y1, int: y2, string: type)
#


def getX(furniture):
    return (furniture[0], furniture[2])

def getY(furniture):
    return (furniture[1], furniture[3])

def getType(furniture):
    return furniture[4]
