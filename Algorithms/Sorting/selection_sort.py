import time


def selection_sort(array):
    """
    :param array: the array to be sorted
    :return: void
    """
    # While there are still elements in the array to be sorted:
    # Pick the next unsorted element
    # Traverse the rest of the array and find the minimum value
    # Swap it with the picked element
    length = len(array)

    # Start time
    start = time.perf_counter()

    for i in range(length):
        minimum_index = i

        for j in range(i + 1, length):
            if array[j] < array[minimum_index]:
                minimum_index = j

        array[i], array[minimum_index] = array[minimum_index], array[i]

    # End time
    end = time.perf_counter()

    # Compute elapsed time
    timer = (end - start)

    print("Selection Sort took " + f"{timer:0.4f} seconds")
