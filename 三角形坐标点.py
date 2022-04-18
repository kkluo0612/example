#-*- coding: utf8 -*-
#首先判断是否是三角形
import math

from regex import B

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

# corA = input("请输入A点的坐标值:").split(",")
# x1,y1 = corA[0],corA[1]

# corB = input("请输入B点的坐标值:").split(",")
# x2,y2 = corB[0],corB[1]

# corC = input("请输入C点的坐标值:").split(",")
# x3,y3 = corC[0],corC[1]

# corP = input("请输入P点的坐标值:").split(",")
# x,y = corP[0],corP[1]

def IsTrangleOrArea(x1,y1,x2,y2,x3,y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

def product(A,B,p):
    return (A.x-p.x)*(B.y-p.y)-(A.y-p.y)*(B.x-p.x)

def IsInside1(x1,y1,x2,y2,x3,y3,x,y):

    #三角形ABC的面积
    ABC = IsTrangleOrArea(x1,y1,x2,y2,x3,y3)

    # 三角形PBC的面积
    PBC = IsTrangleOrArea(x,y,x2,y2,x3,y3)

    # 三角形ABC的面积
    PAC = IsTrangleOrArea(x1,y1,x,y,x3,y3)

    # 三角形ABC的面积
    PAB = IsTrangleOrArea(x1,y1,x2,y2,x,y)

    return (ABC == PBC + PAC + PAB)


def isInside2(A,B,C,p):
    if (product(A,B,p)>=0 and product(B,C,p)>=0 and product(C,A,p)>=0):
        return True
    return False



if __name__ =="__main__":
#if IsInside(10, 30, 20, 0, 10, 30, 10, 15):
    A=Point(1,1)
    B=Point(2,1)
    C=Point(2,3)
    p=Point(1.5,1.5)
    print(isInside2(A,B,C,p))

    # p=Point(1.5,1.5)
    # if IsInside1(x1,y1,x2,y2,x3,y3,x,y):
    #     print("Inside")
    # else:
    #     print("Outside")