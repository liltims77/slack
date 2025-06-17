# ✅ What are Mutating Methods?
# Mutating methods are functions (usually tied to objects like lists or dictionaries) that change the original object directly, instead of creating a new one.
# ie. there is no need to pass a variable to them
# In simple terms:

# 🧪 A mutating method means: “I will change the object I'm called on.”


# 🔁 Examples of mutating methods in Python (for list):
# Method	            What it does	                     Mutating?
# .append(x)	        Adds x to the end	                 ✅ Yes
# .extend(iterable)	Adds multiple items	                 ✅ Yes
# .insert(i, x)	    Inserts x at index i	             ✅ Yes
# .remove(x)	        Removes first item equal to x	     ✅ Yes
# .pop(i)	            Removes and returns item at index i	 ✅ Yes
# .clear()	        Removes all items	                 ✅ Yes
# .sort()	            Sorts list in-place	                 ✅ Yes
# .reverse()	        Reverses list in-place               ✅ Yes




# ❌ Non-Mutating Methods (Don't change original)
# These return new values, leaving the original unchanged.
# ie. you can  pass a variable to them. they return a new values

# Function or Method	            Mutating?	        Example
# sorted(my_list)	                ❌ No	           Returns a new sorted list
# reversed(my_list)	            ❌ No	           Returns an iterator
# my_list[::-1]	                ❌ No	           Returns a reversed copy
# str.upper()	                    ❌ No	           Returns a new uppercase string
# str.replace("a", "b")	        ❌ No	           Returns a new string



# 🧠 Quick Rule to Remember
# If it ends with () and doesn't return a useful value (returns None), it's probably mutating.