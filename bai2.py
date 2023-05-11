from __future__ import annotations

import math


class Point:
    __y = int
    __x = int

    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    
    def read(self, x=int, y=int):
        try:
            self.__x = x
            self.__y = y
        except TypeError:
            print("You typed wrong variable format!")

    # move the point to another position
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy
        return f"New Position: ({self.__x}, {self.__y})"

    # return x value
    def getX(self):
        return self.__x

    # return y value
    def getY(self):
        return self.__y

    def distance(self, *args):
        if len(args) == 0:
            return math.sqrt(self.__x ** 2 + self.__y ** 2)

        if len(args) == 1:
            if isinstance(args[0], Point):
                return math.sqrt((int(self.__x) - int(args[0].__x)) ** 2 + (int(self.__y) - int(args[0].__y)) ** 2)


class LineSegment:
    __d1 = Point()
    __d2 = Point()

    def __init__(self, *args):
        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)

        elif len(args) == 2:
            if isinstance(args[0], Point) and isinstance(args[1], Point):
                self.__d1 = args[0]
                self.__d2 = args[1]


        elif len(args) == 4:
            if isinstance(args[0], int):
                self.__d1 = Point(args[0], args[1])
                self.__d2 = Point(args[2], args[3])

        elif len(args) == 1:
            if isinstance(args[0], LineSegment):
                self.__d1 = args[0].__d1
                self.__d2 = args[0].__d2
        # alternative ways
        # ||
        # vv
        # if len(args) == 1:
        #     self = copy.deepcopy(args[0])

    def __str__(self): 
        return f"[{self.__d1}; {self.__d2}]"



    def read(self):
        s = input("Nhap toa do doan thang: ")
        self.__d1 = Point(s.split()[0], s.split()[1])
        self.__d2 = Point(s.split()[2], s.split()[3])

    def print(self):
        print(f"[{self.__d1}; {self.__d2}]")

    def move(self, dx=0, dy=0):
        self.__d1.move(dx, dy)
        self.__d2.move(dx, dy)
        return f"[({self.__d1.getX()}, {self.__d1.getY()}); ({self.__d2.getX()}, {self.__d2.getY()})]"

    def length(self):
        return self.__d1.distance(self.__d2)

    def angle(self):
        return math.atan(self.__d1.getY(), self.__d1.getX())


class LineSegmentTest:
    def testCase1(self):
        A = Point(2, 5)
        B = Point(20, 35)
        AB = LineSegment(A, B)
        AB.print()
        AB.move(35, 51)
        AB.print()

    def testCase2(self):
        CD = LineSegment()
        CD.read()
        CD.length()
        print(f'|CD| = {CD.length():.2f}')

    def testCase3(self):
        n = int(input("Nhap vao so doan thang: "))
        danhsach = []
        for i in range(n):
            l = LineSegment()
            l.read()
            danhsach.append(l)
            
            danhsach.sort(key= lambda dist: dist.length())

            for s in danhsach: 
                print(s)
                print(s.length())

LineSegmentTest().testCase3()
