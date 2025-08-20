"""Decorators in Python are a powerful tool that allows you to 
modify or enhance the behavior of functions 
or classes without changing their actual code. 
Essentially, a decorator is a higher-order function 
(a function that takes another function as an argument and returns a new function) 
that wraps around the original function to add extra functionality"""

# Decorators add functionalities to an existing code

## A decorator takes another function as an agrument, then defines an inner function
#called a wrapper that executes codes before or after calling the original function


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

# Calling the decorated function
say_hello("Alice")

###################### Explanation:

# Defining the Decorator:
# my_decorator is a function that takes another function func as its argument.

# The Wrapper Function:
# Inside my_decorator, we define wrapper, which:

# Prints a message before calling the original function.
# Calls the original function with any arguments it receives.
# Prints another message after the function call.
# Returns the result of the original function call.
# Applying the Decorator:
# The line @my_decorator above say_hello is shorthand for:
# say_hello = my_decorator(say_hello)
# when you call say_hello("Alice"), it actually calls the wrapper function.




# Why Use Decorators?
# Decorators are commonly used to:

#1. Add Logging: Track when functions are called.
#2. Access Control: Verify user permissions before executing a function.
#3. Caching/Memoization: Store results of expensive function calls.
#4. Validation: Check function input or output.
#5. Timing: Measure the execution time of a function.



# Built-in Decorators
# Python comes with some built-in decorators that are very useful:

# 1. @staticmethod and @classmethod: Used in class definitions 
#   to define methods that are independent of class instances 
#   or that need to operate on the class itself.
# 2. @property: Allows you to access methods like attributes, 
#   typically used to define getters and setters for class attributes.



# Advanced Decorators
# Decorators can also accept arguments. 
# This requires an extra layer of function definitions, 
# effectively turning the decorator into a decorator factory.

# def repeat(num_times):
#     def decorator_repeat(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeat

# @repeat(3)
# def greet(name):
#     print(f"Hello, {name}!")

# greet("Bob")


# In this example:

# repeat is a function that takes an argument (num_times).
# It returns the actual decorator decorator_repeat, which then wraps the function greet.
# When you call greet("Bob"), it will print the greeting three times.
