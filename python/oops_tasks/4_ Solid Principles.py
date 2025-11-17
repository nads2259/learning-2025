# Single Responsibility

class Restaurant():
    pass

class Kitchen:
    
    def cook(self):
        pass
    
class CustomerService:
    
    def takeFeedback(self):
        pass
    def serveFood(self):
        pass
    
class Inventory:
    
    def orderIngredients(self):
        pass
    def expenses(self):
        pass
    def decor(self):
        pass
    
    
# O / C Principle

class Cricketer:
    
    def role(self,type):
        if type == "Batsman":
            print("Batting")
        elif type == "Bowler":
            print("Bowling")
        elif type == "All rounder":
            print("Both")

# ___________________

class Cricketer:
    
    def role(self,type):
        pass
    
class Batsman(Cricketer):
    
    def role(self):
        print("Batting")
        
        
class Bowler(Cricketer):
    
    def role(self):
        print("Bowling")

class All_Rounder(Cricketer):
    
    def role(self):
        print("Both")
    
    




# LISKOV SUBSTITUTION


class Payment:
    
    def pay(self,amount):
        pass
    def refund(self,amount):
        pass
    
class CryptoPayment(Payment):
    def refund(self,amount):
        print("No refunds allowed in this type")
        
# _______


class Payment:
    def pay(self,amount):
        pass
    
class RefundablePayment:
    def pay(self,amount):
        pass
    def refund(self,amount):
        pass
    
class CryptoPayment(Payment):
    pass

            
    
    
    
    
# INTERFACE SEGREGATION

class SocialMedia:
    
    def post(self):
        pass
    def message(self):
        pass
    def raiseFunds(self):
        pass
    def collab(self):
        pass
    

class SimpleUser(SocialMedia):
    def post(self):
        pass
    
    # Doesnt need rest of the functions
    
    
    
class Poster:
    def post(self):
        pass
    
class Messenger:
    def message(self):
        pass
    
class FundRaiser:
    def raiseFunds(self):
        pass
    
class Collab:
    def collab(self):
        pass
    

class SimpleUser(Poster,Messenger):
    pass

class ContentCreator(Poster,Messenger,FundRaiser,Collab):
    pass


# DEPENDENCY INVERSION

class Lamp:
    
    def turn_on(self):
        print("Lamp is on")
        

class Switch:

    def on(self):
        lamp = Lamp() # Only tied to lamp not other devices
        lamp.turn_on()
        
# switch = Switch()
# switch.on()


# ______


class Device:
    
    def turn_on(self):
        pass
    
class Lamp(Device):
    
    def turn_on(self):
        print("Lamp is on")
    
class Fan(Device):
    
    def turn_on(self):
        print("Fan is on")
    
class AC(Device):
    
    def turn_on(self):
        print("AC is on")
        
class Switch:
    
    def __init__(self,device : Device):
        self.device = device
    
    def on(self):
        self.device.turn_on()
        
    
switch = Switch(Lamp())
switch.on()

switch_2 = Switch(AC())
switch_2.on()
    
        
    