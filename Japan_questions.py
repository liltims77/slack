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
        # capacity is a value you pass when you create the object
        self.capacity = capacity
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
            # return self.cache[key]
            return [str(self.cache[key])] # return the value from the cachee as a list to match the requirement of returning value as a list ["value"]
            # Then [ ... ] → put that value inside a list.
        else:
            # If key does not exist, return -1
            # return -1
            return ["-1"] # return -1 as a list to match the requirement of returnig " -1 " (string) if key does not exist
        
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

# If the limit given in the constructor is exceeded, the least recently unused key will be deleted.*
    
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



# ##############################################################################################################################################################
class INDDecMe:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []
        
    def get(self, key):
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        else:
            return -1
            
    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache) >= self.capacity:
                self._remove_lru()
            
            self.cache[key] = value
            self.order.append(key)
            
    def _remove_lru(self):
        if self.order:
            lru_key = self.order.pop(0)
            del self.cache[lru_key]



# ##############################################################################################################################################################
# Three Implementation Approaches:
# 1. Simple Dictionary (Python 3.7+)

# Uses the fact that Python dictionaries maintain insertion order
# Clean and readable code
# O(1) average time complexity

# 2. OrderedDict

# More explicit about ordering semantics
# Has convenient move_to_end() method
# Clear intent for LRU operations

# 3. Doubly Linked List + HashMap (Most Optimal)

# 4. HashMap + List hybrid that's conceptually sound but doesn't meet the O(1) 
# time complexity requirement. The fundamental issue is that maintaining order
#  with a list requires O(n) operations for removal and shifting.

# True O(1) worst-case time complexity
# Uses a hash map for O(1) lookups and a doubly linked list for O(1) insertion/deletion
# More complex but most efficient for large-scale applications


# ##############################################################################################################################################################

class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with given capacity.
        Uses OrderedDict for O(1) operations.
        """
        self.capacity = capacity
        self.cache = {}  # Using regular dict (Python 3.7+ maintains insertion order)
    
    def get(self, key: int) -> int:
        """
        Get value by key. If key exists, move it to end (most recently used).
        Returns -1 if key doesn't exist.
        Time Complexity: O(1)
        """
        if key in self.cache:
            # Remove and re-insert to move to end (most recent)
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        return -1
    
    def put(self, key: int, value: int) -> None:
        """
        Put key-value pair. If key exists, update and move to end.
        If cache is full and key is new, remove least recently used item.
        Time Complexity: O(1)
        """
        if key in self.cache:
            # Key exists - remove and re-insert with new value
            self.cache.pop(key)
            self.cache[key] = value
        else:
            # New key
            if len(self.cache) >= self.capacity:
                # Cache is full - remove least recently used (first item)
                self.cache.pop(next(iter(self.cache)))
            self.cache[key] = value


# Alternative implementation using collections.OrderedDict for clarity
from collections import OrderedDict

class LRUCacheOrderedDict:
    def __init__(self, capacity: int):
        """
        Initialize the LRU cache using OrderedDict for explicit ordering.
        """
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        """
        Get value by key and move to end (most recently used).
        """
        if key in self.cache:
            # Move to end by removing and re-inserting
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    
    def put(self, key: int, value: int) -> None:
        """
        Put key-value pair. Update existing or add new.
        """
        if key in self.cache:
            # Update existing key and move to end
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            # Add new key
            if len(self.cache) >= self.capacity:
                # Remove least recently used (first item)
                self.cache.popitem(last=False)
            self.cache[key] = value


# Most efficient implementation using doubly linked list + hash map
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCacheOptimal:
    def __init__(self, capacity: int):
        """
        Initialize with doubly linked list + hash map for true O(1) operations.
        """
        self.capacity = capacity
        self.cache = {}  # key -> node
        
        # Create dummy head and tail nodes
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node):
        """Add node right after head."""
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        """Remove an existing node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _move_to_head(self, node):
        """Move node to head (most recently used)."""
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        """Remove last node before tail (least recently used)."""
        last_node = self.tail.prev
        self._remove_node(last_node)
        return last_node
    
    def get(self, key: int) -> int:
        """Get value and mark as most recently used."""
        node = self.cache.get(key)
        
        if node:
            # Move to head (most recently used)
            self._move_to_head(node)
            return node.value
        
        return -1
    
    def put(self, key: int, value: int) -> None:
        """Put key-value pair."""
        node = self.cache.get(key)
        
        if node:
            # Update existing node
            node.value = value
            self._move_to_head(node)
        else:
            # Add new node
            new_node = Node(key, value)
            
            if len(self.cache) >= self.capacity:
                # Remove least recently used
                tail = self._pop_tail()
                del self.cache[tail.key]
            
            self.cache[key] = new_node
            self._add_node(new_node)


# Your approach (HashMap + List) - O(n) time complexity
class INDDecMe:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []  # This causes O(n) operations
        
    def get(self, key):
        if key in self.cache:
            self.order.remove(key)  # O(n) operation!
            self.order.append(key)
            return self.cache[key]
        else:
            return -1
            
    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.order.remove(key)  # O(n) operation!
            self.order.append(key)
        else:
            if len(self.cache) >= self.capacity:
                self._remove_lru()
            
            self.cache[key] = value
            self.order.append(key)
            
    def _remove_lru(self):
        if self.order:
            lru_key = self.order.pop(0)  # O(n) operation!
            del self.cache[lru_key]


# Improved version using deque (still not perfect for LRU)
from collections import deque

class LRUCacheDeque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = deque()  # Better for pop(0), but remove() is still O(n)
        
    def get(self, key):
        if key in self.cache:
            self.order.remove(key)  # Still O(n)!
            self.order.append(key)
            return self.cache[key]
        return -1
            
    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.order.remove(key)  # Still O(n)!
            self.order.append(key)
        else:
            if len(self.cache) >= self.capacity:
                lru_key = self.order.popleft()  # O(1) now
                del self.cache[lru_key]
            
            self.cache[key] = value
            self.order.append(key)


# Test the implementations
def test_lru_cache():
    print("Testing LRU Cache implementations...")
    
    # Test with the provided example
    lru = LRUCache(2)
    
    lru.put(1, 1)  # cache: {1=1}
    lru.put(2, 2)  # cache: {1=1, 2=2}
    print(f"get(1): {lru.get(1)}")  # returns 1, cache: {2=2, 1=1}
    
    lru.put(3, 3)  # evicts key 2, cache: {1=1, 3=3}
    print(f"get(2): {lru.get(2)}")  # returns -1 (not found)
    
    lru.put(4, 4)  # evicts key 1, cache: {3=3, 4=4}
    print(f"get(1): {lru.get(1)}")  # returns -1 (not found)
    print(f"get(3): {lru.get(3)}")  # returns 3
    print(f"get(4): {lru.get(4)}")  # returns 4

if __name__ == "__main__":
    test_lru_cache()
    
    