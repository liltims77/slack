# my_string = 'Hello'

# write a code  to reverse the string only if all elements are unique.
# otherwise, return the duplicates. Do not use reversed() function.

def reverse_or_find_duplicates(s):
    char_count = {}
    duplicates = set()
    
    # Count occurrences of each character
    for char in s:
        if char in char_count:
            duplicates.add(char)
        char_count[char] = char_count.get(char, 0) + 1
    
    # If there are duplicates, return them; otherwise, reverse the string
    if duplicates:
        return ''.join(sorted(duplicates))
    else:
        reversed_string = ''
        for i in range(len(s) - 1, -1, -1):  # Manually reversing the string
            reversed_string += s[i]
        return reversed_string

# Example usage
my_string = 'Hello'
print(reverse_or_find_duplicates(my_string))  # Output: 'l'

my_string = 'World'
print(reverse_or_find_duplicates(my_string))  # Output: 'dlroW'