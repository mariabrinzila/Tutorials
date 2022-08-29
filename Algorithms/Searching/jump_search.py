import linear_search as linear

import time


def jump_search(array, to_be_sought, skipped):
    """
    :param array: the array in which we're looking for the element
    :param to_be_sought: the element we're seeking in the given array
    :param skipped: the number of elements to be skipped
    :return: the element's index, if it exists in the given array and -1, otherwise
    """
    # Start time
    start = time.perf_counter()

    # Keep skipping skipped elements until we get to a point where array[position] > to_be_sought
    position = 0
    size = len(array)

    while array[position + skipped] < to_be_sought:
        position += skipped

        if position + skipped > size - 1:
            break

    # Do Linear Search from the computed position to find the sought element
    index = linear.linear_search_recursive(array, to_be_sought, position)

    # End time
    end = time.perf_counter()

    # Compute elapsed time
    timer = (end - start)

    print("Jump Search took " + f"{timer:0.4f} seconds")

    return index
