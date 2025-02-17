# def func(lst):
#     lst[0] = 1
#     return x
# x = [0, 1, 2, 3]
# print(func(x))


##tuple

#In Python, tuples are immutable, meaning their elements cannot be modified after creation. So if you want to modify the elements of a tuple, you need to convert it to a mutable data type, like a list, where you can change individual elements.

def func(tpl):
    lst = list(tpl)  # Convert tuple to a list to modify it
    lst[0] = 1       # Modify the first element
    return tuple(lst)  # Convert the modified list back to a tuple and return it

x = (0, 1, 2, 3)  # Define x as a tuple
print(func(x))


