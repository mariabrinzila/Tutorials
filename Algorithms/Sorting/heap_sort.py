import time


def heap_sort(array):
    """
    :param array: the array to be sorted
    :return: void
    """
    # Start timer
    start = time.perf_counter()

    # Build a Max-Heap from the given array
    size = len(array)
    last_non_leaf = size // 2 - 1

    # From the last non-leaf node (on position size // 2 - 1) to the root (on position 0), going up:
    # Call heapify on the current node
    for i in range(last_non_leaf, -1, -1):
        heapify(array, size, i)

    # One by one, remove the root of the Max-Heap and create a new Max-Heap with the remaining elements
    # Keep doing this until there is only one node in the Max-Heap
    # Remove the root by swapping it with the last element and decreasing the size of the array
    for i in range(size - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)

    # End timer
    end = time.perf_counter()

    # Compute elapsed time
    timer = (end - start)

    print("Heap Sort took " + f"{timer:0.4f} seconds")


def heapify(array, size, index):
    """
    :param array: the current array to be turned into a Max-Heap
    :param size: the size of the current array
    :param index: the index of the current node (current root node)
    :return: void
    """
    # Compute the current node's children
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    # Compute the largest node value out of the current node and its children
    largest_index = index

    if left_index < size and array[left_index] > array[largest_index]:
        largest_index = left_index

    if right_index < size and array[right_index] > array[largest_index]:
        largest_index = right_index

    # If the largest node value is not the current node
    # Swap it with it
    # Call heapify for the largest node value
    if array[largest_index] != array[index]:
        array[index], array[largest_index] = array[largest_index], array[index]
        heapify(array, size, largest_index)
