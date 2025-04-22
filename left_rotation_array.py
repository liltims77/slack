# Problem Statement: Left Rotation on a Circular Array
# A left rotation operation on a circular array shifts each of the array's elements 1 unit to the left. Elements that fall off the left end reappear at the right end. Given an integer d, rotate the array d steps to the left and return the result.

# Example:
# Input: arr = [1, 2, 3, 4, 5], d = 2

# Output: [3, 4, 5, 1, 2]

# Explanation:
# After 1 rotation: [2, 3, 4, 5, 1]

# After 2 rotations: [3, 4, 5, 1, 2]

# Function Description:
# Complete the rotateLeft function in the editor below.

# Parameters:
# d: An integer, the number of steps to rotate the array.

# arr: A list of integers, the array to rotate.

# Returns:
# A list of integers, the rotated array.

# Input Format:
# The first line contains two space-separated integers:

# n: The number of elements in the array.

# d: The number of steps to rotate the array.

# The second line contains n space-separated integers, the elements of the array.

# Constraints:







###################################################################
# SOLUTION
def rotateLeft(d, arr):
    if not arr or d == 0:
    # If the array is empty (has no elements), there’s nothing to rotate, so we return the array as is
    # d == 0: If d is 0, it means no rotation is needed, so we return the array as is.
        return arr
    
    # Normalize d to be within the range of the array length
    d = d % len(arr)
    #     This line normalizes the value of d.

    # The % operator is called the modulo operator. It gives the remainder when d is divided by the length of the array (len(arr)).

    # For example:

    # If d = 7 and the array length is 5, then d % len(arr) is 2 (because 7 divided by 5 leaves a remainder of 2).

    # This ensures that d is always within the range of the array length, even if d is larger than the array length.
    
    # Perform the rotation using slicing
    rotated_arr = arr[d:] + arr[:d]
    #     This line performs the rotation:

    # arr[d:]: This slices the array starting from index d to the end. For example, if arr = [1, 2, 3, 4, 5] and d = 2, then arr[d:] gives [3, 4, 5].

    # arr[:d]: This slices the array from the start up to (but not including) index d. For the same example, arr[:d] gives [1, 2].

    # The + operator concatenates (combines) these two slices. So, [3, 4, 5] + [1, 2] results in [3, 4, 5, 1, 2].
    
    return rotated_arr
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


# Slicing in Python:
# arr[start:end]:

# start: The index where the slice begins (inclusive).

# end: The index where the slice ends (exclusive).

# The slice includes all elements from start up to, but not including, end.

# arr[start:]:

# If end is omitted, the slice goes from start to the end of the array.

# arr[:end]:

# If start is omitted, the slice goes from the beginning of the array up to, but not including, end.

# Examples:
# Let’s use the array arr = [10, 20, 30, 40, 50] to demonstrate slicing:

# 1. arr[3:]:
# This means "slice the array from index 3 to the end."

# Index 3 is inclusive, so it includes the element at index 3.

# Result: [40, 50]

# 2. arr[:3]:
# This means "slice the array from the start up to, but not including, index 3."

# Index 3 is exclusive, so it stops at index 2.

# Result: [10, 20, 30]

# 3. arr[1:4]:
# This means "slice the array from index 1 to index 4."

# Index 1 is inclusive, and index 4 is exclusive.

# Result: [20, 30, 40]

# 4. arr[:]:
# This means "slice the entire array."

# Result: [10, 20, 30, 40, 50]



