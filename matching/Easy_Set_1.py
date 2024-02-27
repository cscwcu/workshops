###############
# Problem Set for the CS Club Matching Game
# Author: Kaushal Patel
# Date 09/07/2023
###############

# Problem 1
x = 5
y = 3
result = x + y
print(result)


# Problem 2
word = "Hello"
for letter in word:
    print(letter)


# Problem 3
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)


# Problem 4
for i in range(5):
    print(i)


# Problem 5
text = "Python is fun!"
length = len(text)
print(length)


# Problem 6
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Problem 7
def multiply(a, b):
    return a * b

result = multiply(4, 6)
print(result)


# Problem 8
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Problem 9
def square(n):
    return n ** 2

result = square(3)
print(result)


# Problem 10
numbers = [2, 4, 6, 8, 10]
for num in numbers:
    if num > 5:
        print(num)


# Problem 11
name = "Alice"
greeting = "Hello, " + name + "!"
print(greeting)


# Problem 12
def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

result = average([3, 6, 9])
print(result)


# Problem 13
temperature_celsius = 25
temperature_fahrenheit = (temperature_celsius * 9/5) + 32
print(temperature_fahrenheit)


# Problem 14
numbers = [1, 2, 3, 4, 5]
squared = [num ** 2 for num in numbers]
print(squared)


# Problem 15
def is_even(n):
    return n % 2 == 0

result = is_even(7)
print(result)


# Problem 16
word = "Python"
if "y" in word:
    print("Letter 'y' found")
else:
    print("Letter 'y' not found")


# Problem 17
numbers = [3, 6, 9, 12]
total = 0
for num in numbers:
    total += num
print(total)


# Problem 18
age = 19
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")


# Problem 19
def greet(name):
    return "Hello, " + name + "!"

message = greet("Bob")
print(message)


# Problem 20
numbers = [10, 20, 30, 40, 50]
count = len(numbers)
print("The list contains", count, "numbers")
