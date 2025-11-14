# class Car:
    
#     def __init__(self,model,color):
#         self.__model = model
#         self.__color = color
    
#     def drive(self):
#         print(f"A {self.__color} {self.__model} is driving")
        

# lambo = Car("Lambo Hurrican","Orange")


# lambo.drive()

# lambo.__model = "Audi"

# lambo.drive()
        
        
# ____ ABSTRACTION

# class BurgerMachine:
    
#     def __init__(self,type):
#         self.__type = type
        
#     def makeBurger(self):
#         self.__addPatty()
#         self.__addVeggies()
#         self.__addMayo()
        
#         print(f"Your {self.__type} burger is ready")
        
#     def __addPatty(self):
#         print("Patty added")
        
#     def __addVeggies(self):
#         print("Veggies added")
        
#     def __addMayo(self):
#         print("Mayo added")
        
# chickenBurger = BurgerMachine("Chicken")
# chickenBurger.makeBurger()

# paneerBurger = BurgerMachine("Paneer")
# paneerBurger.makeBurger()


## INHERITANCE

class Animal:
    
    def __init__(self):
        pass
    
    def introduce(self):
        print("I am an animal")
        
class Fish(Animal):
    
    def __init__(self):
       pass
   
    def introduce(self):
        print("i am a water animal")
        
class Dog(Animal):
    
    def __init__(self):
       pass
   
    def introduce(self):
        print("I am a land animal")
        

fish_1 = Fish()
fish_1.introduce()

dog_1 = Dog()
dog_1.introduce()
    