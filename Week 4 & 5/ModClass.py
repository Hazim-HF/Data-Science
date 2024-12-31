class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage
        print(f"The odometer reading has been updated to {self.odometer_reading} miles.")

    def increment_odometer(self, miles):
        """Add the given amount of the odometer reading."""
        self.odometer_reading += miles
        print(f"The odometer has been increased to {self.odometer_reading}")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 70
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")