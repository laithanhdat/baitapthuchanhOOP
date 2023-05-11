import math
class Point:
    __x = int
    __y = int

    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def read(self):
        s = input("Nhập vào tọa độ:")
        self.__x = int(s.split()[0])
        self.__y = int(s.split()[1])

    def __str__(self):
        return "(%d, %d)\n" % (self.__x, self.__y)

    def move(self, dx=0, dy=0):
        self.__x += dx
        self.__y += dy

    def getX(self):
        return self.__x
    def getY(self):
        return self.__y

    def distance(self,*args):
        if len(args) == 0:
            d = math.sqrt(self.__x**2 + self.__y**2)
        if len(args) == 1:
            if isinstance(args[0], Point):
                d = math.sqrt((self.__x-args[0].__x)**2 + (self.__y-args[0].__y)**2)
        return d

class PointTest:
    def main():
        A = Point(3,4)
        print("Điểm A:", A)
        B = Point()
        B.read()
        print("Điểm B:", B)
        C = Point(-B.getX(), -B.getY())
        print("Điểm C:", C)
        print(B.distance())
        print(B.distance(A))

# PointTest.main()

