my_list = []
def add_element(data_structure, element):
    if element in data_structure:
         data_structure.append(element)
    else:
        print(f"{element} not found in the list.")

add_element(my_list, 42)
add_element(my_list, 17)
add_element(my_list, 99)

print("current list:", my_list)

# print(f"current list: {my_list}")



