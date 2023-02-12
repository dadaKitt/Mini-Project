import json
import math
import os
def __main__():
    while 1:
        print("---------------------------")
        print("| Select your number      |")
        print("| [1].Math Calculator     |")
        print("| [2].Physic Calculator   |")
        print("| [3].Chemical Calculator |")
        print("---------------------------")
        selectNum = int(input("=> : "))
        if selectNum == 1:
            mathCal()
        elif selectNum == 2:
            physicCal()
        elif selectNum == 3:
            chemiCal()
        return False

def mathCal():
    print("------------------------------")
    print("| Select your number         |")
    print("| [1].Math Calculator        |")
    print("| [2].Multiply Table         |")
    print("| [3].Matrix Calculator      |")
    print("| [4].Area Calculator        |")
    print("------------------------------")
    selectnum = int(input("=> : "))
    if selectnum == 1:
      # Author Bongkotphetr
        def calCulate():
          x = input("ป้อนตัวเลขที่ 1: ")
          y = input("ป้อนตัวเลขที่ 2: ")

          x = float(x)
          y = float(y)

          sum = x + y
          minus = x - y
          multiply = x * y
          divide = x / y

          print("ผลบวก =", sum)
          print("ผลลบ =", minus)
          print("ผลคูณ =", multiply)
          print("ผลหาร =", divide)
        calCulate()
    elif selectnum == 2:
        def multiTb():
            num = int(input("Input your number => : "))
            for i in range(1,13):
                print(num, "x" , i , "= " , num*i)     
        multiTb()
    elif selectnum == 3:
        def matrixCal():
            rows = int(input("ป้อนจำนวนแถว: "))
            cols = int(input("ป้อนจำนวนหลัก: "))

            print("Matrix ขนาด",rows,"x",cols)
            matrix1 = []
            print("ค่าสำหรับ Matrix ที่ 1")
            for i in range(rows):
                row = []
                for j in range(cols):
                    val = int(input("ป้อนค่าแถว {0} , หลัก {1}: ".format(i+1, j+1)))
                    row.append(val)
                matrix1.append(row)

            matrix2 = []
            print("ค่าสำหรับ Matrix ที่ 2")
            for i in range(rows):
                row = []
                for j in range(cols):
                    val = int(input("ป้อนค่าแถว {0} , หลัก {1}: ".format(i+1, j+1)))
                    row.append(val)
                matrix2.append(row)

            op = input("ป้อนการคำนวณ (+, -, หรือ *): ")

            result = []
            if op == "+":
                for i in range(rows):
                    row = []
                    for j in range(cols):
                        row.append(matrix1[i][j] + matrix2[i][j])
                    result.append(row)
            elif op == "-":
                for i in range(rows):
                    row = []
                    for j in range(cols):
                        row.append(matrix1[i][j] - matrix2[i][j])
                    result.append(row)
            elif op == "*":
                for i in range(rows):
                    row = []
                    for j in range(cols):
                        val = 0
                        for k in range(cols):
                            val += matrix1[i][k] * matrix2[k][j]
                        row.append(val)
                    result.append(row)

            print("ผลลัพธ์:")
            for row in result:
                print(row)
        matrixCal()
    elif selectnum == 4:
      def areaCal():

        print("Area Calculator")
        print("1. สามเหลี่ยม")
        print("2. วงกลม")
        print("3. สี่เหลี่ยม")

        choice = int(input("เลือกหาพื้นที่ของรูปทรงหมายเลข: "))

        if choice == 1:
            base = float(input("ป้อนความยาวฐาน: "))
            height = float(input("ป้อนความสูง: "))
            area = 0.5 * base * height
            print("พื้นที่ของสามเหลี่ยม = ", area)

        elif choice == 2:
            radius = float(input("ป้อนความยาวรัศมี: "))
            area = math.pi * radius ** 2
            print("พื้นที่ของวงกลม = ", area)

        elif choice == 3:
            length = float(input("ป้อนความยาวด้าน: "))
            width = float(input("ป้อนความกว้าง: "))
            area = length * width
            print("พื้นที่ของสี่เหลี่ยม = ", area)

        else:
            print("เลือกหมายเลขไม่ถูกต้อง")
      areaCal()

    return False

def physicCal():
    while 1:
        print("-------------------------")
        print("| Select your number    |")
        print("| [1].Force Calculator  |")
        print("| [2].Speed Calculator  |")
        print("-------------------------")
        select = int(input("=> : "))
        if select == 1:
            def forceCal():
                f = m*a
                print("Result for force count is : ", f , "N")
                return False
            m = int(input("Enter your mass: "))
            a = int(input("Enter your acceleration: "))
            forceCal()
        elif select == 2:
            def speedCal():
                time = sspeed/km
                print("Result for time is : ", time , "Minute")
            sspeed = int(input("Enter your speed (Km/h): "))
            km = int(input("Enter your distance (Km): "))
            speedCal()
        return False

    
def chemiCal():
    while 1:
        print("-------------------------")
        print("| Select your number    |")
        print("| [1].Periodic Table    |")
        print("-------------------------")
        select = int(input("=> : "))
        if select == 1:
          
          def periodic():
            print('''            Periodic Table of Elements
                  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
                1 H                                                  He
                2 Li Be                               B  C  N  O  F  Ne
                3 Na Mg                               Al Si P  S  Cl Ar
                4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
                    5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
                    6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
                    7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og
            
                        Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
                        Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr''')
          return False
        periodic()


# Run 
__main__()
