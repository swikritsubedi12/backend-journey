# ====================================
# DAY 2 — Strings & String Methods
# ====================================

# Task 1: Reverse a String
# Take input from user, print reversed string using slicing.
# Example: "hello" → "olleh"
input1 = "Hello"
reverse_input1 = input1[::-1]
print(reverse_input1)


# Task 2: Count Vowels
# Take a sentence, count how many vowels (a, e, i, o, u) it contains.
# Should work for both uppercase and lowercase.
check = "Aj eio"
check = check.lower()

count = (
    check.count("a") +
    check.count("e") +
    check.count("i") +
    check.count("o") +
    check.count("u")
)

print(count)



# Task 3: Palindrome Check
# Take a word from user, check if it reads the same forwards and backwards.
# Example: "madam" → Palindrome, "hello" → Not palindrome
# Hint: Use slicing with [::-1]
p_check = "ama"
if p_check == p_check[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# Task 4: Capitalize Words
# Take a sentence, capitalize the first letter of every word.
# DO NOT use .title() — write your own logic with .split() and .join()
# Example: "hello world from python" → "Hello World From Python"
# Task 4: Capitalize Words

sentence = "hello world from python"

words = sentence.split()
capitalized_words = []

for word in words:
    capitalized_word = word[0].upper() + word[1:]
    capitalized_words.append(capitalized_word)

result = " ".join(capitalized_words)

print(result)


# Task 5: Email Parser
# Take an email like "first.last@domain.com"
# Extract and print: first name, last name, domain
# Example: "john.doe@gmail.com" → First: john | Last: doe | Domain: gmail.com
# Task 5: Email Parser using find() and slicing

email = "john.doe@gmail.com"

dot_position = email.find(".")
at_position = email.find("@")

first_name = email[:dot_position]
last_name = email[dot_position + 1 : at_position]
domain = email[at_position + 1 :]

print("First:", first_name)
print("Last:", last_name)
print("Domain:", domain)



# Task 6: Count Word Occurrences
# Take a sentence and a word.
# Print how many times that word appears (case-insensitive).
# Example: "Python is great. python is easy." + "python" → 2
word = "Python is great. python is easy."
word = word.lower().split()
word_count = {}
for i in word:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] =1
print(word_count)

# Task 7: Remove All Spaces
# Take a string and remove ALL spaces (not just trim).
# Example: "h e l l o   world" → "helloworld"
# Hint: use .replace()
new = "h e l l o   world"
new = new.replace(" ","")
print(new)

# Task 8: Initials Generator
# Take a full name, return initials in uppercase.
# Example: "swikrit kumar subedi" → "S.K.S"
names = "swikrit kumar subedi"

words = names.split()
initials = ""

for word in words:
    initials += word[0].upper() + "."

initials = initials[:-1]

print(initials)


# Task 9: Password Strength Checker (basic)
# Take a password, check if it has:
#   - At least 8 characters
#   - At least 1 uppercase letter
#   - At least 1 digit
# Print "Strong" or "Weak" and reasons why.
password = "123456"

has_length = len(password) >= 8
has_uppercase = False
has_digits = False

for char in password:
    if char.isupper:
        has_uppercase = True
    if char.isdigit():
        has_digits = True

if has_length and has_digits and has_uppercase:
    print("Strong")
else:
    print("Weak")




# Task 10: Most Frequent Character
# Take a string, find which character appears the most.
# Example: "programming" → 'r' or 'g' or 'm' (any with count 2)
# Hint: Loop through string, use .count()

random_word = "programming"
word_count = {}

for i in random_word:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1

most_frequent = ""
highest_count = 0

for char in word_count:
    if word_count[char] > highest_count:
        highest_count = word_count[char]
        most_frequent = char

print("Most frequent character:", most_frequent)
print("Count:", highest_count)