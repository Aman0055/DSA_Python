"""
5. Explain the four pillars of OOP (Encapsulation, Abstraction, Inheritance, Polymorphism) 
with one real-life example each.
"""

from abc import ABC , abstractmethod    # for initialising the abstract class methods 

class Oops_fundamental:

    def __init__(self):
        return "Welcome to the Oops fundamental hierarchy !! "

    def Oops_operation(self,choice):
        self.choice = choice
        if self.choice == "1":
            return Encapsulation()
        elif self.choice == "2":
            return Polymorphism()
        elif self.choice == "3":
            return Car()
        elif self.choice == "4":
            return Abstract_Class_Implementation()
        else :
            return "Invalid choice !!"

class Encapsulation:

    def __init__(self):
        print("Welcome Encapsulation property !!")
        

    def encapsulation(self, id, name, address, password):
        self.id = id
        self.name = name 
        self.address = address
        self.password = password

    def set_id(self,id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_address(self,address):
        self.address = address

    def set_password(self,password):
        self.password = password

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_password(self):
        return self.password

class Polymorphism:

    """Base example: shows the common interface every 'player' shares."""

    def __init__(self):
        print("Welcome to Polymorphism Property !!")

    def play(self):
        return "We are playing game !!"


class FootballPlayer(Polymorphism):
    def play(self):
        return "We are playing Football !"

class ChessPlayer(Polymorphism):
    def play(self):
        return "We are playing Chess !"

def demo_polymorphism():
    """Call .play() on different types without caring which one it is."""
    players = [FootballPlayer() , ChessPlayer()]
    for p in players:
        print(p.play())
    
class Inheritence:

    def __init__(self):
        return "Welcome to Inheritence Property !!"

class Vehicle(Inheritence):

    def __init__(self, model, agency, location, brand_value):
        super().__init__()
        self.model = model
        self.agency = agency 
        self.location = location
        self._brand_value = brand_value

        # For the given constraints are Null at the point
        self.tank_limit = None
        self.volume = None

    def status_of_vehicle(self):
        return "Currently in rest position"

    def brand_value(self,brand_value):
        self._brand_value = brand_value
        return f"The brand Value of the model : {self.brand_value}"

    def fuel_tank(self,tank_limit, volume):
        self.tank_limit = float(
            input(f"Enter the tank_limit of the vehicle (Current : {self.tank_limit})")
        )
        self.volume = float (
            input(f"Enter the voulme of fuel filled in the tank (Current : {self.volume})")
        )

    def refill(self,check):
        self.check = check
        if self.tank_limit is None or self.volume is None:
            return "Fuel tank has not been set yet - call fuel_tank() first."
        if self.tank_limit >= 10000.0 and self.volume <= 20.0:
            return "Kindly refill the tank as per the level/volume"
        else :
            return f"Vehicle has refilled successfully : {self.volume} with the mentioned tank_limit : {self.tank_limit}"
        
class Car(Vehicle):

    def __init__(self, model, agency, location, brand_value):
        super().__init__(model, agency, location, brand_value)
        print("Welcome to the Car Section")

    def brand_name(self,brand):
        self.brand = brand
        return self.brand

    def brand_value(self, brand_value):
        return super().brand_value(brand_value)

class Abstraction(ABC):

    @abstractmethod
    def secure_payment(self):
        """Provide a payment """
        pass

    @abstractmethod
    def identity_of_Model(self):
        pass

    @abstractmethod
    def is_available(self):
        pass

class Abstract_Class_Implementation(Abstraction):

    def __init__(self):
        print("Welcome to the concreate class where implementation where happens !!")

    def secure_payment(self):
        return "Payment has initiated successfully !!"

    def identity_of_Model(self):
        return "The identity of model has been displayed on the screen"

    def is_available(self):
        return "The model has been available as per requirement"

if __name__ == "__main__":
    e = Encapsulation()
    e.encapsulation(1,"Aman","Delhi","secret123")
    print(e.get_name(), e.get_password())

    demo_polymorphism()

    c = Car("Model X","Abc motors", "Delhi", 500000)
    print(c.status_of_vehicle())
    print(c.brand_value(600000))


    imp1 = Abstract_Class_Implementation()
    print(imp1.secure_payment())

    







    