# Write a function to check if a string is a palindrome and return True if so.
# e.g. racecar is a palindrome, it's the same word backwards and forwards.

# Extension: Make it work for palindrome sentences e.g. Mr. Owl ate my metal worm


import re

def is_palindrome(s):
    
    # Normalize the string: remove non-alphanumeric characters and convert to lowercase
    normalized = re.sub(r'[^a-zA-Z0-9]', '', s).lower() #--->> ^ In this case stands nor NOT
    # This line of code check (a-zA-Z0-9 in the palindrome arugment eg (Mr. Owl ate my metal worm))
    # anything not related to (a-zA-Z0-9) is replaced with empty string ''
    # .lower() converts it into lower case
    # the re.sub() replaces and removes those empty string '' (anything from parameter not in (^a-zA-Z0-9) replce/sunstitute them with desired method eg '')
    
    # Check if the normalized string is the same forwards and backwards
    return normalized == normalized[::-1]

# Example usage:
print(is_palindrome("racecar"))  # True
print(is_palindrome("Mr. Owl ate my metal worm"))  # True
print(is_palindrome("Hello, World!"))  # False


# (^ inside the bracket)"Matches " means "finds" characters that fit the pattern.
# "Removes" happens when re.sub() replaces them with '' (nothing).


# Great question! Let's break it down step by step.

# A palindrome is a sequence of letters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

# Now, let's analyze:
# 👉 "Mr. Owl ate my metal worm"

# Remove spaces and punctuation

# "Mrowlatemymetalworm"
# Convert everything to lowercase

# "mrowlatemymetalworm"
# Compare it forward and backward

# Forward: "mrowlatemymetalworm"
# Backward: "mrowlatemymetalworm"

# Understanding r'[^a-zA-Z0-9]'
# This is a regular expression (regex) pattern. Let's go part by part:

# 1️⃣ a-zA-Z0-9
# a-z → Matches lowercase letters (a to z)
# A-Z → Matches uppercase letters (A to Z)
# 0-9 → Matches digits (0 to 9)
# 👉 So, a-zA-Z0-9 means "any letter or number"
# 2️⃣ [^...] (caret ^ inside square brackets)
# [...] means "match any of the characters inside the brackets."
# [^...] means "match anything that is NOT inside the brackets."
# The ^ inside [] negates the match.
# 3️⃣ Putting it together
# r'[^a-zA-Z0-9]' → Match any character that is NOT a letter or a digit
# This means it will match spaces, punctuation, and special characters (like , . ! ? @ # $ % ^ & *)




import re

text = "Hello123!"

# Remove ONLY the first letter if it's an alphabet
result = re.sub(r'^[a-zA-Z]', '', text) # extract the first letter (r'^[a-zA-Z]') if it is an alphabet and substitute it with nothing ie ('') --> ello123!
# r'^[a-zA-Z]' -->> means first letter --> ello123!
# r'[^a-zA-Z0-9]' -->> means the whole letter or string, or parameter or argument if it is an alphabet or number 0-9 -->> Hello



print(result)
