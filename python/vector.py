import math


# Returns the angle between 2 vectors in radians
def get_angle_diff(vec1, vec2):
    dist = vec1 - vec2
    return dist.get_angle()


# Returns the distance between 2 vectors
def get_distance(vec1, vec2):
    dist = vec1 - vec2
    return dist.get_len()


# Returns the dot product of 2 vectors
#|vec1|*|vec2|*cos(angleDiff(vec1, vec2))
def dot_product(vec1, vec2):
    return vec1.get_len() * vec2.get_len() * math.cos(get_angle_diff(vec1, vec2))


def mult2(vec1, vec2):
    return vec1.x * vec2.x + vec1.y * vec2.y


class Vector2:
    PLANE_PIXELS = "pixels"
    PLANE_BLOCKS = "blocks"


    def __init__(self, x, y = None, plane=PLANE_PIXELS):
        if isinstance(x, tuple) and y == None:
            self.x = x[0]
            self.y = x[1]
        else:
            self.plane = plane
            self.x = x
            self.y = y

    def __str__(self):
        return "Vec2[{}, {}]".format(self.x, self.y)

    #Add 2 vectors and return the result
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    #Subtract 2 vectors and return the result 
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    #Multiply a vector and a number and return the result
    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def __eq__(self, other):
        if(other == None):
            return  False

        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return self.__str__()

    def __div__(self, other):
        return Vector2(self.x / other, self.y / other)

    def __truediv__(self, other):
        return Vector2(self.x / other, self.y / other)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    #Returns the length of the vector
    def get_len(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    #Returns the angle of the vector
    def get_angle(self):
        return math.atan2(self.y, self.x)

    def getTuple(self):
        return (self.x, self.y)

