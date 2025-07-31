# write a function that takes nested dictionary where the inner dictionaries represents
# items and their prices in different stores, and returns a new dictionary with items as
# keys and the stores with the lowest price as the value. for example, the fruit_stores
# nested dictionary should output: {'apple': 'store1', 'banana':'store2'}

fruit_stores = {'apple':{'store1': 1.0, 'store2': 1.5},
                'banana':{'store1':2.0, 'store2':1.8}
                }           

def find_lowest_price_stores(fruit_stores):
    lowest_price_stores = {}

    for item, stores in fruit_stores.items():
        # print(item, stores) 
        # output below
        # apple {'Store1': 1.0, 'Store2': 1.5}
        # banana {'Store1': 2.0, 'Store2': 1.8}
            # item is the fruit name like "apple".
            # stores is a dictionary of store names and their prices for that fruit.


        # Find the store with the minimum price
        lowest_store = min(stores, key=stores.get)
        # why min(stores, key=stores.get)?  min() requires 2 arguments
        lowest_price_stores[item] = lowest_store
         # Set the lowest store as the value in the new dictionary using the item as the key
    return lowest_price_stores

print(find_lowest_price_stores(fruit_stores))

# OUTPUT : {'apple': 'store1', 'banana': 'store2'}


# .items() gives you both keys and values together.
# for item, stores in fruit_stores.items():
#     print("Item:", item)
#     print("Stores and prices:", stores)

# Without .items()
# for key in fruit_stores:
#     print(key)
# So, .items() helps you loop through both the fruit name and its store prices at the same time.





my_dict = {'name': 'Tim', 'age': 25}

# Using .keys() and .values()
for key in my_dict.keys():
    value = my_dict[key]
    print(key, value)
