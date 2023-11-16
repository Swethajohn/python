# class Animal:
#     def speak(self):
#         print("animal speaking")
# class Lion(Animal):
#     def roar(self):
#         print("Lion roaring")
# d=Lion()
# d.roar()
# d.speak()


# class cal1:
#     def addition(self,x,y):
#         return x+y
# class cal2:
#     def multiplication(self,x,y):
#         return x*y
# class derived(cal1,cal2):
#     def division(self,a,b):
#         return a/b
# d=derived()class Shape():
#     def area(self):
#         print()
# class rectangle(Shape):
#     def arearectangle(self,l,b):
#         return l*b
# class circle(Shape):
#     def areaCircle(self,r):
#         return 3.14*r**2
# d=rectangle()
# print(d.arearectangle(10,5))
# c=circle()
# print(c.areaCircle(6))
# print(d.addition(2,4))
# print(d.multiplication(2,4))
# print(d.division(2,4))


# class animal():
#     def speak(self):
#         print("animal speaking")
# class Lion(animal):
#     def roar(self):
#         print("lion roaring")
# class babyLion(Lion):
#     def eat(self):
#         print("eating meat..")
# d=babyLion()
# d.roar()
# d.speak()
# d.eat()


# class Shape():
#     def area(self):
#         print()
# class rectangle(Shape):
#     def arearectangle(self,l,b):
#         return l*b
# class circle(Shape):
#     def areaCircle(self,r):
#         return 3.14*r**2
# d=rectangle()
# print(d.arearectangle(10,5))
# c=circle()
# print(c.areaCircle(6))


# class Shape():
#     def __init__(self,area):
#         self.a=area
#     def area(self):
#         print(self.a)
# class rectangle(Shape):
#     def areaRectangle(self,l,b):
#         self.a=l*b
# class circle(Shape):
#     def areaCircle(self,r):
#         self.a=3.14*r**2
# d=rectangle()
# print(d.areaRectangle(10,5))
# c=circle()
# print(c.areaCircle(6))


# class Animal():
#     def speak(self):
#         print("animal speaking")
# class Dog(Animal):
#     def bow(self):
#         super().speak()
#         print("dog bark's")
# class Cat(Animal):
#     def meow(self):
#         super().speak()
#         print("cat meows")
# class Cow(Animal):
#     def moo(self):
#         super().speak()
#         print("cow moo's")
# m=Cow()
# m.moo()
# c=Cat()
# c.meow()
# d=Dog()
# d.bow()


# class Car():
#     def start_engine(self):
#         print("engine started")
# class ElectricCar(Car):
#     def start_engine(self):
#         super().start_engine()
#         print("electicCar engine starts")
# class GasolinCar(Car):
#     def start_engine(self):
#         super().start_engine()
#         print("GasolinCar engine starts")
# g=GasolinCar()
# g.start_engine()
# e=ElectricCar()
# e.start_engine()


# class Employee():
#     def __init__(self,salary):
#         self.t=salary

#     def calculate_salary(self):
#         days=int(input("enter the days worked:"))
#         ta=100*days
#         da=200*days
#         bonus=2000
#         self.t=ta+da+bonus
# class Manager(Employee):
#     def salary(self):
#         super().calculate_salary()
#         basicSalary=100000
#         self.t+=basicSalary
#         print("total salary:",self.t)
# class Developer(Employee):
#     def salary(self):
#         super().calculate_salary()
#         basicSalary=50000
#         self.t+=basicSalary
#         print("total salary:",self.t)

# while True:
#     choice=int(input("1. manager 2. developer 3. exit"))
#     if choice==1:
#         obj1=Manager(0)
#         obj1.salary()
#     if choice==2:
#         obj2=Developer(0)
#         obj2.salary()
#     if choice==3:
#         break



