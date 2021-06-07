import math

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def isEqualTo(self, pointb, tol=0.001):
        return abs(self.x - pointb.x) < tol and abs(self.y - pointb.y) < tol

    def coords(self):
        return self.x, self.y

    def dist(self, pointb):
        return math.sqrt(math.pow(pointb.x - self.x, 2) + math.pow(pointb.y - self.y, 2))

class line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class rect:
    def __init__(self, corner, width, height):
        if type(corner) is tuple:
            corner = point(corner[0], corner[1])

        self.leftx = corner.x
        self.rightx = corner.x + width
        self.topy = corner.y
        self.bottomy = corner.y + height

        self.width = width
        self.height = height

        self.TL = point(self.leftx, self.topy)
        self.BR = point(self.rightx, self.bottomy)
        self.BL = point(self.leftx, self.bottomy)
        self.TR = point(self.rightx, self.topy)

        self.area = width * height
        self.perimiter = 2 * (width + height)

        self.centerx = corner.x + width/2
        self.centery = corner.y + height/2

class circle:
    def __init__(self, center, rad):
        if type(center) is tuple:
            center = point(center[0], center[1])
        self.center = center
        self.rad = rad
        self.dia = 2 * rad

        self.circum = self.dia * math.pi
        self.area = math.pow(self.rad, 2) * math.pi
