import time


def binary_search_iterative(array, to_be_sought):
    """
    :param array: the array in which we're looking for the element
    :param to_be_sought: the element we're seeking in the given array
    :return: the element's index, if it exists in the given array and -1, otherwise
    """
    # Start time
    start = time.perf_counter()

    start_index = 0
    end_index = len(array) - 1

    # While we haven't found the sought element and the search interval isn't empty:
    # Compute the middle of the search interval
    # Compare the middle with the sought element
    # If they're equal, return the middle's index
    # If the middle is < the sought element, the search interval becomes the second half
    # Otherwise, the search interval becomes the first half
    index = -1

    while start_index < end_index:
        middle_index = (start_index + end_index) // 2

        if array[middle_index] == to_be_sought:
            index = middle_index
            break
        elif to_be_sought > array[middle_index]:
            start_index = middle_index + 1
        else:
            end_index = middle_index

    if array[start_index] == to_be_sought:
        index = start_index
    elif array[end_index] == to_be_sought:
        index = end_index

    # End time
    end = time.perf_counter()

    # Compute elapsed time
    timer = (end - start)

    print("Binary Search Iterative took " + f"{timer:0.4f} seconds")

    return index


def binary_search_recursive(array, to_be_sought, start_index, end_index):
    """
    :param array: the current array (search interval) in which we're looking for the element
    :param to_be_sought: the element we're seeking in the given array
    :param start_index: the index where the search interval begins
    :param end_index: the index where the search interval ends
    :return: the element's index, if it exists in the given array and -1, otherwise
    """
    middle_index = (start_index + end_index) // 2

    if start_index > end_index:
        return -1

    if array[middle_index] == to_be_sought:
        return middle_index
    elif to_be_sought > array[middle_index]:
        return binary_search_recursive(array, to_be_sought, middle_index + 1, end_index)
    else:
        return binary_search_recursive(array, to_be_sought, start_index, middle_index)
