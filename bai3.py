import math

class Point: 
    __x = int 
    __y = int

    def __init__(self, x = 0, y = 1): 
        self.x = x
        self.y = y
    
    def read(self, x, y): 
        try: 
            self.__x = x 
            self.__y = y
        except TypeError: 
            print("You typed in wrong variable format.")
            return
    
    def print(self): 
        print(f"({self.__x}, {self.__y})")

    def move(self, dx = int, dy = int):
        self.__x += dx
        self.__y += dy
        print("The new coordinates is: ({self.__x}, {self.__y})")

    def getX(self): 
        return self.__x

    def getY(self): 
        return self.__y

    def setXY(self, x, y): 
        self.__x = x
        self.__y = y

    def distance(self, *args):
        args = Point
        if len(args) == 0:
            return math.sqrt(self.__x**2 + self.__y**2)
        
        elif len(args) == 1: 
            return math.sqrt((self.__x - args.__x)**2 - (self.__y - args.__y)**2)
        
        else:
            print("Wrong format")
            exit(None)
    
class ColorPoint(Point):
    __color = str 

    def __init__(self,*args): 
        if len(args) == 0: 
            self.__color = "Blue"

        elif len(args) == 3:
            self.__x = int(args[0])
            self.__y = int(args[1])
            self.__color = args[2]
        
        elif len(args) == 1:
            self = copy.deepcopy(args[0])

    def read(self): 
        super().read()
        self.__color = input("Enter the color")

    def __str__(self):
        return f"{super().__str__+}: {self.__color}"
    
    def  setColor(self, color): 
        self.__color = color


class C002454: 
    def testCase1(self): 
        A = ColorPoint(5, 10, "White")
        print(A)

    def testCase2(self): 
        B = ColorPoint()
        B.read()
        print(B)
        B.move()
        print(B)

    def testCase3(self): 
        C = ColorPoint(6, 3, "Black")
        D = ColorPoint(C)
        # D = copy.deepcopy(C)
        print(D)
        D.setColor("Yello")
        print(D)
        print(C)

C002454().testCase1()