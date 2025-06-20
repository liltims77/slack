arr = [-4, -2, 1, 3, 5]
# for i in range(len(arr)-1, -1, -1):
#     print(i)
#     print(arr)
# #If you want the loop to include the first index (0),
# 4
# 3
# 2
# 1
# 0




# for i in range(len(arr)-1, 0, -1):
#     print(i)

# 4
# 3
# 2
# 1
#     print(arr)
#If you want the loop to exclude the first index (0),
    # Start from the index len(arr)-1 (last element).
    # Stop at 0 (exclusive—does not include 0).
    # Move backward (-1 as the step).
    # This means the loop will iterate in reverse, but it will stop before reaching index 0.

# In range(len(arr)-1, -1, -1), the stop is -1, so it includes 0 in the iteration.
# In range(len(arr)-1, 0, -1), the stop is 0 (exclusive), so the loop skips 0.





# for i in range(0,len(arr)+1, 2):
#     print(i)

# 0
# 2
# 4



for i in range(1,len(arr)+1, 2):
    print(i)

1
3
5



arr = [-4, -2, 1, 3, 5]
for i in range(0, len(arr)+2, 2):
    print(i)
0
2
4
6


# len(arr) is 5.
# This creates a range object, which generates numbers starting from 0, 
# up to but not including len(arr) + 2 = 7, stepping by 2.

# range(0, 7, 2) --->>>(start:stop:step)