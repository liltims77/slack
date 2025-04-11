# my_string = ['Love', 'Hope', 'Peace', 'Grace']

# Write a code to return the longest my_string
# in the list os strings above. If there is a tie,
# the code must return the string with the highest index.

my_string = ['Love', 'Hope', 'Peace', 'Grace']

# Initialize variables to track the longest string and its length
longest = ""
max_length = 0

# Loop through the list with index
for i in range(len(my_string)):
    current = my_string[i]
    if len(current) >= max_length:
        longest = current
        max_length = len(current)

print("Longest string:", longest)
