# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# Example






# : Append  to the list, .
# : Append  to the list, .
# : Insert  at index , .
# : Print the array.
# Output:
# [1, 3, 2]
# Input Format

# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.

# Constraints

# The elements added to the list must be integers.
# Output Format

# For each command of type print, print the list on a new line.

# Sample Input 0

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output 0

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]



# SOLUTION

if __name__ == '__main__':
    # Read the number of commands
    N = int(input())

    # Initialize an empty list
    lst = []

    # Iterate through each command
    # In Python, for _ in range(N): is a loop that runs N times, executing the block of code inside it on each iteration.
    # range(N): Generates a sequence of numbers from 0 to N-1 (i.e., 0, 1, 2, ..., N-1).
    # for _ in range(N): Loops through this sequence N times.
    # The underscore (_) is used when the loop variable is not needed.
    # In this case, we don’t need to reference the loop index inside the loop. We just want to execute the commands N times.
    for _ in range(N):
        command = input().split()
        # split record in each line
        
        # Execute the corresponding operation
        if command[0] == "insert":
            lst.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(lst)
        elif command[0] == "remove":
            lst.remove(int(command[1]))
        elif command[0] == "append":
            lst.append(int(command[1]))
        elif command[0] == "sort":
            lst.sort()
        elif command[0] == "pop":
            lst.pop()
        elif command[0] == "reverse":
            lst.reverse()
