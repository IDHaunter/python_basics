from simple_classes import Car

carDonald = Car("Chevy", "Corvette", 2023, "blue")


def hi() -> str:
    print("Hello World!")
    return "Hello World!"


hi()


def hello(first, middle, last) -> str:
    print("Hello " + first + " " + middle + " " + last)
    return "Hello " + first + " " + middle + " " + last


hello("Mr.", "Donald", "the Duck")
hello(first="Mr.", middle="Donald", last="the Duck")
print(hello("Mr.", "Donald", "the Duck"))

print(f"Here is your {carDonald.color} {carDonald.make} {carDonald.model}")
carDonald.drive()
