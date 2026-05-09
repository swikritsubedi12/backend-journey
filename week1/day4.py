# ====================================
# DAY 4 — Lists & Tuples
# ====================================

# Task 1: Sum & Average
# Take 5 numbers from user, store in a list.
# Print sum, average, max, and min.
count = 0
user_list = []
while count<5:
    user_input = int(input("Enter the number: "))
    user_list.append(user_input)
    count+=1

print(user_list)
print(sum(user_list))
print(sum(user_list)/len(user_list))
print(max(user_list))
print(min(user_list))


# Task 2: Second Largest Number
# Given a list, find the second largest WITHOUT using sort().
# Example: [10, 20, 4, 45, 99] → 45

numbers = [10, 20, 4, 45, 99]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)


# Task 3: Remove Duplicates (Preserve Order)
# Given [1, 2, 2, 3, 4, 4, 5], return [1, 2, 3, 4, 5]
# DO NOT use set() — write your own logic.

new = [1, 2, 2, 3, 4, 4, 5]
no_duplicate = []
others = []
for i in new:
    if i not in no_duplicate:
        no_duplicate.append(i)
    else:
        others.append(i)

print(no_duplicate)

# Task 4: Merge Two Sorted Lists
# Input: [1, 3, 5] and [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]
# Hint: You can simply combine then sort, but try a manual merge too.

a = [1,3,5]
b = [2,4,6]
a.extend(b)
print(sorted(a))

# Task 5: List Comprehension Practice
# Using ONE LINE list comprehensions:
#   a) Squares of even numbers from 1 to 20
#   b) Uppercase versions of ["apple","banana","mango"]
#   c) Numbers from 1-50 divisible by both 3 and 5
#   d) Lengths of words in ["hi", "hello", "hey", "world"]

squares = [x**2 for x in range(1,21) if x % 2 == 0]
upper = [x.upper() for x in ["apple","banana","mango"]]
numbers = [x for x in range(1,51) if x%3 == 0 and x%5 == 0]
word_count = [len(x) for x in ["hi", "hello", "hey", "world"]]
print(squares)
print(upper)
print(numbers)
print(word_count)

# Task 6: Rotate a List
# Given a list and k, rotate the list k positions to the right.
# Example: [1,2,3,4,5], k=2 → [4,5,1,2,3]
# Hint: Slicing makes this a one-liner.

numbers = [1, 2, 3, 4, 5]
k = 2

rotated = numbers[-k:] + numbers[:-k]

print(rotated)

# Task 7: Find Common Elements
# Given two lists, return elements present in BOTH.
# Example: [1,2,3,4] and [3,4,5,6] → [3,4]

x= [1,2,3,4]
y = [3,4,5,6]
both = [item for item in x if item in y]

print(both)

# Task 8: Flatten a Nested List
# Input: [[1,2], [3,4], [5,6]]
# Output: [1, 2, 3, 4, 5, 6]
# Try both: a regular for-loop AND a list comprehension.
Input= [[1,2], [3,4], [5,6]]
output = []

for small_items in Input:
    for items in small_items:
        output.append(items)

print(output)


# Task 9: Count Positive, Negative, and Zero
# Given a list of numbers, count how many are positive, negative, zero.
# Return as a tuple: (positives, negatives, zeros)

numbers = [1, -2, 0, 5, -7, 0, 9]
positive = 0
negative = 0
zero = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

result = (positive, negative, zero)  
print(result)

# Task 10: Move Zeros to End
# Given [0, 1, 0, 3, 12], return [1, 3, 12, 0, 0]
# Order of non-zero elements must stay the same.

numbers = [0, 1, 0, 3, 12]
positive = []
zero = []

for num in numbers:
    if num > 0:
        positive.append(num)
    elif num == 0:
        zero.append(num)

result = (positive, zero)
output = []
for item in result:
    for small_item in item:
        output.append(small_item)

print(output)

# Task 11: Tuple Unpacking Practice
# Create a list of tuples: students = [("Alice", 85), ("Bob", 72), ("Carol", 90)]
# Loop through and print: "Alice scored 85"

students = [("Alice", 85), ("Bob", 72), ("Carol", 90)]

for name, marks in students:
    print(f"{name} scored {marks}")

# Task 12: Find Pair with Given Sum
# Given a list and a target sum, find any pair that adds up to the target.
# Example: [2, 7, 11, 15], target=9 → (2, 7)
# Return the pair as a tuple.

numbers = [2, 7, 11, 15]
target = 9

pair = None

for num1 in numbers:
    for num2 in numbers:
        if num1 != num2 and num1 + num2 == target:
            pair = (num1, num2)
            break

    if pair != None:
        break

print(pair)



# Task 13: Reverse a List in 3 Different Ways
# a) Using [::-1] slicing
# b) Using .reverse() method
# c) Using a loop (without any built-in)

numbers = [2, 7, 11, 15]

# a) Using slicing
reversed_slicing = numbers[::-1]
print(reversed_slicing)

# b) Using .reverse()
numbers2 = [2, 7, 11, 15]
numbers2.reverse()
print(numbers2)

# c) Using a loop
numbers3 = [2, 7, 11, 15]
reversed_loop = []

for i in range(len(numbers3) - 1, -1, -1):
    reversed_loop.append(numbers3[i])

print(reversed_loop)

# Task 14: Min-Max Without Built-in
# Find min and max of a list WITHOUT using min() or max().
# Return as a tuple.

numbers = [2, 7, 11, 15]
min_number = numbers[0]
max_number = numbers[0]

for num in numbers:
    if num > max_number:
        max_number = num
    if num < min_number:
        min_number = num
    
result = (min_number, max_number)
print(result)


# Task 15: Cumulative Sum
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]   (each item = sum of all previous + itself)
new = [1,2,3,4]
out = []
total = 0

for num in new:
    total = total+num
    out.append(total)

print(out)