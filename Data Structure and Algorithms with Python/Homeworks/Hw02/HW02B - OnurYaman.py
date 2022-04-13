from abc import abstractmethod
from math import pi
class point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        if float(self.x)-int(self.x)==0:self.x=int(self.x)
        else:self.x=round(float(self.x),2)
        if float(self.y)-int(self.y)==0:self.y=int(self.y)
        else:self.y=round(float(self.y),2)
        if float(self.x)-int(self.x)==0 and float(self.y)-int(self.y)==0:
            return "("+str(self.x)+","+str(self.y)+")"
        else:return "("+"{:.2f}".format(self.x)+","+"{:.2f}".format(self.y)+")"
class shape():
    def __init__(self,x,y):
        self.givenLeftTop=point(x,y)
        self.pointsList=[]
    @abstractmethod
    def calculatePoints(self):
        pass
    @abstractmethod
    def calculateArea(self):
        pass
    @abstractmethod
    def calculatePerimeter(self):
        pass
    @abstractmethod
    def move(self,new_x,new_y):
        pass
class rectangle(shape):
    def __init__(self,x,y,h,w):
        shape.__init__(self,x,y)
        self.leftTop=self.givenLeftTop
        self.w=w
        self.h=h
    def calculatePoints(self):
        self.pointsList.append(self.leftTop)
        rigthTop=point(self.leftTop.x+self.w,self.leftTop.y)
        self.pointsList.append(rigthTop)
        rigthBottom=point(self.leftTop.x+self.w,self.leftTop.y+self.h)
        self.pointsList.append(rigthBottom)
        leftBottom=point(self.leftTop.x,self.leftTop.y+self.h)
        self.pointsList.append(leftBottom)
        return self.pointsList
    def calculateArea(self):
        return self.h*self.w
    def calculatePerimeter(self):
        return 2*(self.w+self.h)
    def move(self,new_x,new_y):
        self.leftTop=point(new_x,new_y)
class circle(shape):
    def __init__(self,x,y,r):
        shape.__init__(self,x,y)
        self.leftTop = self.givenLeftTop
        self.r=r
    def calculatePoints(self):
        self.pointsList.append(self.leftTop)
        rigthBottom=point(self.leftTop.x+2*self.r,self.leftTop.y+2*self.r)
        self.pointsList.append(rigthBottom)
        return self.pointsList
    def calculateArea(self):
        return pi*self.r**2
    def calculatePerimeter(self):
        return 2*pi*self.r
    def move(self,new_x,new_y):
        self.leftTop=point(new_x,new_y)
def test(givenShape):
    def do_print_for_rec(obj):
        print("--Rectangle--")
        if float(obj.h)-int(obj.h)==0:print("Heigth:",int(obj.h))
        else:print("Heigth:","{:.2f}".format(float(obj.h)))
        if float(obj.w)-int(obj.w)==0:print("Width:",int(obj.w))
        else:print("width:","{:.2f}".format(float(obj.w)))
        print("Left Top Point:", obj.leftTop)
        print("Area:", "{:.2f}".format(obj.calculateArea()))
        print("Perimeter:", "{:.2f}".format(obj.calculatePerimeter()))
        points = obj.calculatePoints()
        print("Points:", points[0], points[1], points[2], points[3])
        points.clear()
    def do_print_for_cir(obj):
        print("--Circle--")
        if float(obj.r)-int(obj.r)==0:print("Radius:",int(obj.r))
        else:print("Radius","{:.2f}".format(float(obj.r)))
        print("Left Top Point:",obj.leftTop)
        print("Area:","{:.2f}".format(obj.calculateArea()))
        print("Perimeter","{:.2f}".format(obj.calculatePerimeter()))
        points=obj.calculatePoints()
        print("Points:",points[0],points[1])
        points.clear()
    if givenShape=="r":
        inputs=str(input("Coordinate (leftTop), height and width: ")).split(" ")
        x=float(inputs[0])
        y=float(inputs[1])
        h=float(inputs[2])
        w=float(inputs[3])
        obj=rectangle(x, y, h, w)
        do_print_for_rec(obj)
        new_inputs=str(input("Move object to the new coordinate (leftTop): ")).split(" ")
        new_x=float(new_inputs[0])
        new_y=float(new_inputs[1])
        obj.move(new_x,new_y)
        do_print_for_rec(obj)
    elif givenShape=="c":
        inputs=str(input("Coordinates (leftTop) and radius: ")).split(" ")
        x=float(inputs[0])
        y=float(inputs[1])
        radius=float(inputs[2])
        obj=circle(x,y,radius)
        do_print_for_cir(obj)
        new_inputs=str(input("Move object to the new coordinate (leftTop): ")).split(" ")
        new_x=float(new_inputs[0])
        new_y=float(new_inputs[1])
        obj.move(new_x,new_y)
        do_print_for_cir(obj)
    elif givenShape=="q":
        exit()
    else:print("This is wrong input please enter r,c or q in this step")
firstInput=input("Type of Shape (q for exit ): ")
try:
    while firstInput!="q":
        test(firstInput)
        firstInput=input("Type of Shape (q for exit): ")
except:
    print("This is invalid input please enter inputs as int space int etc\n"
          "for example 100 100 10 in one row.Now please run program again")