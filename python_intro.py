#!/usr/bin/env python3
# =========================
# Part 1: Introduction to Python
# =========================

# 1.1 Getting Started
print("Hello, World!")

# Variables + f-string
name = "Alice"      # String
age = 20            # Integer
height = 5.5        # Float
is_student = True   # Boolean


print(f"{name} is {age} years old.")

# Data Types examples
# Strings
greeting = "hello"
print(greeting.upper())      # "HELLO"
print("a,b,c".split(","))    # ['a', 'b', 'c']

# Lists
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple

# Dictionaries
person = {"name": "Bob", "age": 25}
print(person["name"])  # Bob

# Tuples
coords = (10, 20)
print(coords[0], coords[1])  # 10 20

# Exercise (1.1): Create a list of 5 numbers, print the sum using sum(my_list)
my_list = [3, 7, 2, 10, 8]
print("Sum of my_list:", sum(my_list))


# 1.2 Control Structures

# If-Else example
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")

# For loop example
for fruit in ["apple", "banana"]:
    print(fruit)

# While loop example
count = 0
while count < 3:
    print(count)
    count += 1

# Exercise (1.2): Write a loop to print even numbers from 1 to 10
for num in range(1, 11):
    if num % 2 == 0:
        print(num)


# 1.3 Functions

def greet(name):
    return f"Hello, {name}!"

print(greet("Charlie"))

# Exercise (1.3): Write a function add_numbers(a, b) that returns their sum.
def add_numbers(a, b):
    return a + b

print("add_numbers(5, 7) =", add_numbers(5, 7))


# 1.4 Modules

import math
print("sqrt(16) =", math.sqrt(16))

# We'll use import re later for regex (Part 2)
