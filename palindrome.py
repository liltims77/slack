# Write a function to check if a string is a palindrome and return True if so.
# e.g. racecar is a palindrome, it's the same word backwards and forwards.

# Extension: Make it work for palindrome sentences e.g. Mr. Owl ate my metal worm


import re

def is_palindrome(s):
    # Normalize the string: remove non-alphanumeric characters and convert to lowercase
    normalized = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Check if the normalized string is the same forwards and backwards
    return normalized == normalized[::-1]

# Example usage:
print(is_palindrome("racecar"))  # True
print(is_palindrome("Mr. Owl ate my metal worm"))  # True
print(is_palindrome("Hello, World!"))  # False