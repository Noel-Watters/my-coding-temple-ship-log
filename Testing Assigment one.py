#Text-base name generator that combims random first and last name using string manipulation
import random

first_names = ['Christian', 'Dylan', 'Travis', 'Katelyn']
last_names = ['Sachs', 'Katina', 'Peck', 'Mehner']

num1 = (random.randrange(0,3))
num2 = (random.randrange(0,3))

print(f"My name is {first_names[num1]} {last_names[num2]}.")
print(f" My name is {random.choice(first_names)} {random.choice(last_names)}")