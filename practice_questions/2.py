
# distionary keys are immutable (they cannot be changed).
# there is no direct method to modify dictionary keys.
# How ever,  we can use pop() method to modify or create
# a new key for a value in the dictionary.

# EXAMPLE

# we want to change the key "school" to "university" in the dictionary below
#  The first step is to use the pop() method to remove the old keys and get its value.
#  the second step is to create a new key and assign it te value of te key we removed


my_dict = {'school': 'yale', 'age': 22}

# step 1: remove the old key and get the value
old_value = my_dict.pop('school')

# print(old_value) -->> yale

# step 2: create a new key with desired name and assign the value
my_dict['university'] = old_value
print(my_dict)
# assigning the value of old_value to the key 'university' in the dictionary my_dict. If the key already exists, its value gets updated; if not, it gets added.
# making university the key of the value old_value





# note  old_value = my_dict['university'] -->> This means you're retrieving the value associated with the 'university' key from the dictionary my_dict and storing it in the variable old_value.








