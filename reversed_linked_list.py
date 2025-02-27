# Write a function to reverse a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reversed_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


#This function reverses a singly linked list. We use three pointers: 
# prev, current, and next_node. We iterate through the list, 
# reversing the direction of the next pointers. 
# Finally, we return the new head of the reversed list



#What’s the difference between a stack and a queue

#"A stack is a Last-In-First-Out (LIFO) data structure, meaning the last element added is the first one to be removed. 
# It’s commonly used for tasks like undo operations or recursion. 
# A queue, on the other hand, is a First-In-First-Out (FIFO) data structure, where the first element added is the first one to be removed. 
# Queues are often used in scenarios like task scheduling or handling requests in a web server.






# Question: "How would you improve the performance of this algorithm?"
# Sample Answer (for a sorting algorithm):

# "If the algorithm is a basic bubble sort with O(n²) complexity, 
# I’d suggest using a more efficient algorithm like QuickSort or MergeSort, 
# which have O(n log n) complexity. Additionally, 
# I’d consider optimizing the implementation by reducing unnecessary comparisons or using in-place sorting to minimize memory usage. 
# If the data is partially sorted, 
# I might use Insertion Sort, which performs well in such cases.