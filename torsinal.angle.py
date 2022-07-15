"""Torsinal Angle Solution Hacker rank problem."""

# -----------------------------------------------------------------------------
# You are given A,B,C and D in a 3-dimensional cartesian coordinate system.
# You are required to print the angle between the vectors A,B,C and
# B,C,D in degrees.(not radians)
# Length of the angle be PHI
#  cos(PHI) = (X.Y) / |X|.|Y| where X = AB * BC and Y = BC * CD
# Here X.Y is the dot product of X and Y and AB * BS means the cross product
# of AB and BC.Also AB = B - A.
#
# Input Format
# One line containing the space separated floating point values of X, Y, Z
# Coordinates of a point.
#
# Output Format
# Output the angle corrct upto two decimal places.
#
# Sample Input
# 0 4 5
# 1 7 6
# 0 5 9
# 1 7 2
#
# Sample Output
# 8.19
# -----------------------------------------------------------------------------
# Solution
import math


class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        "dot product of 2 vector"
        return (self.x * no.x + self.y * no.y + self.z * no.z)

    def cross(self, no):
        """Cross product of 2 vector"""
        return Points(self.y * no.z - self.z * no.y,
                      self.z * no.x - self.x * no.z,
                      self.x * no.y - self.y * no.x)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]
                                            ), Points(*points[2]), Points(*points[3])

    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
