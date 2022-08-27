import time


def linear_search_iterative(array, to_be_sought):
    """
    :param array: the array in which we're looking for an element
    :param to_be_sought: the element we're seeking in the given array
    :return: the element's index, if it exists in the given array and -1, otherwise
    """
    # Start time
    start = time.perf_counter()

    # Traverse all the elements in the given array
    # If we come across the sought element, return its index
    # Otherwise, return -1
    size = len(array)
    index = -1

    for i in range(size):
        if array[i] == to_be_sought:
            index = i
            break

    # End time
    end = time.perf_counter()

    # Compute elapsed time
    timer = (end - start)

    print("Linear Search Iterative took " + f"{timer:0.4f} seconds")

    return index


def linear_search_recursive(array, to_be_sought, position):
    """
    :param array: the array in which we're looking for an element
    :param to_be_sought: the element we're seeking in the given array
    :param position: the current position in the given array
    :return: the element's index, if it exists in the given array and -1, otherwise
    """
    if position == len(array) - 1:
        return -1

    if array[position] == to_be_sought:
        return position

    return linear_search_recursive(array, to_be_sought, position + 1)
