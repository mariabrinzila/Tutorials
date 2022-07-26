import time

import selection_sort as selection
import bubble_sort as bubble
import insertion_sort as insertion
import merge_sort as merge
import quick_sort as quick
import heap_sort as heap
import counting_sort as count
import radix_sort as radix
import bucket_sort as bucket


# Selection Sort
to_be_sorted = [100, 99, 98, 97, 90, 85, 82, 70, 65, 54, 51, 43, 37, 29, 24, 22, 20, 16, 12, 10, 6, 1, 100]

selection.selection_sort(to_be_sorted)

print("The sorted array with Selection Sort is: " + str(to_be_sorted))
print("---------------------------------------")

# Bubble Sort
to_be_sorted = [100, 99, 98, 97, 90, 85, 82, 70, 65, 54, 51, 43, 37, 29, 24, 22, 20, 16, 12, 10, 6, 1, 100]

bubble.bubble_sort(to_be_sorted)

print("The sorted array with Bubble Sort is: " + str(to_be_sorted))
print("---------------------------------------")

# Insertion Sort
to_be_sorted = [100, 99, 98, 97, 90, 85, 82, 70, 65, 54, 51, 43, 37, 29, 24, 22, 20, 16, 12, 10, 6, 1, 100]

# Start timer
start = time.perf_counter()

insertion.insertion_sort(to_be_sorted)

# End timer
end = time.perf_counter()

# Compute elapsed time
timer = (end - start)

print("Insertion Sort took " + f"{timer:0.4f} seconds")
print("The sorted array with Insertion Sort is: " + str(to_be_sorted))
print("---------------------------------------")

# Merge Sort
to_be_sorted = [100, 99, 98, 97, 90, 85, 82, 70, 65, 54, 51, 43, 37, 29, 24, 22, 20, 16, 12, 10, 6, 1, 100]

# Start timer
start = time.perf_counter()

merge.merge_sort(to_be_sorted)

# End timer
end = time.perf_counter()

# Compute elapsed time
timer = (end - start)

print("Merge Sort took " + f"{timer:0.4f} seconds")
print("The sorted array with Merge Sort is: " + str(to_be_sorted))
print("---------------------------------------")

# Quick Sort
to_be_sorted = [100, 99, 98, 97, 90, 85, 82, 70, 65, 54, 51, 43, 37, 29, 24, 22, 20, 16, 12, 10, 6, 1, 100]

# Start timer
start = time.perf_counter()
last_position = len(to_be_sorted) - 1

quick.quick_sort(to_be_sorted, 0, last_position)

# End timer
end = time.perf_counter()

# Compute elapsed time
timer = (end - start)

print("Quick Sort took " + f"{timer:0.4f} seconds")
print("The sorted array with Quick Sort is: " + str(to_be_sorted))
print("---------------------------------------")

# Heap Sort
to_be_sorted = [100, 99, 98, 97, 90, 85, 82, 70, 65, 54, 51, 43, 37, 29, 24, 22, 20, 16, 12, 10, 6, 1, 100]

heap.heap_sort(to_be_sorted)

print("The sorted array with Heap Sort is: " + str(to_be_sorted))
print("---------------------------------------")

# Counting Sort
to_be_sorted = [100, 99, 98, 97, 90, 85, 82, 70, 65, 54, 51, 43, 37, 29, 24, 22, 20, 16, 12, 10, 6, 1, 100]
m = min(to_be_sorted)
n = max(to_be_sorted) + 1

if m > 0:
    m -= 1

sorted_array = count.counting_sort(to_be_sorted, m, n)

print("The sorted array with Counting Sort is: " + str(sorted_array))
print("---------------------------------------")

# Radix Sort
to_be_sorted = [100, 99, 98, 97, 90, 85, 82, 70, 65, 54, 51, 43, 37, 29, 24, 22, 20, 16, 12, 10, 6, 1, 100]

sorted_array = radix.radix_sort(to_be_sorted)

print("The sorted array with Radix Sort is: " + str(sorted_array))
print("---------------------------------------")

# Bucket Sort
to_be_sorted = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434, 0.12, 0.23, 0.45, 0.0006, 0.34, 0.789, 0.899]

sorted_array = bucket.bucket_sort(to_be_sorted, 10)

print("The sorted array with Bucket Sort is: " + str(sorted_array))

to_be_sorted = [9.8, 0.6, 10.1, 1.9, 3.07, 3.04, 5.0, 8.0, 4.8, 7.68, 0.0001, 9.1023, 6.234, 5.602]

sorted_array = bucket.bucket_sort_integer(to_be_sorted, 5)

print("The sorted array with Bucket Sort is: " + str(sorted_array))
