#Expriment No. - 06
#Title - Program to calculate volume,diameter and circumference of sphere using class.
#Class - SY CSE
#Name -Sumedh Gajanan Kamble
#Roll No. -2005
#Subject - Python Programming

class A:
    def volume(self,r):
        v=(4/3)*(3.14*r*r*r)
        print("volume of sphere is {}".format(v))
    def dia(self,r):
        d=2*r
        print("Diameter of sphere is{}".format(d))
    def circumference(self,r):
        c=2*3.14*r
        print("Circumference of sphere is {}".format(c))
obj=A()
r=int(input("Enter radius of sphere"))
obj.volume(r)
obj.dia(r)
obj.circumference(r)