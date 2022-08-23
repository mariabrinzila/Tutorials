import time


def bubble_sort(array):
    """
    :param array: the array to be sorted
    :return: void
    """
    length = len(array)

    # Start time
    start = time.perf_counter()

    # While there are still elements in the array to be sorted:
    # Pick the next unsorted element
    # Traverse the array until the length - i - 1 position
    # If we find 2 elements that are in the wrong order, swap them
    # If after such a traversal the number of swaps is 0, the array is sorted
    for i in range(length):
        swaps = False

        # The last i elements are already sorted
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                swaps = True
                array[j], array[j + 1] = array[j + 1], array[j]

        if not swaps:
            break

    # End time
    end = time.perf_counter()

    # Compute elapsed time
    timer = (end - start)

    print("Bubble Sort took " + f"{timer:0.4f} seconds")
