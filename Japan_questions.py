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


#################################################################################################################################################
class INDDecMe:
    def __init__(self, capacity):
        #__init__ -> a constructor/ method tells python you want to create a new class
        """
        Initialize the LRU cache with given capacity
        
        Args:
            capacity (int): Maximum number of key-value pairs the cache can hold
        """
        self.capicity = capacity
        self.cache = {} # Dictionary to store key-value pairs
        self.order = [] # List to maintain the order of usage (most recent at end)
    

    # method to add or update a key-value pair in the cache
    def get(self, key): #refers to the newly created instance of the class which is key
        """
        Retrieve the value associated with the key from the cache
        
        Args:
            key (str): The key to look up in the cache
            
        Returns:
            int: The value associated with the key, or -1 if the key does not exist
        """
        if key in self.cache:
            # If key exists, update its usage frequency
            # self.order.remove(key)
            # self.order.append(key)
            self._update_usage(key)  # The underscore makes it clear it’s an internal method, not a public one.
            return self.cache[key]
        else:
            # If key does not exist, return -1
            return -1
        
# Is there a built-in self.update()?
# No ❌.
# Python doesn’t automatically give every class an update method.
# Only dict objects (like {"a": 1}) have .update() built in.
# No built-in update exists for their class.
# _update_usage is a custom helper function the programmer wrote.
# The underscore makes it clear it’s an internal method, not a public one.

# ✅ Rule
# Any method or variable that starts with a single underscore (e.g., _update_usage, _data, _helper) is considered internal/private by convention.
# It tells other programmers:
    
    def put(self, key, value):

        """
        Add or update a key-value pair in the cache
        
        Args:
            key (str): The key to add or update in the cache
            value (int): The value associated with the key
            
        Returns:
            None
        """
        if key in self.cache:
            # If key exists, update its value and usage frequency
            self.cache[key] = value
            # self.order.remove(key)
            # self.order.append(key)
            self._update_usage(key)
        else:
            # New key-value pair
            if len(self.cache) >= self.capacity:
                # Cache is full, remove least recently used item
                self._remove_lru()

            # Add new key-value pair
            self.cache[key] = value
            self.order.append(key)
    

    def _update_usage(self, key):
        """
        Update the usage order of a key (move to most recently used)
        
        Args:
            key (string): The key to update
        """
        # Remove key from current position and add to end (most recent)
        self.order.remove(key)
        self.order.append(key)
    
    def _remove_lru(self):
        """
        Remove the least recently used item from cache
        """
        if self.order:
            # Remove the first item (least recently used)
            lru_key = self.order.pop(0)
            del self.cache[lru_key]

    def display_cache(self):
        """
        Helper method to display current cache state (for debugging)
        """
        print("Cache contents:")
        for key in self.order:
            print(f"  {key}: {self.cache[key]}")
        print(f"Capacity: {len(self.cache)}/{self.capacity}")
        
# Example usage and testing
if __name__ == "__main__":
    # Create LRU cache with capacity of 3
    lru = INDDecMe(3)
    
    print("=== LRU Cache Demo ===")
    
    # Test putting values
    print("\n1. Adding key-value pairs:")
    lru.put("a", 1)
    lru.put("b", 2)
    lru.put("c", 3)
    lru.display_cache()
    
    # Test getting values
    print("\n2. Getting values:")
    print(f"get('a'): {lru.get('a')}")  # Should return 1 and move 'a' to most recent
    print(f"get('d'): {lru.get('d')}")  # Should return -1 (not found)
    lru.display_cache()
    
    # Test LRU eviction
    print("\n3. Adding new item (should evict LRU):")
    lru.put("d", 4)  # Should evict 'b' since 'a' was accessed recently
    lru.display_cache()
    
    # Test updating existing key
    print("\n4. Updating existing key:")
    lru.put("c", 30)  # Update value and move to most recent
    lru.display_cache()
    
    # Test more operations
    print("\n5. More operations:")
    print(f"get('c'): {lru.get('c')}")
    lru.put("e", 5)  # Should evict 'd'
    lru.display_cache()
    
    