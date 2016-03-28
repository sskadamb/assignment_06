
import unittest
import sys
import random
import os
#sys.path.insert(0, os.path.abspath('..'))



#sys.path.insert(0, os.path.abspath('..'))




class TestPoint(unittest.TestCase):
    def setUp(self):
        pass

    def test_xyCheck(self):
        points = point.Point(5,4)
        self.assertEqual(5,points.x)
        self.assertEqual(4,points.y)

    def test_coincident(self):
        point1 = point.Point(1,2)

        self.assertTrue(point1.patched_coincident((1,2)))
        self.assertFalse(point1.patched_coincident((3,4)))

    def test_shift(self):
        point1 = point.Point(1,0)
        point1.patched_shift(1,2)
        self.assertEqual((2,2),(point1.x,point1.y))

    def test_marks(self):
        random.seed(12345)

        marks = ['lavender','orange','rose','ash','violet','magenta','cerulean']

        #list of points:
        points = []
        markArray = []
        #instantiate 15 random points
        for i in range(15):
            new_point = point.Point(random.randint(0,9),random.randint(0,9),random.choice(marks))
            print(new_point.x)
            print(new_point.y)
            print(new_point.mark)
            points.append(new_point)

        #count the amount of times a mark appears in the list
        for p in points:
            markArray.append(p.mark)
        c = Counter(markArray)

        self.assertEqual(c["lavender"],4)
        self.assertEqual(c["cerulean"],3)
        self.assertEqual(c["violet"],3)
        self.assertEqual(c["magenta"],2)
        self.assertEqual(c["orange"],2)
        self.assertEqual(c["ash"],1)

from .. import point
from collections import Counter