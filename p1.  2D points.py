######################################################################################################################
# Name: Victoria Giepert
# Date: 3/14/22
# Description: program 1 2D points
######################################################################################################################
#we need to square root for distance formula 
from math import sqrt

# the 2D point class
class Point:
    def __init__(self, x=0, y=0): #default values
        self.x = x
        self.y = y

    #accessors aka getters
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    #mutators aka setters
    @x.setter
    def x(self, value):
        self._x = float(value) #the numbers entered are int so this will convet them to float
            
    @y.setter
    def y(self, value):
        self._y = float(value)

    #magic function that makes it readable
    def __str__(self):
        return "({},{})".format(self.x, self.y)

    #take two points as inputs and calculate and return the distance
    def dist(self, p):
        x1, y1 = self.x, self.y #did this so COULD unpack non-iterable Point object
        x2, y2 = p.x, p.y

        a = (x2 - x1)**2
        b = (y2 - y1)**2
        ab = a + b
        d = sqrt(ab)
        return d

    #take two points as inputs ams calculate and return the midpoint
    def midpt(self, p):
        x1, y1 = self.x, self.y
        x2, y2 = p.x, p.y

        a = (x1 + x2) / 2
        b = (y1 + y2) / 2

        m = Point(a, b) #is a new point
        return m

        

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# create some points
p1 = Point()
p2 = Point(3, 0)
p3 = Point(3, 4)
# display them
print("p1:", p1)
print("p2:", p2)
print("p3:", p3)
# calculate and display some distances
print("distance from p1 to p2:", p1.dist(p2))
print("distance from p2 to p3:", p2.dist(p3))
print("distance from p1 to p3:", p1.dist(p3))
# calculate and display some midpoints
print("midpt of p1 and p2:", p1.midpt(p2))
print("midpt of p2 and p3:", p2.midpt(p3))
print("midpt of p1 and p3:", p1.midpt(p3))
# just a few more things...
p4 = p1.midpt(p3)
print("p4:", p4)
print("distance from p4 to p1:", p4.dist(p1))





