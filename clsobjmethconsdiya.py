# class Student:
#     name="pooja"
#     age=21

# student1=Student()
# print(student1.name)
# print(student1.age)

#method

# class Student:
#     def study(self):
#         print("student is studying")
# student1 =Student()
# student1.study()


#constructors

# class Student():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def study(self):
#         print(self.name,"is studying")

# student1= Student("pooja",21)
# student2=Student("diya",22)
# student3=Student("mariyam",21)
# print(student1.name)
# print(student1.age)
        
# print(student2.name)
# print(student2.age)


# print(student3.name)
# print(student3.age)
        



# class Student():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def study(self):
#         print(self.name,"is studying")

#     def display(self):
#         print("name: ",self.name)
#         print("age: ",self.age)

# student1= Student("pooja",21)
# student2=Student("diya",22)
# student3=Student("mariyam",21)

# student1.display()
# student1.study()

# print()
# student2.display()
# student2.study()
# print()
# student3.display()
# student3.study()







# INHERITANCE

# SINGLE INHERITANCE

# class Animal:
#     def bark(self):
#         print("animal is eating")

# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# d= Dog()

# d.eat()
# d.bark()





#  MULTIPLE INHERITANCE


# class Father:
#     def driving(self):
#         print("driving")

# class Mother:
#     def cooking(self):
#         print("cooking")

# class Child(Father,Mother):
#     pass

# c=Child()
# c.driving()
# c.cooking()


# MULTILEVEL INHERITANCE


# class Grandfather:
#     def house(self):
#         print("Grandfather has a house")

# class Father(Grandfather):
#     pass
# class Son(Father):
#     pass

# s=Son()
# s.house()



# HIERARCHICAL INHERITANCE

# class Animal:
#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# class cat(Animal):
#     def meow(self):
#         print("cat is meowing")

# d= Dog()
# c=cat()


# d.eat()
# d.bark()

# c.eat()
# c.meow()




# HYBRID INHERITANCE


# class A:
#     def show_a(self):
#         print("A")
# class B(A):
#     def show_b(self):
#         print("B")

# class C(A):
#     def show_c(self):
#         print("C")

# class D(B,C):
#     def show_d(self):
#         print("D")

# d =D()

# d.show_a()
# d.show_b()
# d.show_c()
# d.show_d()



#  Encapsulation

# class Student:
#     def __init__(self):
#         self.__marks =90

#     def get_marks(self):
#        return self.__marks

# s =Student()

# print(s.get_marks())


# class Student:

#     def __init__(self, mark):
#         self.__mark = mark

#     def get_mark(self):
#         return self.__mark

#     def set_mark(self, mark):
#         self.__mark = mark

# student = Student(90)
# print(student.get_mark())
# student.set_mark(95)
# print(student.get_mark())














  # POLYMORPHISM

#   Polymorphism എന്നത് “one name, many forms” എന്നാണ്.

# അതായത്, same method/function name different objects-il different രീതിയിൽ work ചെയ്യുന്നത്.
# Example
# Nammukku sound() enna oru action undennu karuthuka.
# Dog → Bow 
# Cat → Meow
# Ellavarum sound undakkunnu.
# But sound different aanu. Athaanu Polymorphism.
# Same method → Different output

#example pgm

# class Dog:
#     def action(self):
#         print("Dog is running")


# class Cat:
#     def action(self):
#         print("Cat is jumping")


# dog = Dog()
# cat = Cat()

# dog.action()
# cat.action()


# TYPES
# 1)Method Overloading
# 2)Method Overriding
# 3)Operator Overloading
# 4)Duck Typing


# 1)Method Overloading


#Same method name + different arguments = Method Overloading

# ഒരു method-ന് ഒരേ പേര് ആയിരിക്കും. പക്ഷേ അതിലേക്ക് different number of inputs കൊടുത്താൽ,
# അതനുസരിച്ച് method work ചെയ്യുന്നതാണ് Method Overloading.

# Python-ൽ ഒരേ പേരിലുള്ള method-നെ different number of arguments ഉപയോഗിച്ച്
# പലതവണ define ചെയ്യാൻ പറ്റില്ല. അതുകൊണ്ട് method overloading ചെയ്യാൻ Python-ൽ
# സാധാരണയായി default arguments അല്ലെങ്കിൽ *args ഉപയോഗിക്കുന്നു.

# class Calculator:

#     def add(self, *numbers):
#         return sum(numbers)


# c = Calculator()

# print(c.add(10, 20))
# print(c.add(10, 20, 30))
# print(c.add(10, 20, 30, 40))







# 2)Method Overriding

# Parent class-ൽ ഉള്ള method same name-ൽ child class വീണ്ടും define ചെയ്യുമ്പോൾ
#  അതിനെ Method Overriding എന്ന് പറയുന്നു

# class Payment:

#     def pay(self):
#         print("Payment")


# class UPI(Payment):

#     def pay(self):
#         print("Payment using UPI")


# class Card(Payment):

#     def pay(self):
#         print("Payment using Card")


# p1 = UPI()
# p2 = Card()

# p1.pay()
# p2.pay()



# 3) Operator Overloading


# Operator Overloading എന്നത് ഒരേ operator-നെ different objects-ൽ 
# different രീതിയിൽ ഉപയോഗിക്കുന്നതാണ്

# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return self.value + other.value


# num1 = Number(10)
# num2 = Number(20)

# print(num1 + num2)




# class Product:
#     def __init__(self, name):
#         self.name = name

#     def __eq__(self, other):
#         return self.name == other.name


# p1 = Product("Pen")
# p2 = Product("Pen")

# print(p1 == p2)



# 4) Duck Typing

# “Object ഏത് class-ലാണ് എന്നത് നോക്കില്ല.
# അതിൽ നമുക്ക് വേണ്ട method ഉണ്ടെങ്കിൽ അത് ഉപയോഗിക്കും. ഇതാണ് Duck Typing.”

# Car ആണോ Bike ആണോ എന്നത് നോക്കേണ്ടതില്ല.
# രണ്ടിലും start() method ഉണ്ടെങ്കിൽ start() call ചെയ്യാം.

# Class നോക്കില്ല → Method ഉണ്ടോ എന്ന് നോക്കും → ഉണ്ടെങ്കിൽ ഉപയോഗിക്കും

class Car:
    def start(self):
        print("Car is starting")


class Bike:
    def start(self):
        print("Bike is starting")





car = Car()
bike = Bike()

def start_vehicle(vehicle):
    vehicle.start()

start_vehicle(car)
start_vehicle(bike)







#  DATA ABSTRACTION

# Data Abstraction എന്ന് പറഞ്ഞാൽ, ആവശ്യമുള്ള information മാത്രം user-ന് കാണിച്ച്,
# ഉള്ളിലെ complicated details hide cheyyunna concept ആണ്

# Real-life Example

# നമ്മൾ ATM ഉപയോഗിക്കുമ്പോൾ:

# PIN enter ചെയ്യുന്നു
# Amount enter ചെയ്യുന്നു
# Cash കിട്ടുന്നു

# പക്ഷേ, ATM-ന്റെ ഉള്ളിൽ എങ്ങനെ transaction നടക്കുന്നു, bank server-ലേക്ക് എങ്ങനെ request പോകുന്നു
# എന്നൊന്നും നമ്മൾ കാണുന്നില്ല.ഇതാണ് Abstraction.


# 1. Abstract Class

# ഒരു parent class പോലെ കരുതാം.
# അതിൽ child classes-ന് follow ചെയ്യേണ്ട rules / methods കൊടുക്കുന്നു

# 2. Abstract Method

# Method എന്ത് ചെയ്യണം എന്ന് define ചെയ്യുന്നു, 
# പക്ഷേ അതിന്റെ actual implementation child class-ൽ നൽകുന്നു






from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):

    def pay(self):
        print("Payment using UPI")


payment = UPI()
payment.pay()






