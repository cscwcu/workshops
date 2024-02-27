###############
# Problem Set for the CS Club Matching Game
# Author: Zach Eanes
# Date 09/07/2023
###############

# Largest Number
num1 = 12
num2 = 8
num3 = 15
largest = max(num1, num2, num3)
print(largest)

# Check for element in list
my_list = [1, 3, 5, 7, 9]
element = 5
if element in my_list:
    print("Found")
else:
    print("Not found")


# Simple Class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

rect = Rectangle(4, 5)
print(rect.area())

# String Manipulation to Upper
text = "Computer Science Club is the best!"
print(text.upper())

# While Loop
i = 0
while i < 10:
    print(i, end=" ")
    i += 1
print()

# Square Numbers
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2
print(numbers)  

# Minimum Number
num1 = 12
num2 = 8
num3 = 15
largest = min(num1, num2, num3)
print(largest)

# Subtraction
x = 12948
y = 1234
print(y - x)

# String Manipulation to Lower
text = "Computer Science Club is the best!"
print(text.lower())

# Type Function
x = 1.234
print(type(x))

# Type Function 2
x = 1234
print(type(x))

# Float Division
x = 1234
y = 5678
print(x / y)

# Integer Division
x = 1234
y = 5678
print(x // y)

# String Manipulation to Title
text = "Computer Science Club is the best!"
print(text.title())

# String Manipulation to Capitalize
text = "Computer Science Club is the best!"
print(text.capitalize())

# String Manipulation to Swap Case
text = "Computer Science Club is the best!"
print(text.swapcase())

# Print a Pattern
n = 4
for i in range(1, n + 1):
    print(n * i, end = " ")
for i in range(n - 1, 0, -1):
    print(n * i, end = " ")
print()

# Return a List
def function(w, x, y, z):
    return list((w, x, y, z))

print(function("I", "love", "CS", "Club"))

# Trick Question
x = 1234
y = 5678
z = x + y

# Print a Pattern 2
n = 4
for i in range(1, n + 1):
    print(n / i, end = " ")
for i in range(n - 1, 0, -1):
    print(n / i, end = " ")
print()

