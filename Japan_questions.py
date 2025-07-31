# Design a data structure of LRU (Least Recently Used) cache using a class.

# LRU refers to a cache algorithm that removes the least recently used data from the cache.
# The timing of updating the frequency of use this time is when get and put are called.
# Please implement the INDDecMe class according to the following specifications.

# Constructor:

# INDDecMe(int list()

# Initialize the cache with a positive integer limit argument.

# methods:

# list get(string key)

# Returns the cache value associated with the key, if it exists, if it does not exist, return “-1.”

# If this method is called, update the usage frequency.

# void put(string key, int value)

# If the key exists, update the cache value associated with the key, if it does not exist, add a new key/value pair to the cache.

# If the limit given in the constructor is exceeded, the least recently unused key will be deleted.*

# If this method is called, update the usage frequency.