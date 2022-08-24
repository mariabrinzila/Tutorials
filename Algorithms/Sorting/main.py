import time

import selection_sort as selection
import bubble_sort as bubble
import insertion_sort as insertion
import merge_sort as merge


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
insertion.insertion_sort(to_be_sorted)

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
