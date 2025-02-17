def sorted_squared_array(arr):
    squared_arr = [x**2 for x in arr]

    squared_arr.sort()

    return squared_arr

input_arr = [1, 2, 3, 4, 5]
sorted_squared = sorted_squared_array(input_arr)
print(sorted_squared)