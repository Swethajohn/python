class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=3.14*self.radius**2
        print("area of the circle:",area)
        
    def circum(self,):
        circum=2*3.14*self.radius
        print("circum of the circle:",circum)

area=int(input("enter the radius of the circle:"))
c=Circle(area)
while True:
    print("1.area \n 2.circumference \n 3. exit \n")
    choice=int(input("enter the choice:"))
    if choice==1:
        c.area()
    elif choice==2:
        c.circum()
    elif choice==3:
        break
    else:
        print("invalid")