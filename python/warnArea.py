import constants;
from vector import Vector2
import pdb

X = 0
Y = 1

def getWarnLevelForFurniture(name):
    return constants.FURNITURE_WARN_LEVELS[name]

def addWarnArea(warnAreas, corners, level):
    warnAreas.append(WarnArea(corners, level));

def getWarnLevel(pos, warnAreas):
    worstLimit = constants.WARNING_NONE;

    for area in warnAreas:
        if(area.level > worstLimit):
            if(area.isInArea(pos)):
                worstLimit = area.level;

    return worstLimit;
        
def isFree(corner1, corner2, warnAreas):
    ax = min(corner1.x, corner2.x)
    ay = min(corner1.y, corner2.y)
    awidth = max(corner1.x, corner2.x) - ax
    aheight = max(corner1.y, corner2.y) - ay

    for area in warnAreas:
        if area.level == constants.WARNING_HARD:
            ac1 = area.corners[0]
            ac2 = area.corners[1]

            bx = min(ac1.x, ac2.x)
            by = min(ac1.y, ac2.y)
            bwidth = max(ac1.x, ac2.x) - ax
            bheight = max(ac1.y, ac2.y) - ay

            if (abs(ax - by) * 2 < (awidth + bwidth)) and \
               (abs(ay - by) * 2 < (aheight + bheight)):
                return False
    return True

class WarnArea:
    def __init__(self, corners, level):
        self.corners = [
                Vector2(corners[0]),
                Vector2(corners[1])
            ]

        #Flip coordinates if they are flipped
        if self.corners[0].x > self.corners[1].x:
            temp = self.corners[0].x 
            self.corners[0].x = self.corners[1].x
            self.corners[1].x = temp;
        if self.corners[0].y > self.corners[1].y:
            temp = self.corners[0].y 
            self.corners[0].y = self.corners[1].y
            self.corners[1].y = temp;

        self.level = level;

    def isInArea(self, pos):
        c = self.corners;

        #Check x
        if c[0].x <= pos.x and c[1].x >= pos.x:
            #check y
            if c[0].y <= pos.y and c[1].y >= pos.y:
                return True;
            
        return False;

    def __str__(self):
        return "Warn area: ({}), ({}))".format(self.corners[0], self.corners[1])

