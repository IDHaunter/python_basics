# JSON = JavaScript Object Notation
import json

birthYear = input("What is your birth year ")
age = 2024 - int(birthYear)
price = 19.95
firstName = input("What is your name? ")
isOnLine = False
print("Hello " + firstName.upper() + ', your age is ' + str(age))
if (age > 1 and age < 50):
    print("You are so young to die")
elif age == 0:
    print("Where is your diaper?")
elif age > 50 and age < 100:
    print("You are pretty old")
    print("and it's cool")
elif age > 100 and age < 140:
    print("You are fucking old")
elif age > 140 and age < 200:
    print("You are kidding me?")
else:
    print("Something wrong with your age")
print("Bye!")

i = 3
while i >= 0:
    print(i)
    i -= 1

print("BOOM!")

names = ["John", "Bob", "Mary", "Zerg"]
names[0] = "Jons"
print(names[0] + ' ' + names[-1])
print(names[0:3])
print(len(names))
for item in names:
    print('for ' + str(item))
i = 0
while i < len(names):
    print('while ' + str(names[i]))
    i += 1

jsonString = '''
{
"students":[{"a": 1},{"a": 2},{"a": 6}],
"school": 52
}
'''
data = json.loads(jsonString)
print(data['students'][0])
data['test'] = True

newJson = json.dumps(data)
print(newJson)

# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing elements by key
print(my_dict['name'])  # Outputs 'John'
print(my_dict['age'])   # Outputs 30
print(my_dict['city'])  # Outputs 'New York'

# Adding a new element
my_dict['occupation'] = 'Engineer'

# Changing a value by key
my_dict['age'] = 31

# Removing an element by key
del my_dict['city']

# Checking if a key is in the dictionary
if 'city' in my_dict:
    print('City is present.')
else:
    print('City is not present.')

# Getting a list of all keys and values
keys = my_dict.keys()
values = my_dict.values()

# Iterate over key-value pairs
for key, value in my_dict.items():
    print(f'{key}: {value}')