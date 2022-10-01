class LRUCache(object):
    def __init__(self, capacity):
        """
        :param capacity: the maximum capacity of the LRU cache
        """
        # Data structure <=> Hash Map, Queue

        # Each LRU cache element will be a key - value pair and the LRU cache itself will be the hash map
        # Key <=> the element's key
        # Value <=> the element's value
        # Hash function <=> H(key) = value

        # Time complexity <=> O(1)
        # Space complexity <=> O(2 * n), where n is the current number of elements in the LRU cache

        # Define a number which represents the LRU cache's maximum capacity (the maximum number of
        # Elements it can hold)
        self.capacity = capacity

        # Define a hash map which represents the LRU cache
        self.hash_map = dict()

        # Define a queue which stores the added keys and whose first element is the one
        # That will be evicted first
        self.keys = []

    def get(self, key):
        """
        :param key: the number corresponding to the key of the element to be returned from the LRU cache
        :return: the value associated to the given key, if the key exists and -1, otherwise
        """
        # Time complexity <=> O(1)
        # Space complexity <=> O(2 * n), where n is the current number of elements in the LRU cache

        # If there is a key equal to the given key in the hash map:
        # Remove the key from the queue of keys and insert it again last (since it was just used)
        # Return the value associated with it
        if self.hash_map.get(key) is not None:
            self.keys.remove(key)
            self.keys.append(key)

            return self.hash_map[key]

        return -1

    def put(self, key, value):
        """
        :param key: the number corresponding to the key of the new element to be added in the LRU cache
        :param value: the number corresponding to the value of the new element to be added in the
            LRU cache
        :return: void
        """
        # Time complexity <=> O(1)
        # Space complexity <=> O(2 * n), where n is the current number of elements in the LRU cache

        # If there already is an element with that key, change its value to the given one
        # And remove its key from the queue of keys and insert it again last (since it was just used)
        # Otherwise and if the LRU cache is at capacity:
        # Remove the element which has the least used key (the first one in the queue of keys)
        # Add the new element in the LRU cache at the end
        # Add the key of the element to the queue of keys at the end
        # Otherwise (if the LRU cache isn't at capacity):
        # Add the new element in the LRU cache at the end
        # Add the key of the element to the queue of keys at the end
        if self.hash_map.get(key) is not None:
            self.hash_map[key] = value
            self.keys.remove(key)
            self.keys.append(key)
        elif len(self.hash_map) == self.capacity:
            self.hash_map.pop(self.keys[0])
            self.keys.pop(0)
            self.hash_map[key] = value
            self.keys.append(key)
        else:
            self.hash_map[key] = value
            self.keys.append(key)


# Example 1
commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
elements = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
results = []
size = len(commands)
cache = LRUCache(elements[0][0])

for i in range(1, size):
    command = commands[i]
    element = elements[i]

    if command == "put":
        cache.put(element[0], element[1])
        results.append(None)
    elif command == "get":
        results.append(cache.get(element[0]))

print(results)
print("-------------------------------------")

# Example 2
commands = ["LRUCache", "get", "put", "get", "put", "put", "get", "get"]
elements = [[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]]
results = []
size = len(commands)
cache = LRUCache(elements[0][0])

for i in range(1, size):
    command = commands[i]
    element = elements[i]

    if command == "put":
        cache.put(element[0], element[1])
        results.append(None)
    elif command == "get":
        results.append(cache.get(element[0]))

print(results)
print("-------------------------------------")

# Example 3
commands = ["LRUCache", "put", "put", "put", "put", "get", "get"]
elements = [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]
results = []
size = len(commands)
cache = LRUCache(elements[0][0])

for i in range(1, size):
    command = commands[i]
    element = elements[i]

    if command == "put":
        cache.put(element[0], element[1])
        results.append(None)
    elif command == "get":
        results.append(cache.get(element[0]))

print(results)
