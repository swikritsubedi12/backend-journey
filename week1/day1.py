# ====================================
# DAY 1 — Variables, Data Types, Operators
# ====================================

# Task 1: Greeting
# Take user's name and age as input.
# Print: "Hi <name>, next year you will be <age+1> years old."
username = input("Enter your username: ")
age = int(input("Enter your age: "))
print(f"Hi {username}, next year you will be {age+1} years old.")

# Task 2: Rectangle Area & Perimeter
# Take length and width as input.
# Print both area and perimeter.
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
perimeter = length + length + width + width
print(f"The area of rectangle is {area:.2f} and perimeter is {perimeter:.2f}.")


# Task 3: Temperature Converter
# Take temperature in Celsius.
# Convert to Fahrenheit using: F = (C * 9/5) + 32
# Print result rounded to 2 decimal places.
celcius = float(input("Enter the temperature in celcius: "))
fahrenheit = (celcius*9/5) + 32
print(f"The temperature in fahrenheit is {fahrenheit:.2f}.")


# Task 4: Even or Odd
# Take a number from user.
# Print whether it's even or odd (use modulus %).
number = int(input("Enter a number: "))
if number==0:
    print(f"The number is 0.")
elif number%2==0:
    print(f"{number} is even number.")
else:
    print("The number is odd.")

# Task 5: Simple Interest Calculator
# Take Principal (P), Rate (R), Time (T) as input.
# Formula: SI = (P * R * T) / 100
# Print the simple interest.
principal= float(input("Enter the number: "))
rate = float(input("Enter rate in %: "))
time = float(input("Enter the duration: "))
SI = (principal*time*rate)/100
print(f"The simple interest is {SI}")

# Task 6: Swap Two Variables
# Take two numbers a and b.
# Swap them WITHOUT using a third variable.
# Print before and after swap.
a = 1
b = 2
print("Before Swap: ")
print("a = ",a)
print("b = ",b)

a = a+b
b = a-b
a = a-b

print("After swap:")
print("a =", a)
print("b =", b)


# Task 7: ASCII Value
# Take a single character from user.
# Print its ASCII value using ord() function.
# Then take a number, print its character using chr() function.

character = input("Enter a single word: ")
ascivalue = ord(character)
print(ascivalue)
another_number = chr(ascivalue)
print(another_number)