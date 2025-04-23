# my_string = ['Love', 'Hope', 'Peace', 'Grace']

# Write a code to return the longest my_string
# in the list of strings above. If there is a tie,
# the code must return the string with the highest index.

my_string = ['Love', 'Hope', 'Peaceful', 'Grace']

# Initialize variables to track the longest string and its length
longest = ""
max_length = 0

# Loop through the list with index
for i in range(len(my_string)):
    current = my_string[i]
    # assign first element in the string to current ie current = 'Love'
    # For example, when i = 0, my_string[i] is 'Love'.
    if len(current) >= max_length:
    # if len(love) >= max_length ie if 4 >= 0
        longest = current
        # longest = love 
        max_length = len(current)
        # max_length = 4

print("Longest string:", longest)
