import time

import linear_search as linear


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
