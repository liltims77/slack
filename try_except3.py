import math

def calc(num):
    try:
        result = num / num - 5
        #eturn result
        print (f"Result: {result}")
        
    except Exception as e:
        print("An error occurred during calculation.")

user_input = float(input("Enter a number: "))
calc(user_input)