# # ✅ What are Mutating Methods?
# # Mutating methods are functions (usually tied to objects like lists or dictionaries) that change the original object directly, instead of creating a new one.
# # ie. there is no need to pass a variable to them
# # In simple terms:

# # 🧪 A mutating method means: “I will change the object I'm called on.”


# # 🔁 Examples of mutating methods in Python (for list):
# | Method              | What it does                          | Mutating? |
# | ------------------- | ------------------------------------- | --------- |
# | `.append(x)`        | Adds `x` to the end                   | ✅ Yes     |
# | `.extend(iterable)` | Adds multiple items                   | ✅ Yes     |
# | `.insert(i, x)`     | Inserts `x` at index `i`              | ✅ Yes     |
# | `.remove(x)`        | Removes first item equal to `x`       | ✅ Yes     |
# | `.pop(i)`           | Removes and returns item at index `i` | ✅ Yes     |
# | `.clear()`          | Removes all items                     | ✅ Yes     |
# | `.sort()`           | Sorts list in-place                   | ✅ Yes     |
# | `.reverse()`        | Reverses list in-place                | ✅ Yes     |





# # ❌ Non-Mutating Methods (Don't change original)
# # These return new values, leaving the original unchanged.
# # ie. you can  pass a variable to them. they return a new values

# | Function or Method      | Mutating? | Example                        |
# | ----------------------- | --------- | ------------------------------ |
# | `sorted(my_list)`       | ❌ No      | Returns a new sorted list      |
# | `reversed(my_list)`     | ❌ No      | Returns an iterator            |
# | `my_list[::-1]`         | ❌ No      | Returns a reversed copy        |
# | `str.upper()`           | ❌ No      | Returns a new uppercase string |
# | `str.replace("a", "b")` | ❌ No      | Returns a new string           |




# # 🧠 Quick Rule to Remember
# # If it ends with () and doesn't return a useful value (returns None), it's probably mutating.








# 📚 Useful Methods by Data Type
# 🔹 List Methods

# | Action          | Method               | Mutates? | Returns?   |
# | --------------- | -------------------- | -------- | ---------- |
# | Add 1 item      | `list.append(x)`     | ✅ Yes    | `None`     |
# | Add multiple    | `list.extend([x,y])` | ✅ Yes    | `None`     |
# | Insert item     | `list.insert(i, x)`  | ✅ Yes    | `None`     |
# | Remove by value | `list.remove(x)`     | ✅ Yes    | `None`     |
# | Remove by index | `list.pop(i)`        | ✅ Yes    | ✅ Item     |
# | Reverse         | `list.reverse()`     | ✅ Yes    | `None`     |
# | Get reversed    | `reversed(list)`     | ❌ No     | ✅ Iterator |
# | Sort            | `list.sort()`        | ✅ Yes    | `None`     |
# | Get sorted copy | `sorted(list)`       | ❌ No     | ✅ List     |





# 🔹 Dictionary Methods
# | Action               | Method                | Returns         |
# | -------------------- | --------------------- | --------------- |
# | Get value by key     | `dict.get("key")`     | Value or `None` |
# | Add/update key-value | `dict["key"] = value` | ✅ In-place      |
# | Remove by key        | `dict.pop("key")`     | ✅ Value         |
# | All keys             | `dict.keys()`         | dict\_keys      |
# | All values           | `dict.values()`       | dict\_values    |
# | All key-value pairs  | `dict.items()`        | dict\_items     |
# | Remove all items     | `dict.clear()`        | `None`          |




# 1️⃣ Built-in array Module
# 📚 Common array methods:
# | Method              | What it does                           | Mutates? | Returns |
# | ------------------- | -------------------------------------- | -------- | ------- |
# | `.append(x)`        | Adds item `x` at the end               | ✅ Yes    | `None`  |
# | `.insert(i, x)`     | Inserts `x` at position `i`            | ✅ Yes    | `None`  |
# | `.pop(i)`           | Removes and returns item at index `i`  | ✅ Yes    | ✅ Item  |
# | `.remove(x)`        | Removes the first item equal to `x`    | ✅ Yes    | `None`  |
# | `.reverse()`        | Reverses the array                     | ✅ Yes    | `None`  |
# | `.tolist()`         | Converts array to Python list          | ❌ No     | ✅ List  |
# | `.buffer_info()`    | Returns memory address + element count | ❌ No     | ✅ Tuple |
# | `.count(x)`         | Counts how many times `x` appears      | ❌ No     | ✅ Int   |
# | `.extend(iterable)` | Appends items from iterable            | ✅ Yes    | `None`  |




# 📚 Common NumPy ndarray methods:
# | Method                          | What it does                       | Returns               |
# | ------------------------------- | ---------------------------------- | --------------------- |
# | `.reshape()`                    | Changes shape                      | ✅ New array           |
# | `.flatten()`                    | Flattens multi-dimensional array   | ✅ New array           |
# | `.astype(type)`                 | Changes data type                  | ✅ New array           |
# | `.sum()`                        | Sums all elements                  | ✅ Scalar              |
# | `.mean()`                       | Mean value                         | ✅ Scalar              |
# | `.max()` / `.min()`             | Maximum / minimum value            | ✅ Scalar              |
# | `.sort()`                       | Sorts array in-place **(1D only)** | ✅ New view            |
# | `.copy()`                       | Makes a full copy                  | ✅ New array           |
# | `.transpose()`                  | Switches rows and columns (matrix) | ✅ New array           |
# | `.argmax()` / `.argmin()`       | Index of max/min value             | ✅ Index               |
# | `.dot()`                        | Dot product                        | ✅ New array or scalar |
# | `.append()` (via `np.append()`) | Adds values to array               | ✅ New array           |
# ⚠ NumPy methods often don’t mutate the array. They return new arrays instead (unlike Python lists).



# 🔹 String Methods (strings are immutable!)
# | Action                     | Method                  | Returns         |
# | -------------------------- | ----------------------- | --------------- |
# | Convert to uppercase       | `str.upper()`           | ✅ New string    |
# | Convert to lowercase       | `str.lower()`           | ✅ New string    |
# | Remove whitespace          | `str.strip()`           | ✅ New string    |
# | Replace substrings         | `str.replace("a", "b")` | ✅ New string    |
# | Split into list            | `str.split(" ")`        | ✅ List          |
# | Join list into string      | `" ".join(list)`        | ✅ String        |
# | Find position of substring | `str.find("word")`      | ✅ Index (or -1) |



# 🧠 How to Remember or Look Up Methods
# 1. ✅ Use Python’s dir() function to list methods:
# print(dir(str))      # all string methods
# print(dir(list))     # all list methods
# print(dir(dict))     # all dict methods

# 2. ✅ Use built-in help system:
# help(list.append)
# help(str.replace)
# help(dict.pop)

