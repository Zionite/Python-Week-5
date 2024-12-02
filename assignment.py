# ACTIVITY 1
class Smartphone:
    def __init__(self, brand, model, price):
        self.__brand = brand  # Private attribute to protect brand
        self.__model = model  # Private attribute to protect model
        self.__price = price  # Private attribute to protect price

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def display_details(self):
        return f"Brand: {self.__brand}, Model: {self.__model}, Price: ${self.__price}"

    def turn_on(self):
        return f"The {self.__brand} {self.__model} is powering up. Welcome!"

class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, features):
        super().__init__(brand, model, price)
        self.features = features 

    def display_details(self):
        base_details = super().display_details()
        return f"{base_details}, Features: {', '.join(self.features)}"

smartphone = Smartphone("Apple", "iPhone 14", 999)
smartwatch = Smartwatch("Samsung", "Galaxy Watch 5", 299, ["Heart Rate Monitor", "GPS", "Water Resistant"])

print(smartphone.display_details())
print(smartphone.turn_on())
print(smartwatch.display_details())


# ACTIVITY 2
# Polymorphism Challenge: Vehicles with different move() actions
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

def demonstrate_movement(vehicle):
    print(vehicle.move())

car = Car()
plane = Plane()
boat = Boat()

demonstrate_movement(car)
demonstrate_movement(plane)
demonstrate_movement(boat)
