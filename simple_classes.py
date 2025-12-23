class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("Car is driving ...")

    def stop(self):
        print("Car is stopped !")


# ElectricCar inherits from Car
class ElectricCar(Car):
    def __init__(self, make, model, year, color, battery_capacity):
        # Call parent class constructor
        super().__init__(make, model, year, color)
        # Add new attribute specific to ElectricCar
        self.battery_capacity = battery_capacity  # in kWh
        self.battery_level = 100  # percentage

    # Override the drive method
    def drive(self):
        print(f"{self.make} {self.model} is driving silently on electric power...")
        self.battery_level -= 5  # Reduce battery when driving

    # Add new method specific to ElectricCar
    def charge(self):
        self.battery_level = 100
        print(f"{self.make} {self.model} is fully charged!")

    # Override get_info to include battery info
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} | Battery: {self.battery_capacity}kWh ({self.battery_level}%)"


# SportsCar inherits from Car
class SportsCar(Car):
    def __init__(self, make, model, year, color, top_speed):
        super().__init__(make, model, year, color)
        self.top_speed = top_speed  # in mph
        self.is_turbo_on = False

    # Override the drive method
    def drive(self):
        if self.is_turbo_on:
            print(f"{self.make} {self.model} is driving FAST with turbo boost!")
        else:
            print(f"{self.make} {self.model} is driving sportily...")

    # Add new method specific to SportsCar
    def toggle_turbo(self):
        self.is_turbo_on = not self.is_turbo_on
        status = "ON" if self.is_turbo_on else "OFF"
        print(f"Turbo mode: {status}")

    # Add another new method
    def race_mode(self):
        self.toggle_turbo()
        print(f"Race mode activated! Top speed: {self.top_speed}mph")


# Example usage
if __name__ == "__main__":
    # Create a regular car
    regular_car = Car("Toyota", "Camry", 2022, "Blue")
    print("Regular Car:")
    print(regular_car.get_info())
    regular_car.drive()
    regular_car.stop()
    print()

    # Create an electric car
    tesla = ElectricCar("Tesla", "Model 3", 2023, "Red", 75)
    print("Electric Car:")
    print(tesla.get_info())
    tesla.drive()
    tesla.drive()  # Drive again to reduce battery
    print(f"Battery level: {tesla.battery_level}%")
    tesla.charge()
    tesla.stop()
    print()

    # Create a sports car
    porsche = SportsCar("Porsche", "911", 2024, "Black", 190)
    print("Sports Car:")
    print(porsche.get_info())
    porsche.drive()
    porsche.toggle_turbo()
    porsche.drive()
    porsche.race_mode()
    porsche.stop()


