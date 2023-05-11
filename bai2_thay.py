from bai1 import Point
import math
import copy

class LineSegment:
    __d1 = Point()
    __d2 = Point()

    def __init__(self,*args):
        if len(args) == 0:
            self.__d1 = Point(8,5)
            self.__d2 = Point(1,0)
        if len(args) == 2:
            self.__d1 = args[0]
            self.__d2 = args[1]
        if len(args) == 4:
            self.__d1 = Point(args[0],args[1])
            self.__d2 = Point(args[2],args[3])
        if len(args) == 1:
            if isinstance(args[0], LineSegment):
                # self = copy.deepcopy(args[0])
                self.__d1 = args[0].__d1
                self.__d1 = args[0].__d2

    def read(self):
        s = input("Nhập tọa độ đoạn thẳng:")
        self.__d1 = Point(int(s.split()[0]),int(s.split()[1]))
        self.__d2 = Point(int(s.split()[2]),int(s.split()[3]))
  
    def __str__(self):
        return "[(%d,%d);(%d,%d)]" % (self.__d1.getX(),self.__d1.getY(),self.__d2.getX(), self.__d2.getY())

    def move(self, dx=0, dy=0):
        self.__d1.move(dx,dy)
        self.__d2.move(dx,dy)

    def length(self):
        return "{:.2f}".format(self.__d1.distance(self.__d2))

    def angle(self):
        return math.atan2(self.__d2.getY()-self.__d1.getY(), self.__d2.getX()-self.__d1.getX())

class LineSegmentTest:
    def testCase1(self):
        A = Point(2, 5)
        print(A)
        B = Point(20, 35)
        print(B)
        AB = LineSegment(A, B)
        print(AB)
        AB.move(35, 51)
        print(AB)

    def testCase2(self):
        CD = LineSegment()
        CD.read()
        print(CD)
        print("|CD| = {:.2f}".format(CD.length()))

    def testCase3(self):
        n = int(input("Nhập số đoạn thẳng:"))
        danhsach = []

        for i in range(n):
            l = LineSegment()
            l.read()
            danhsach.append(l)

        for s in danhsach:
            print(s)
            print(s.length())

        danhsach.sort(key = lambda dist: dist.length(), reserve = True)

        for s in danhsach:
            print(s)
            print(s.length())

    def main():
        LineSegmentTest().testCase1()
        LineSegmentTest().testCase2()
        LineSegmentTest().testCase3()

a = LineSegment()
b = LineSegment(a)
print(a)
print(b)
















