# my_list = [1, 2, 2, 3, 4, 4, 5]

# write a one-line python expression to find the element that appear exactly once in a list of integers above

# your code must output:
# [1, 3, 5]


# solution

print([x for x in my_list if my_list.count(x) == 1])

# x for x in my_list goes through each number in the list.

# my_list.count(x) == 1 checks how many times x appears in the list — it only keeps the ones that appear once.

# The whole thing creates a new list with only those unique elements.
