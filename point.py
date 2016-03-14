import unittest

from .utils import check_coincident, shift_point

class Point(object):
    def __init__(self,x,y,mark={}):
        self.x = x
        self.y = y
        self.mark = mark

    def patched_coincident(self,point2):
        point1 = (self.x,self.y)

        return check_coincident(point1,point2)

    def patched_shift(self,x_shift,y_shift):
        point = (self.x,self.y)
        self.x,self.y = shift_point(point,x_shift,y_shift)