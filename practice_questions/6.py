
# List of records (dictionaries)

# Example: Filtering people who are 18 or older
people = [
    {'name': 'Tim', 'age': 25},
    {'name': 'Sarah', 'age': 17},
    {'name': 'John', 'age': 19},
    {'name': 'Emma', 'age': 16}
]

# Loop through the records
for record in people:
    # Access the value of 'age' in each record
    age = record['age']
    
    # Check if the person is 18 or older
    if age >= 18:
        print(f"{record['name']} is {age} years old and eligible.")
    else:
        print(f"{record['name']} is {age} years old and not eligible.")


# Output:
# Tim is 25 years old and eligible.
# Sarah is 17 years old and not eligible.
# John is 19 years old and eligible.
# Emma is 16 years old and not eligible.

# record['age'] accesses the value of the age key in each dictionary (record).

my_dict = {'name': 'Tim', 'age': 25}

# Using .keys() and .values()
for key in my_dict.keys():
    value = my_dict[key]
    print(key, value)



