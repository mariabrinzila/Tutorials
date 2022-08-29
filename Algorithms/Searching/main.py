import time
import numpy as np

import linear_search as linear
import binary_search as binary
import jump_search as jump


array = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170, 34, 1, 567, 1000, 23, 5, 10, 5, 78, 9045, 65, 0, 54, 80]

# Linear Search (iterative)
element = 2

result = linear.linear_search_iterative(array, element)

if result == -1:
    print("The element you're searching for doesn't exist in the given array")
else:
    print("The element you're searching for exists in the given array on position " + str(result))

element = 567

result = linear.linear_search_iterative(array, element)

if result == -1:
    print("The element you're searching for doesn't exist in the given array")
else:
    print("The element you're searching for exists in the given array on position " + str(result))

# Linear Search (recursive)
element = 81

# Start time
start = time.perf_counter()

result = linear.linear_search_recursive(array, element, 0)

# End time
end = time.perf_counter()

# Compute elapsed time
timer = (end - start)

print("Linear Search Recursive took " + f"{timer:0.4f} seconds")

if result == -1:
    print("The element you're searching for doesn't exist in the given array")
else:
    print("The element you're searching for exists in the given array on position " + str(result))

element = 100

# Start time
start = time.perf_counter()

result = linear.linear_search_recursive(array, element, 0)

# End time
end = time.perf_counter()

# Compute elapsed time
timer = (end - start)

print("Linear Search Recursive took " + f"{timer:0.4f} seconds")

if result == -1:
    print("The element you're searching for doesn't exist in the given array")
else:
    print("The element you're searching for exists in the given array on position " + str(result))

print("---------------------------------------")

# The array needs to be sorted for Binary and Jump Search
array.sort()

print("The sorted array is: " + str(array))
print("---------------------------------------")

# Binary Search (iterative)
element = 6

result = binary.binary_search_iterative(array, element)

if result == -1:
    print("The element you're searching for doesn't exist in the given array")
else:
    print("The element you're searching for exists in the given array on position " + str(result))

element = 9045

result = binary.binary_search_iterative(array, element)

if result == -1:
    print("The element you're searching for doesn't exist in the given array")
else:
    print("The element you're searching for exists in the given array on position " + str(result))

# Binary Search (recursive)
# The array needs to be sorted
array.sort()
element = 904545

# Start time
start = time.perf_counter()
index = len(array) - 1

result = binary.binary_search_recursive(array, element, 0, index)

# End time
end = time.perf_counter()

# Compute elapsed time
timer = (end - start)

print("Binary Search Recursive took " + f"{timer:0.4f} seconds")

if result == -1:
    print("The element you're searching for doesn't exist in the given array")
else:
    print("The element you're searching for exists in the given array on position " + str(result))

element = 5

# Start time
start = time.perf_counter()
index = len(array) - 1

result = binary.binary_search_recursive(array, element, 0, index)

# End time
end = time.perf_counter()

# Compute elapsed time
timer = (end - start)

print("Binary Search Recursive took " + f"{timer:0.4f} seconds")

if result == -1:
    print("The element you're searching for doesn't exist in the given array")
else:
    print("The element you're searching for exists in the given array on position " + str(result))

print("---------------------------------------")

# Jump Search
element = 170

n = len(array)
m = int(np.sqrt(n))

result = jump.jump_search(array, element, m)

if result == -1:
    print("The element you're searching for doesn't exist in the given array")
else:
    print("The element you're searching for exists in the given array on position " + str(result))

element = 1745

result = jump.jump_search(array, element, m)

if result == -1:
    print("The element you're searching for doesn't exist in the given array")
else:
    print("The element you're searching for exists in the given array on position " + str(result))
