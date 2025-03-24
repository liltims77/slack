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



##SELECTION SORT USING PYTHON
# This code is an example of the selection sort algorithm, which is used to sort a list of numbers in order (from smallest to largest).
def selection_sort(arr):
    # Loop over each position i in the array
    for i in range(len(arr)):
        # Assume the element at position i is the smallest (best)
        min_idx = i
        
        # Check the rest of the array (from i+1 to end)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                # Found a new best candidate, update min_idx
                min_idx = j
        
        # Swap the best candidate found with the element at position i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap the found min with the first unsorted element

arr = [64, 25, 12, 22, 11]
print("original array:", arr)
selection_sort(arr)
print("sorted array:", arr)

In the first pass (when i = 0), the initial value of min_idx is set to 0, which means it assumes that the first element of the array (arr[0] = 64) is the smallest.
First Pass (i = 0):
Initial min_idx = 0 (element = 64)
The inner loop (j = 1 to 4) compares arr[j] with arr[min_idx]:
arr[1] = 25 < arr[0] = 64 → Update min_idx = 1
arr[2] = 12 < arr[1] = 25 → Update min_idx = 2
arr[3] = 22 > arr[2] = 12 → No change
arr[4] = 11 < arr[2] = 12 → Update min_idx = 4
After the inner loop, min_idx = 4, meaning the smallest element in the remaining array is arr[4] = 11.

Swap arr[0] and arr[4]:
New array: [11, 25, 12, 22, 64]

So, in the first pass, min_idx is initially set to 0, but it is updated to 4 as the loop finds smaller elements.


First Pass (i = 0):
Start with i = 0, assume min_idx = 0 (first element is the smallest).

min_idx = 0, value = 64

Now, compare arr[j] with arr[min_idx] for j = 1 to 4:
Compare arr[1] = 25 with arr[min_idx] = 64
25 < 64, so update min_idx = 1
New min_idx = 1, value = 25
Compare arr[2] = 12 with arr[min_idx] = 25
12 < 25, so update min_idx = 2
New min_idx = 2, value = 12
Compare arr[3] = 22 with arr[min_idx] = 12
22 > 12, so min_idx remains 2
Compare arr[4] = 11 with arr[min_idx] = 12
11 < 12, so update min_idx = 4
New min_idx = 4, value = 11
After checking all elements, the smallest value found is arr[4] = 11.
Swap arr[0] and arr[4]:
Before swap: [64, 25, 12, 22, 11]
After swap: [11, 25, 12, 22, 64]





2️⃣ Selection Sort (Your Second Code)
It finds the smallest element in the unsorted part and swaps it with the first unsorted element.
It sorts the list by placing the smallest element in its correct position first.

Example of Selection Sort on [64, 25, 12, 22, 11]:
Pass 1: [11, 25, 12, 22, 64]  (11 is the smallest, swap with 64)
Pass 2: [11, 12, 25, 22, 64]  (12 is the next smallest, swap with 25)
Pass 3: [11, 12, 22, 25, 64]  (22 is the next smallest, swap with 25)
Pass 4: [11, 12, 22, 25, 64]  (Already sorted)


Before Selection Sort: [64, 25, 12, 22, 11]

Pass 1:
  Swapped 11 with 64: [11, 25, 12, 22, 64]  # Smallest element moved to first
Pass 2:
  Swapped 12 with 25: [11, 12, 25, 22, 64]  # Next smallest moved to second
Pass 3:
  Swapped 22 with 25: [11, 12, 22, 25, 64]  # Next smallest moved to third
Pass 4:
  Swapped 25 with 25: [11, 12, 22, 25, 64]  # Already correct
After Selection Sort: [11, 12, 22, 25, 64]







##BUBBLE SORTING IN PYTHON

for i in range(n):
    number_of_swaps = 0  # Reset the swap counter at the start of each pass
    for j in range(n - 1):  # Inner loop for swapping
        if arr[j] > arr[j + 1]:  # Compare adjacent elements
            arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap them if out of order
            number_of_swaps += 1  # Increment swap counter
    if number_of_swaps == 0:  # If no swaps happened, the list is sorted
        break


Before Bubble Sort: [64, 25, 12, 22, 11]

Pass 1:
  After comparing 25 and 64: [25, 64, 12, 22, 11]
  After comparing 12 and 64: [25, 12, 64, 22, 11]
  After comparing 22 and 64: [25, 12, 22, 64, 11]
  After comparing 11 and 64: [25, 12, 22, 11, 64]  # 64 is at the correct position

Pass 2:
  After comparing 12 and 25: [12, 25, 22, 11, 64]
  After comparing 22 and 25: [12, 22, 25, 11, 64]
  After comparing 11 and 25: [12, 22, 11, 25, 64]  # 25 is at the correct position

Pass 3:
  After comparing 12 and 22: [12, 22, 11, 25, 64]
  After comparing 11 and 22: [12, 11, 22, 25, 64]  # 22 is at the correct position

Pass 4:
  After comparing 11 and 12: [11, 12, 22, 25, 64]  # Sorted!

After Bubble Sort: [11, 12, 22, 25, 64]

Final Thoughts
Bubble Sort swaps elements a lot but is good if the list is almost sorted.
Selection Sort is better if swaps are costly because it only swaps once per pass.
Both are slow for large lists; Quick Sort or Merge Sort are better for big data.  
Bubble Sort → Compares and swaps adjacent elements repeatedly. Moves large elements up gradually. 🔄
Selection Sort → Finds the smallest element and moves it directly to its correct position. ✅
Selection Sort is usually faster than Bubble Sort because it makes fewer swaps.
Bubble Sort is useful when the list is nearly sorted because it can stop early.


Which is Better?
If you want fewer swaps: 🏆 Selection Sort is better (because it moves elements directly to their final position).
If you want a stable sort (preserves order of equal elements): 🏆 Bubble Sort is better.
If the list is already nearly sorted: 🏆 Optimized Bubble Sort is faster.
For large lists, neither is good: Both have 
𝑂(𝑛2)O(n 2) time complexity, which is slow. Instead, use Merge Sort or Quick Sort.



##QUICK SORT

1️⃣ Quick Sort (Divide and Conquer)
Picks a pivot (usually the last or first element).
Partitions the array so that:
Elements smaller than the pivot go to the left.
Elements greater than the pivot go to the right.
Recursively sorts the left and right parts.

def quick_sort(arr):
    if len(arr) <= 1:  # Base case: Already sorted
        return arr
    
    pivot = arr[len(arr) - 1]  # Choose last element as pivot
    left = [x for x in arr[:-1] if x <= pivot]  # Elements ≤ pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements > pivot
    
    print(f"Pivot: {pivot} | Left: {left} | Right: {right}")  # Show partitioning
    return quick_sort(left) + [pivot] + quick_sort(right)  # Recursively sort

# Example
arr1 = [64, 25, 12, 22, 11]
print("Before Quick Sort:", arr1)
sorted_arr = quick_sort(arr1)
print("After Quick Sort:", sorted_arr)

Before Quick Sort: [64, 25, 12, 22, 11]

Pivot: 11 | Left: [] | Right: [64, 25, 12, 22]  
Pivot: 22 | Left: [12] | Right: [64, 25]  
Pivot: 25 | Left: [] | Right: [64]  
After Quick Sort: [11, 12, 22, 25, 64]

🔹 Quick Sort splits the list into smaller parts and sorts them recursively.




2️⃣ Merge Sort (Divide and Merge)
Divides the array into two halves.
Recursively sorts both halves.
Merges them back together in sorted order.

def merge_sort(arr):
    if len(arr) <= 1:  # Base case: Already sorted
        return arr
    
    mid = len(arr) // 2  # Find the middle
    left = merge_sort(arr[:mid])  # Recursively sort left half
    right = merge_sort(arr[mid:])  # Recursively sort right half
    
    merged = merge(left, right)
    print(f"Merging: {left} + {right} -> {merged}")  # Show merging step
    return merged

def merge(left, right):
    sorted_arr = []
    i = j = 0
    
    while i < len(left) and j < len(right):  # Merge two sorted lists
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    sorted_arr.extend(left[i:])  # Add remaining elements
    sorted_arr.extend(right[j:])
    
    return sorted_arr

# Example
arr2 = [64, 25, 12, 22, 11]
print("Before Merge Sort:", arr2)
sorted_arr2 = merge_sort(arr2)
print("After Merge Sort:", sorted_arr2)



Before Merge Sort: [64, 25, 12, 22, 11]

Merging: [64] + [25] -> [25, 64]  
Merging: [12] + [22] -> [12, 22]  
Merging: [12, 22] + [11] -> [11, 12, 22]  
Merging: [25, 64] + [11, 12, 22] -> [11, 12, 22, 25, 64]
After Merge Sort: [11, 12, 22, 25, 64]
🔹 Merge Sort breaks the list in half, sorts each half, then merges them back in order.



🔍 Comparing Sorting Algorithms
Algorithm	    Time Complexity (Worst)	    Best for?
Bubble Sort	    O(n²)	                    Small nearly sorted lists
Selection Sort	O(n²)	                    Small lists, fewer swaps
Quick Sort	    O(n log n)	                Large lists, efficient for random data
Merge Sort	    O(n log n)	                Consistent performance, best for linked lists

