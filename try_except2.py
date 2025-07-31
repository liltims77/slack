import math

def square_root(number1):
    try:
        result = math.sqrt(number1)
        print(f"Result: {result}")
        #return result
    except ValueError:
        print("Error: Invalid input! Please enter a positive integer or a float value.")
number1=float(input("Enter the number:-"))
square_root(number1)
#print(square_root(number1))