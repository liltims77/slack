#write a function which takes an array of integers and 
# find the two items which sum to a given total and returns their product

# ([1, 2, 4, 8], 10) 2 * 8 = 16
# ([1721, 979, 366, 299, 675, 1456], 2020)  1721 * 299 = 514579

# an int array
# target value
# two numbers that sums to the target value
# returns the product of the two numbers

def get_product_of_two_numbers(numbers, target_value):
    numbers.sort()  # Step 1: Sort the array


    #left starts at the beginning of the list (index 0), 
    # and right starts at the end of the list (len(numbers) - 1). 
    # These pointers allow us to "scan" the array from both ends simultaneously.

    left = 0                  # Step 2: Initialize two pointers
    right = len(numbers) - 1

    while left < right:       # Step 3: Loop until the pointers meet
        current_sum = numbers[left] + numbers[right]  # Calculate the sum of the elements at the pointers

        if current_sum == target_value:               # Step 4: Check if we found the target sum
            return numbers[left] * numbers[right]
        elif current_sum < target_value:              # Step 5: Adjust the pointers based on the sum If current_sum < target_value, increase left by 1 (move right to increase the sum).
            left += 1
        else:
            right -= 1                                 # If current_sum > target_value, decrease right by 1 (move left to decrease the sum).

            # Sorting: numbers = [1, 2, 4, 8].
            # Pointer Initialization: left = 0, right = 3.
            # Iterations:
            # current_sum = 1 + 8 = 9 (Move left).
            # current_sum = 2 + 8 = 10 (Match found!).
            # Result: 2 * 8 = 16.
    return None   # If no such pair is found, return None



# Test case 1
print(get_product_of_two_numbers([1, 2, 4, 8], 10))  # Output: 16

# Test case 2
print(get_product_of_two_numbers([1721, 979, 366, 299, 675, 1456], 2020))
  # Output: 514579



# ([1, 2, 4, 8], 10) 2 * 8 = 16
  #brute force approach
def get_product_of_two_numbers(numbers, target_value):
    # Loop through each pair of numbers
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
        #This is a nested loop {for j in range(i + 1, len(numbers)), Begins at i + 1, where i is defined in an outer loop}
            if numbers[i] + numbers[j] == target_value:
                return numbers[i] * numbers[j]
            # Input: numbers = [1, 2, 4, 8], target_value = 10
            # Iterations:
            # (i=0, j=1): numbers[0] + numbers[1] = 1 + 2 = 3 (Not 10).
            # (i=0, j=2): numbers[0] + numbers[2] = 1 + 4 = 5 (Not 10).
            # (i=0, j=3): numbers[0] + numbers[3] = 1 + 8 = 9 (Not 10).
            # (i=1, j=2): numbers[1] + numbers[2] = 2 + 4 = 6 (Not 10).
            # (i=1, j=3): numbers[1] + numbers[3] = 2 + 8 = 10 (Match!).
            # Result: The function returns 2 * 8 = 16

    # If no pair is found, return None
    return None



# ([1, 2, 4, 8], 10) 2 * 8 = 16
# hash set approach
def get_product_of_two_numbers(numbers, target_value):
    # Create an empty set to store the numbers we have seen so far
    seen_numbers = set()

    # Loop through each number in the list
    for num in numbers:
        # Calculate the required complement
        complement = target_value - num

        # Check if the complement is in the set of seen numbers
        if complement in seen_numbers:
            # Return the product of the two numbers
            return num * complement
        
        # Add the current number to the set
        seen_numbers.add(num)

    # If no pair is found, return None
    return None
# Test case 1
print(get_product_of_two_numbers([1, 2, 4, 8], 10))  # Output: 16

# Test case 2
print(get_product_of_two_numbers([1721, 979, 366, 299, 675, 1456], 2020))  # Output: 514579


# In programming, "array" and "list" are both data structures used to store collections of elements, but they have some important differences depending on the language and context.
#  I'll explain the differences between arrays and lists in Python, as well as give examples.

# Key Differences Between Arrays and Lists in Python
# Data Type Restrictions:

# Array: All elements in an array must be of the same data type. For example, if it's an array of integers, it can only contain integers.
# List: A list can hold elements of different data types. For example, a list could contain an integer, a string, and a float all at once.



# When reading any input in Python using input(), the input is always initially received as a string, even if it represents a number.


#  len(arr) gives the total number of elements in arr
#  len(arr) - 1 the last index of an array


    
####### LEETCODE 
#Question 1: Sorted Squared Array - You are given an array of Integers in which each subsequent value is not less than the previous value. 
# Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending orde

def sorted_square_array(arr):
    # Initialize an empty list to store the squares
    squared_array = [0] * len(arr)

    # Two pointers, one at the start and one at the end of the array
    left = 0
    right = len(arr) - 1   # index of the last element

    # Fill the squared_array from the end to the beginning
    #range(start, stop, step)
    for i in range(len(arr)-1, -1, -1): # is a reverse loop that iterates through the indices of the array arr from the last index to the first index.
        #If you want the loop to include the first index (0), you should use: # for i in range(len(arr)-1, -1, -1):
        #If you want the loop to exclude the first index (0), you can use: # for i in range(len(arr)-1, 0, -1):
        
        if abs(arr[left]) > abs(arr[right]):
            squared_array[i] = arr[left] ** 2
            #Move the left pointer one step right (left += 1).
            left += 1
        else:
            squared_array[i] = arr[right] ** 2
            right -= 1
    return squared_array

arr = [-7, -3, 1, 5, 9]
arr = [1, 2, 3, 4, 5]
print(sorted_square_array(arr))  



# Question 2: Monotonic Array - An array is monotonic if it is either monotone increasing or monotone decreasing. 
# An array is monotone increasing if all its elements from left to right are non-decreasing. 
# An array is monotone decreasing if all  its elements from left to right are non-increasing. 
# Given an integer array return true if the given array is monotonic, or false otherwise.
def is_monotonic(arr):
    if len(arr) <= 1:
        return True # Arrays with 0 or 1 element are trivially monotonic
    
    # Determine if the array is increasing or decreasing
    is_increasing = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    is_decreasing = all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))

     # Return True if the array is either increasing or decreasing
    return is_increasing or is_decreasing

# Example usage:
print(is_monotonic([1, 2, 3, 3, 5]))  # Output: True (monotone increasing)
print(is_monotonic([5, 4, 3, 2, 1]))  # Output: True (monotone decreasing)
print(is_monotonic([1, 3, 2]))  # Output: False (not monotonic)




# Problem: Given an array of integers nums and an integer target, 
# return the indices of the two numbers that add up to the target.

# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]  
# # Because nums[0] + nums[1] = 2 + 7 = 9

def two_sum(nums, target):
    num_map = {} #store the numbers and their index
    #e.g [2, 7, 11, 15]
       #  0, 1, 2, 3

    for i, num in enumerate(nums):
        #eg 0 2, 
         # 1 7, 
         # 2 11, 
         # 3 15

        complement = target - num
        #eg 9 - 2 = 7

        if complement in num_map:
            #eg if 7 in Input: nums = [2, 7, 11, 15]

            return [num_map[complement], i]
            #If the complement is found, 
            #return the KEY which is the index of the complement
            #i.e return the index of 7 which is 1 and current index 0
            # it returns the indices of the two numbers that add up to the target.
        
        num_map[num] = i
        #If the complement is not found in num_map, this line adds the current
        #number num and its index i to the num_map dictionary. This way, if we
        #encounter the complement of this number later in the list, we can quickly look it up.
        
        return []
        #If the loop finishes without finding a pair of numbers that add up to the target, 
        # this line returns an empty list [], indicating that no solution was found.






# Problem: Given a string s containing just the characters (, ), {, }, [, and ], 
# determine if the input string is valid.

# Input: s = "()[]{}"
# Output: True

def is_valid(s):
    stack = []
    mapping = {")": "(",  "}":"{", "]":"["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

