# ====================================
# DAY 5 — Dictionaries & Sets
# ====================================

# Task 1: Word Frequency Counter
# Take a sentence, return a dict where keys = words, values = count.
# Example: "the cat sat on the mat" → {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}

Example = "the cat sat on the mat"
Example = Example.split()
word_count = {}

for word in Example:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

# Task 2: Character Frequency Counter
# Take a string, return a dict of character → count.
# Example: "hello" → {"h":1, "e":1, "l":2, "o":1}

Example = "hello"
word_count = {}
for word in Example:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

# Task 3: Merge Two Dictionaries
# If a key exists in both, SUM the values.
# Example: {"a":1, "b":2} + {"b":3, "c":4} → {"a":1, "b":5, "c":4}

a = {"a": 1, "b": 2}
b = {"b": 3, "c": 4}

c = {}

for key in a:
    c[key] = a[key]

for key in b:
    if key in c:
        c[key] += b[key]
    else:
        c[key] = b[key]

print(c)

# Task 4: Find Common Characters (use sets!)
# Given two strings, return characters that appear in BOTH.
# Example: "python" and "typhoon" → {'p', 'y', 't', 'h', 'o', 'n'}
# (Order doesn't matter — sets are unordered)

e1 = set("python")
e2 = set("typhoon")
result = e1 & e2
print(result)

# Task 5: Phonebook (mini CRUD project)
# Build a CLI menu:
#   1. Add contact (name → phone)
#   2. Search contact by name
#   3. Delete contact
#   4. List all contacts
#   5. Exit
# Store in a dict. Loop until user picks Exit.
# Handle missing names gracefully (use .get()).
contacts = {}
while True:
    print("1: Add contact")
    print("2: Search contact")
    print("3: Delete contact")
    print("4: List Contact")
    print("5: Exit")
    user_input = int(input("What would you like to do?(1/2/3/4/5): "))
    if user_input == 1:
        add_name = input("Enter name to add: ")
        add_phno = int(input("Enter the number: "))
        if add_name in contacts:
            print("Contact Exists!!")
        else:
            contacts[add_name] = add_phno
            print("Contact Added!")
    elif user_input == 2:
        search_name = input("Which name would you like to search?: ")
        if search_name in contacts:
            print(f"{search_name} -> {contacts.get(search_name)}")
        else:
            print(f"{search_name} does not exist!!")
    elif user_input == 3:
        del_name = input("Enter name you want to delete: ")
        if del_name in contacts:
            contacts.pop(del_name)
            print(f"{del_name} deleted successfully!!")
    elif user_input == 4:
        print(contacts)
    elif user_input == 5:
        break

print("Thank You!!")
    

# Task 6: Group Words by First Letter
# Input: ["apple", "ant", "banana", "bat", "cat"]
# Output: {"a": ["apple", "ant"], "b": ["banana", "bat"], "c": ["cat"]}

Input = ["apple", "ant", "banana", "bat", "cat"]

output = {}

for i in Input:
    first_letter = i[0]

    if first_letter in output:
        output[first_letter].append(i)
    else:
        output[first_letter] = [i]

print(output)


# Task 7: Invert a Dictionary
# Input: {"a": 1, "b": 2, "c": 3}
# Output: {1: "a", 2: "b", 3: "c"}
# (Swap keys and values)

Input = {"a": 1, "b": 2, "c": 3}
output = {}
for key, value in Input.items():
    output[value] = key

print(output)

# Task 8: Find Duplicates Using Set
# Given a list, return items that appear MORE THAN ONCE.
# Example: [1, 2, 3, 2, 4, 5, 3, 6] → {2, 3}
Input = [1, 2, 3, 2, 4, 5, 3, 6]

seen = set()
duplicates = set()

for item in Input:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print(duplicates)


# Task 9: Two Sum (THE most famous interview question — using dict!)
# Given a list and target, return INDICES of the two numbers that add to target.
# Example: nums=[2, 7, 11, 15], target=9 → [0, 1]
# Hint: Loop once. For each num, check if (target - num) is already in dict.
# Solve in O(n) — single pass!

nums = [2, 7, 11, 15]
target = 9

seen = {}

for i, num in enumerate(nums):
    needed = target - num

    if needed in seen:
        print([seen[needed], i])
        break

    seen[num] = i

# Task 10: Student Marks → Grades
# Input: {"Alice": 85, "Bob": 42, "Carol": 73, "David": 90}
# Output: {"Alice": "A", "Bob": "F", "Carol": "B", "David": "A"}
# Grading: A>=80, B>=70, C>=60, D>=50, F<50
# Use a dict comprehension if you can!

marks = {"Alice": 85, "Bob": 42, "Carol": 73, "David": 90}

grades = {}

for name, mark in marks.items():
    if mark >= 80:
        grades[name] = "A"
    elif mark >= 70:
        grades[name] = "B"
    elif mark >= 60:
        grades[name] = "C"
    elif mark >= 50:
        grades[name] = "D"
    else:
        grades[name] = "F"

print(grades)

# Task 11: Top 3 Highest Scorers
# Given the dict above, return names of top 3 scorers in order.
# Hint: sorted(d.items(), key=lambda x: x[1], reverse=True)

marks = {"Alice": 85, "Bob": 42, "Carol": 73, "David": 90}

sorted_marks = sorted(marks.items(), key=lambda x: x[1], reverse=True)

top_3 = []

for name, mark in sorted_marks[:3]:
    top_3.append(name)

print(top_3)

# Task 12: Set Operations
# Given:
#   python_devs = {"Alice", "Bob", "Carol", "David"}
#   js_devs = {"Bob", "Eve", "Carol", "Frank"}
# Find:
#   a) Devs who know BOTH (intersection)
#   b) Devs who know EITHER (union)
#   c) Devs who know ONLY Python (difference)
#   d) Devs who know one but not both (symmetric difference)

python_devs = {"Alice", "Bob", "Carol", "David"}
js_devs = {"Bob", "Eve", "Carol", "Frank"}

both = python_devs & js_devs
either = python_devs | js_devs
only_python = python_devs - js_devs
one_not_both = python_devs ^ js_devs

print("Both:", both)
print("Either:", either)
print("Only Python:", only_python)
print("One but not both:", one_not_both)

# Task 13: Anagram Check (using dicts/sets)
# Two strings are anagrams if they contain the same characters with same counts.
# Example: "listen" and "silent" → True
# "hello" and "world" → False
# Solve using character frequency dicts.

word1 = "listen"
word2 = "silent"

count1 = {}
count2 = {}

for char in word1:
    if char in count1:
        count1[char] += 1
    else:
        count1[char] = 1

for char in word2:
    if char in count2:
        count2[char] += 1
    else:
        count2[char] = 1

if count1 == count2:
    print(True)
else:
    print(False)

# Task 14: Nested Dictionary Access
# Given:
#   data = {
#       "user": {
#           "name": "Alice",
#           "address": {"city": "Delhi", "pincode": 110001}
#       }
#   }
# Print the city. Then add "country": "India" to the address.

data = {
    "user": {
        "name": "Alice",
        "address": {
            "city": "Delhi",
            "pincode": 110001
        }
    }
}

print(data["user"]["address"]["city"])

data["user"]["address"]["country"] = "India"

print(data)

# Task 15: Remove Duplicates Preserving Order (using set as helper)
# Given [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# Return [3, 1, 4, 5, 9, 2, 6]
# Use a set to track seen items, but build a list to preserve order.

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

seen = set()
result = []

for num in numbers:
    if num not in seen:
        result.append(num)
        seen.add(num)

print(result)