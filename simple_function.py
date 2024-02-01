from simple_classes import Car

carDonald = Car("Chevy","Corvette",2023,"blue")

def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)
    return "Hello " + first + " " + middle + " " + last

hello("Mr.","Donald", "the Duck")
hello(first="Mr.",middle="Donald", last="the Duck")
print(hello("Mr.","Donald", "the Duck"))

print(f"Here is your {carDonald.color} {carDonald.make} {carDonald.model}")
carDonald.drive()