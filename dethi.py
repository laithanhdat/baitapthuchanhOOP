import math
import sys
from operator import itemgetter
from operator import attrgetter
import pickle

class TuLanh: 
    __nhanhieu = str 
    __maso = str 
    __nuocsx = str 
    __tkdien = bool
    __dungtich = int
    __gia = int

    def __init__(self, nhanhieu = "Electrolux", maso = "UNKNOWN", nuocsx = "Vietnam", tkdien = True, dungtich = 256, gia = 7000000):
        self.__nhanhieu = nhanhieu
        self.__maso = maso 
        self.__nuocsx = nuocsx
        if tkdien == True:
            self.__tkdien="Yes"
        else:
            self.__tkdien = "No"
        self.__dungtich = dungtich 
        self.__gia = gia
    
    def nhapThongTin(self): 
        try: 
            self.__nhanhieu = str(input())
            self.__maso = str(input())
            self.__nuocsx = str(input())
            self.__tkdien = bool(input())
            self.__dungtich = int(input())
            self.__gia = int(input())
            print("\n")
        except ValueError: 
            print("Wrong value, please try again!!!")
            sys.exit()

    def makeCopy(self, *args): #try copy.deepcopy later
            if len(args) == 1 and isinstance(args[0], TuLanh):
                self.__nhanhieu = args[0].__nhanhieu
                self.__maso = args[0].__maso 
                self.__nuocsx = args[0].__nuocsx
                self.__tkdien= args[0].__tkdien
                self.__dungtich = args[0].__dungtich
                self.__gia = args[0].__gia
    
    def __str__(self): 
        return f"Nhan Hieu: {self.__nhanhieu}\nMa so: {self.__maso}\nNuoc san xuat: {self.__nuocsx}\nTiet kiem dien: {self.__tkdien}\nDung tich: {self.__dungtich}\nGia: {self.__gia}\n \n"
    
    def hienThi(self): 
        print (f"Nhan Hieu: {self.__nhanhieu}\nMa so: {self.__maso}\nNuoc san xuat: {self.__nuocsx}\nTiet kiem dien: {self.__tkdien}\nDung tich: {self.__dungtich}\nGia: {self.__gia}\n \n")

    def layNhanHieu(self): 
        return self.__nhanhieu
    
    def get_gia(self):
        return self.__gia
    
    @classmethod
    def layGia(self): 
        return self.__gia
    
    def soNguoiSD(self): 
        return math.floor(self.__dungtich/100)
    
    def cungNhanHieu(self, args):
        try: 
            if isinstance(args, TuLanh):
                if self.__nhanhieu == args.layNhanHieu(): 
                    print(f"Tu lanh {args} co cung nhan hieu!")
                else: 
                    print(f"Tu lanh {args} khong cung nhan hieu!")    
        except ValueError:  
            print("Day khong phai la tu lanh!!!")
            sys.exit()
            

    def nhHon(self, args): 
        try: 
            if isinstance(args, TuLanh):
                if self.__dungtich < args.__dungtich: 
                    return True
                else: 
                    return False  
        except args != TuLanh:  
            print("Day khong phai la tu lanh!!!")
            sys.exit()
        

class C002454(TuLanh): 
    def testCase1(): 
        tl1 = TuLanh()
        tl1.nhapThongTin()
        tl2 = TuLanh("LG", "LG-28382", "Han Quoc", True, 600, 43000000)
        tl2.hienThi()
        tl3 = TuLanh()
        tl3.makeCopy(tl1)
        tl3.hienThi()
        
    def testCase2(): 
        n = int(input("Nhap so tu lanh: "))
        while n <= 0 and n >= 100: 
            n = int(input("Qua so luong. Nhap lai so luong: "))
        print(n)
        danhsach = []
        for i in range(n): 
            i = TuLanh()
            i.nhapThongTin()
            danhsach.append(i)
        
        danhsach.reverse()

        for i in danhsach:
            print(i)
        
    def testCase3():
        n = int(input("Nhap so tu lanh: "))
        while n <= 0 and n >= 100: 
            n = int(input("Qua so luong. Nhap lai so luong: "))
        print(n)

        danhsach = []
        
        for i in range(n): 
            i = TuLanh()
            i.nhapThongTin()
            danhsach.append(i)
        
        danhsach.sort(key= lambda x: x.get_gia(), reverse= True)   

        for i in danhsach:
            print(i)
    
    def testCase4(): 
        n = int(input("Nhap so tu lanh: "))
        while n <= 0 and n >= 100: 
            n = int(input("Qua so luong. Nhap lai so luong: "))
        print(n)
        danhsach = []
        for i in range(n): 
            i = TuLanh()
            i.nhapThongTin()
            danhsach.append(i)

        with open('DsTuLanh.json', 'wb') as f: 
            for i in danhsach: 
                pickle.dump(i, f)
    
        with open('DsTuLanh.json', 'rb') as f: 
            for i in danhsach: 
                i = pickle.load(f)
                print(i)

    def testCase5(): 
        n = int(input("Nhap so tu lanh: "))
        while n <= 0 and n >= 100: 
            n = int(input("Qua so luong. Nhap lai so luong: "))
        print(n)
        danhsach = []
        for i in range(n): 
            i = TuLanh()
            i.nhapThongTin()
            danhsach.append(i)

        x = 0 
        y = 0
        z = 0 
        for i in danhsach: 
            if i.layNhanHieu() == "LG": 
                x = x +  1  
            elif i.layNhanHieu() == "Panasonic":
                y = y + 1
            elif i.layNhanHieu() == "Sharp":
                z= z + 1   
        # Try cungNhanHieu() function later
        
        print(f"LG: ({x})")                
        print(f"Panasonic: ({y})")  
        print(f"Sharp: ({z})")  


# C002454.testCase1() \succeeded\
# C002454.testCase2() \succeeded\
# C002454.testCase3() \succeeded\
# C002454.testCase4() \succeded\
# C002454.testCase5() \succeeded\





