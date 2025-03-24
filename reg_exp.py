
# 1️⃣ re.findall() → Find All Matches
# ✅ Finds all occurrences of a pattern in a string and returns a list of matches.
import re

text = "Email: hello@example.com, Contact: user123@gmail.com"
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

matches = re.findall(pattern, text)
print(matches)

# ✅ Output:
['hello@example.com', 'user123@gmail.com']




# 2️⃣ re.search() → Find First Match
#  Finds the first match of the pattern in a string and returns a match object.
import re

text = "My phone number is 123-456-7890"
pattern = r'\d{3}-\d{3}-\d{4}'  # Matches phone number format
# \d -->> matches any digit character(0-9)
# \D -->> matches non digit caracter  ('hello')

match = re.search(pattern, text)
print(match.group() if match else "No match found")

# ✅ Output:
123-456-7890





# 3️⃣ re.split() → Split a String by Pattern
# ✅ Splits a string wherever the pattern matches.

import re

text = "apple, banana; grape orange"
pattern = r'[,\s;]+'  # Split by comma, space, or semicolon
#  \s matches ant white spaces character (newline, space, tab) ('hello world')
#  \S matches ant white spaces character (newline, space, tab) ('hello_world')

words = re.split(pattern, text)
print(words)

# ✅ Output:
['apple', 'banana', 'grape', 'orange']





# 4️⃣ re.sub() → Replace Matches
# ✅ Replaces all occurrences of a pattern with another string.
import re

text = "My number is 123-456-7890."
pattern = r'\d'  # Matches any digit (0-9)

result = re.sub(pattern, '*', text)
print(result)


# ✅ Output:
# My number is ***-***-****.



# 5️⃣ re.subn() → Replace & Count
# ✅ Works like sub() but returns a tuple ((new_string, count_of_replacements)).
import re

text = "hello hello hello"
pattern = r'hello'

result = re.subn(pattern, "hi", text)
print(result)

# ✅ Output:
('hi hi hi', 3)





# 6️⃣ re.match() → Match at Start
# ✅ Checks if the string starts with the pattern.
import re

text = "hello world"
pattern = r'hello'

match = re.match(pattern, text)
print(match.group() if match else "No match")

# ✅ Output:
# hello




# 7️⃣ re.compile() → Precompile a Pattern
# ✅ Precompiles a regex pattern for repeated use.
import re

pattern = re.compile(r'\d{3}-\d{3}-\d{4}')  # Precompiled regex

text1 = "Call me at 123-456-7890"
text2 = "Another number: 987-654-3210"

print(pattern.search(text1).group())  # 123-456-7890
print(pattern.search(text2).group())  # 987-654-3210





# 8️⃣ re.escape() → Escape Special Characters
# ✅ Escapes all special regex characters in a string.

import re

text = "My website is https://example.com"
escaped_text = re.escape(text)

print(escaped_text)

# ✅ Output:

# My\ website\ is\ https\:\/\/example\.com



# Method	                                Description
# re.findall(pattern, text)	            Returns a list of all matches
# re.search(pattern, text)	            Returns the first match as a match object
# re.split(pattern, text)	                Splits the string at matches
# re.sub(pattern, replacement, text)	    Replaces matches with new text
# re.subn(pattern, replacement, text)	    Same as sub(), but also returns the number of replacements
# re.match(pattern, text)             	Checks if the string starts with the pattern
# re.compile(pattern)	                    Precompiles a regex for reuse (makes matching faster)
# re.escape(text)	                        Escapes all regex special characters

































