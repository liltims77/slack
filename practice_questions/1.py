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


# | Use case                           | Use `len(list)`? | Use `len(list) - 1`? |
# | ---------------------------------- | ---------------- | -------------------- |
# | Loop through every item            | ✅ Yes            | ❌ No                 |
# | Access the last item using index   | ❌ No             | ✅ Yes                |
# | Compare item with the next one     | ❌ No             | ✅ Yes                |
# | Create a sliding window of size 2+ | ❌ No             | ✅ Yes                |


# 📌 What is a "Sliding Window"?
# A sliding window is a technique used to look at a fixed number of elements at a time (a "window") as you move across a list.

# For example, if we use a window size of 2, we look at two items at a time:

# First window: [1, 3]

# Slide forward → next window: [3, 5]

# Slide again → [5, 7]

# You’re just sliding across the list, looking at a fixed number of items each time.

#     my_list = ['a', 'b', 'c', 'd', 'e']
# # indexes:      0    1    2    3    4

# for i in range(len(my_list) - 2):
#     print(i, my_list[i])

# 🔍 Step-by-step breakdown:
# len(my_list) is 5 (because there are 5 elements).

# So range(len(my_list) - 2) becomes range(5 - 2) → range(3)

# That means i will take the values: 0, 1, and 2

# Let's see what the loop will print:

# When i = 0 → my_list[0] = 'a'

# When i = 1 → my_list[1] = 'b'

# When i = 2 → my_list[2] = 'c'

# 0 a
# 1 b
# 2 c
