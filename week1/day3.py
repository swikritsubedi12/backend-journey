# ====================================
# DAY 3 — Control Flow (if/else, loops)
# ====================================

# Task 1: FizzBuzz (CLASSIC INTERVIEW QUESTION)
# Print numbers 1 to 100, but:
#   - Multiples of 3 → print "Fizz"
#   - Multiples of 5 → print "Buzz"
#   - Multiples of both 3 and 5 → print "FizzBuzz"
#   - Otherwise → print the number
for i in range(1,101):
    if i%3 == 0 and i%5==0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)





# Task 2: Multiplication Table
# Take a number N from user.
# Print its multiplication table from 1 to 10.
# Example: N=5 → 5x1=5, 5x2=10, ... 5x10=50
N = 8
for i in range(1,11):
    print(f"{N}x{i} = {N*i}")


# Task 3: Factorial
# Take a number N from user.
# Calculate factorial: N! = N × (N-1) × (N-2) × ... × 1
# Example: 5! = 120
# Hint: Use a loop with a running product variable
userinput = 5
factorial = 1
for i in range(userinput, 0, -1):
    factorial = factorial*i

print(f"Factorial: {factorial}")



# Task 4: Fibonacci Series
# Take N from user, print first N Fibonacci numbers.
# Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# (Each number = sum of previous two)

N = 9

a=0
b=1

for i in range(N):
    print(a)
    next_number = a+b
    a=b
    b=next_number


# Task 5: Prime Number Check
# Take a number from user.
# Print whether it's prime or not.
# Hint: A prime is divisible only by 1 and itself.
# Optimization: Only check up to √n

N = 10
if N <= 1:
    print("Not Prime")
else:
    is_prime = True

    for i in range(2,N):
        if N % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")


# Task 6: Sum of Digits
# Take a number, return sum of its digits.
# Example: 1234 → 1+2+3+4 = 10
# Hint: Use while loop with % 10 and // 10

number = 1234
sum = 0
while number > 0:
    digit = number % 10
    sum = sum + digit
    number = number // 10

print(sum)



# Task 7: Reverse a Number
# Take a number, reverse it WITHOUT converting to string.
# Example: 1234 → 4321
# Hint: Use modulus and division

# Task 7: Reverse a Number

num = 567

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)

# Task 8: Star Pattern (Right Triangle)
# Take N from user, print:
# *
# **
# ***
# ****
# *****  (for N=5)
# Task 8: Star Pattern

n = 5

for i in range(1, n + 1):
    print("*" * i)

# Task 9: Inverted Star Pattern
# Take N from user, print:
# *****
# ****
# ***
# **
# *

N = 5
for i in range(N, 0, -1):
    print("*"*i)

# Task 10: Pyramid Pattern (BONUS)
# Take N from user, print:
#     *
#    ***
#   *****
#  *******
# ********* (for N=5)
N = 5

for i in range(1, N + 1):
    spaces = N - i
    stars = 2 * i - 1

    print(" " * spaces + "*" * stars)


# Task 11: Number Guessing Game
# Computer picks a random number between 1 and 100 (use random module).
# User has 7 tries to guess it.
# After each guess, print "Too high", "Too low", or "Correct!"
# Print number of attempts used.
# import random  ← put this at the top
# random_number = random.randint(1, 100)

import random

random_number = random.randint(1, 100)
tries = 0
limit = 7

while tries < limit:
    guess = int(input("Enter your guess: "))
    tries += 1

    if guess == random_number:
        print("Correct!")
        print("Attempts used:", tries)
        break
    elif guess > random_number:
        print("Too high!")
    else:
        print("Too low!")

else:
    print("You exceeded your limit!!")
    print("The number was:", random_number)

print("Attempts used:", tries)
    
    

# Task 12: Find Largest of Three Numbers
# Take 3 numbers from user, print the largest WITHOUT using max().
a = 2
b = 10
c = 3

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number:", largest)


# Task 13: Count Digits in a Number
# Example: 12345 → 5 digits
# DO NOT use len(str(n)) — use a while loop

number = 123456
count = 0
while number>0:
    digit = number%10
    count += 1
    number = number // 10

print(count)

# Task 14: Armstrong Number Check
# A number is Armstrong if sum of cubes of its digits = the number itself.
# Example: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ✓
# Take a 3-digit number, check if Armstrong.

# Task 14: Armstrong Number Check

number = 153

original_number = number
sum_cubes = 0

while number > 0:
    digit = number % 10
    sum_cubes = sum_cubes + digit ** 3
    number = number // 10

if sum_cubes == original_number:
    print("Armstrong")
else:
    print("Not Armstrong")
