#!/usr/bin/python3
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    """Bus class with method overriding"""
    def seating_capacity(self, capacity=50):
        """Overriding the method from Vehicle class"""
        try:
            return ("Bus {} has capaity of {}".format(self.name, capacity))
        except Exception as e:
            return e
print(Bus("Ferarri", 33, 90).seating_capacity())