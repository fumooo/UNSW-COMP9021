# Written by *** for COMP9021
#
# Defines two classes, Point and Triangle.
#
# An object of class Point is created by passing exactly
# 2 integers as arguments to __init__().
# You can assume that nothing but integers will indeed be
# passed as arguments to __init__(), but not that exactly
# 2 arguments will be provided; when that is not the case,
# a PointError error is raised.
# The point class implements the __str__() and __repr__()
# special methods.
#
# An object of class Triangle is created by passing exactly
# 3 points as keyword only arguments to __init__().
# You can assume that exactly three points will indeed be
# passed as arguments to __init__().
# The three points should not be collinear for the triangle
# to be created; otherwise a TriangleError error is raised.
# A triangle object can be modified by changing one two or three
# points thanks to the method change_point_or_points(),
# all of whose arguments are keyword only.
# At any stage, the object maintains correct values
# for perimeter and area.
import sys
from fractions import Fraction
from math import sqrt

class PointError(Exception):
    def __init__(self,error):
        self.error = error

# INSERT YOUR CODE HERE
class Point():
    def __init__(self, *args):
        if(len(args) !=2 ):
            raise PointError("Need two coordinates, point not created.")
        self.x = args[0]
        self.y = args[1]
        # print(f'Point({self.x},{self.y})')
        # if (self.x == 0 and self.y == 0):
        #     print(f'Point({self.x},{self.y})')
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    def __str__(self):
        return f'Point of x-coordinate {self.x} and y-coordinate {self.y}'

class TriangleError(Exception):
    def __init__(self,error):
        self.error = error

class Triangle():
    def __init__(self, **kwargs):
        self.point1 = kwargs["point_1"]
        self.point2 = kwargs["point_2"]
        self.point3 = kwargs["point_3"]
        # print(point1.x,point1.y,point2,point3)
        if(self.checkIsVaild()):
            raise TriangleError("Incorrect input, triangle not created.")

        # x1 = self.point1.x - self.point2.x
        # y1 = self.point1.y - self.point2.y
        # x2 = self.point1.x - self.point3.x
        # y2 = self.point1.y - self.point3.y
        # if(x1 * y2 - y1 * x2 == 0):
        #     raise TriangleError("Incorrect input, triangle not created.")
    def checkIsVaild(self):
        x1 = self.point1.x - self.point2.x
        y1 = self.point1.y - self.point2.y
        x2 = self.point1.x - self.point3.x
        y2 = self.point1.y - self.point3.y
        # print(x1,y1,x2,y2)
        if (x1 * y2 - y1 * x2 == 0):
            return True


    def calculate_side_length(self, p1, p2):#计算边长
        return sqrt( (p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

    @property
    def perimeter(self):
        side1 = self.calculate_side_length(self.point1, self.point2)
        side2 = self.calculate_side_length(self.point2, self.point3)
        side3 = self.calculate_side_length(self.point3, self.point1)
        perimeter = side1 + side2 + side3
        return perimeter
        # print(perimeter)


    def perimeterCopy(self):
        side1 = self.calculate_side_length(self.point1, self.point2)
        side2 = self.calculate_side_length(self.point2, self.point3)
        side3 = self.calculate_side_length(self.point3, self.point1)
        perimeter = side1 + side2 + side3
        return perimeter

    @property
    def area(self):
        area = 0
        side1 = self.calculate_side_length(self.point1, self.point2)
        side2 = self.calculate_side_length(self.point2, self.point3)
        side3 = self.calculate_side_length(self.point3, self.point1)

        s = self.perimeterCopy() / 2  # 半周长
        area = sqrt(s * (s - side1) * (s - side2) * (s - side3))
        return area
        # print(area)

    def change_point_or_points(self,**kwargs):
        # if(len(kwargs) == 1):
        #     print("Incorrect input, triangle not modified.")
        # print(kwargs)
        point1 = self.point1
        point2 = self.point2
        point3 = self.point3
        if(len(kwargs) > 0):
            if("point_1" in kwargs):
                self.point1 = kwargs["point_1"]
            if ("point_2" in kwargs):
                self.point2 = kwargs["point_2"]
            if ("point_3" in kwargs):
                self.point3 = kwargs["point_3"]
        if (self.checkIsVaild()):
            print("Incorrect input, triangle not modified.")
            self.point1 = point1
            self.point2 = point2
            self.point3 = point3
            # sys.exit()




if __name__ == '__main__':
    # Point(0, 0)
    #
    # print(Point(0, 0))
    p1 = Point(1, 2)
    p2 = Point(4, 8)
    # p3 = Point(2, 4)
    p3 = Point(3, 5)
    # Triangle(p1, p2, p3)
    triangle = Triangle(point_1=p1, point_2=p2, point_3=p3)

    p0 = Point(0, 0)
    p3 = Point(0, 4)
    triangle.change_point_or_points(point_3=p3)
    triangle.change_point_or_points(point_3=p3, point_1=p0)
    triangle.change_point_or_points(point_2=Point(4, 0))
    triangle.change_point_or_points(point_3=Point(4, 0))

    triangle.change_point_or_points(point_3=Point(4, 8))
    # triangle.perimeter
    triangle.area

