# 1. Define the Parent (Base) Class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand  # Inheritable attribute
        self.model = model  # Inheritable attribute

    def start_engine(self):
        # Shared method available to all subclasses
        return f"The engine of this {self.brand} is now running."

    def fuel_type(self):
        return "Generic fuel"


# 2. Define the Child (Derived) Class
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        # super() initializes parent attributes without rewriting code
        super().__init__(brand, model)
        self.doors = doors  # Unique child attribute

    # Method Overriding: Replaces the parent's logic with child-specific logic
    def fuel_type(self):
        return "Gasoline"

    def open_trunk(self):
        # Unique child method
        return "Trunk is open."


# 3. Instantiate and Use the Objects
# Create an instance of the child class
my_car = Car("Toyota", "Camry", 4)

# Accessing inherited attributes and methods
print(my_car.brand)          # Output: Toyota
print(my_car.start_engine()) # Output: The engine of this Toyota is now running.

# Accessing overridden and unique child features
print(my_car.fuel_type())   # Output: Gasoline (Uses child version, not parent)
print(my_car.open_trunk())   # Output: Trunk is open.
