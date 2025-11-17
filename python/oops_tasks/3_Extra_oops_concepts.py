# ACCESS MODIFIERS

# -- Do not work in python only used for caution to users

class Car:
    
    def __init__(self):
        self.type = "Kawasaki" # Public
        self._model = "H2" # Protected
        self.__engine = "1000cc" # Private
        

# METHOD OVERRIDING

class GameCharacter:
    
    def attack(self):
        print("Game character attacks with hands")
        
class Wizard(GameCharacter):
    
    def attack(self):
        print("Wizard casts a spell")
    
wiz = Wizard()
wiz.attack()


# SUPER() and __INIT__()

# To call the constructor of parent class and also define the methods in them

class Parent:
    def __init__(self):
        print("I am the parent")
        
        
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("I am the child")
        
c = Child()

# Static Method

class Math:
    
    @staticmethod
    def add(a,b):
        print(a + b)
        
    @staticmethod
    def sub(a,b):
        print(a - b)
        
    @staticmethod
    def mul(a,b):
        print(a * b)
        
    @staticmethod
    def div(a,b):
        print(a // b)
        
        
a = Math()
a.add(5,2)
a.sub(5,2)
a.mul(5,2)
a.div(5,2)



# CLASS METHOD

class Student:
    counter = 0
    
    def __init__(self):
        Student.counter += 1
        
    @classmethod
    def objectCount(cls):
        print(cls.counter)
        

s1 = Student()
s2 = Student()
s3 = Student()

Student.objectCount()

# ABSTRACT CLASS

from abc import ABC, abstractmethod

class Payment(ABC):
    
    @abstractmethod
    def pay(self,amount):
        pass
    
class UPI(Payment):
    
    def pay(self,amount):
        print(f"Paid {amount} thru UPI")
        
class Crypto(Payment):
    
    def pay(self,amount):
        print(f"Paid {amount} thru Crypto")

upi = UPI()
upi.pay(300)

crypto = Crypto()
crypto.pay(500)
