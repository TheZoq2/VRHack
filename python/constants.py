# C1 = (0,0)                 C2 = (ROOM_WIDTH, 0)
#       +------------------+
#       |       WALL1      |
#       |                  |
#       |                  |
#       | WALL4      WALL2 |
#       |                  |
#       |                  |
#       |       WALL3      |
#       +------------------+
# C4 = (0, ROOM_WIDTH)       C3 = (ROOM_WIDTH, ROOM_WIDTH)

ROOM_WIDTH = 500

C1 = (0, 0)
C2 = (ROOM_WIDTH, 0)
C3 = (ROOM_WIDTH, ROOM_WIDTH)
C4 = (0, ROOM_WIDTH)

WALL1 = (C1, C2)
WALL2 = (C2, C3)
WALL3 = (C4, C3)
WALL4 = (C1, C4)
WALLS = [WALL1, WALL2, WALL3, WALL4]

BED_SIZE = (90, 200)
COUCH_SIZE = (80, 250)
DESK_SIZE = (70, 150)
CHAIR_SIZE = (60, 60)
TV_SIZE = (3, 80)
TABLE_SIZE = (50, 80)
RUG_SIZE = (150, 200)
SHELF_SIZE = (40, 100)

WINDOW_WIDTH = 90
DOOR_WIDTH = 100

WARNING_NONE = 0
WARNING_LOW = 1
WARNING_WINDOW = 2
WARNING_HARD = 3

FURNITURE_WARN_LEVELS = {
            "bed": WARNING_HARD,
            "couch": WARNING_HARD,
            "desk": WARNING_HARD,
            "chair": WARNING_HARD,
            "tv": WARNING_WINDOW,
            "table": WARNING_HARD,
            "rug": WARNING_NONE,
            "shelf": WARNING_HARD,
            "window": WARNING_WINDOW,
            "door": WARNING_HARD,
            }

FURNITURE_SIZES = {
    "bed" : BED_SIZE,
    "couch" : COUCH_SIZE,
    "desk" : DESK_SIZE,
    "chair" : CHAIR_SIZE,
    "tv" : TV_SIZE,
    "table" : TABLE_SIZE,
    "rug" : RUG_SIZE,
    "shelf" : SHELF_SIZE,
    "window" : WINDOW_WIDTH,
    "door" : DOOR_WIDTH
}

#def getX(furniture):
#    return furniture[0]
#
#def getY(furniture):
#    return furniture[1]
#
#def getCenter(x1, y1, x2, y2):
#    return ((x1 + x2)/2,(y1 + y2)/2)
#
