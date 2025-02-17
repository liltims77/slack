arr = [-4, -2, 1, 3, 5]
for i in range(len(arr)-1, -1, -1):
    print(i)
    print(arr)
#If you want the loop to include the first index (0),





# for i in range(len(arr)-1, 0, -1):
#     print(i)
#If you want the loop to exclude the first index (0),
    # Start from the index len(arr)-1 (last element).
    # Stop at 0 (exclusive—does not include 0).
    # Move backward (-1 as the step).
    # This means the loop will iterate in reverse, but it will stop before reaching index 0.

# In range(len(arr)-1, -1, -1), the stop is -1, so it includes 0 in the iteration.
# In range(len(arr)-1, 0, -1), the stop is 0 (exclusive), so the loop skips 0.

