import time


def insertion_sort(array):
    """
    :param array: the array to be sorted
    :return: void
    """
    length = len(array)

    # Start timer
    start = time.perf_counter()

    # While there are still elements in the array to be sorted:
    # Pick the next unsorted element
    # While there are still elements before it that are < than it:
    # The picked element will have to be ahead of them
    # So move them one position to the right
    for i in range(1, length):
        picked = array[i]
        j = i - 1

        while j >= 0 and picked < array[j]:
            array[j], array[j + 1] = array[j + 1], array[j]
            j -= 1

    # End timer
    end = time.perf_counter()

    # Compute elapsed time
    timer = (end - start)

    print("Insertion Sort took " + f"{timer:0.4f} seconds")
