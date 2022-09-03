def quick_sort(array, low, high):
    """
    :param array: the current array to be sorted
    :param low: the index of the first element in the current array
    :param high: the index of the last element in the current array
    :return: void
    """
    # If we can still partition the given array:
    # Partition the array and return the index of the pivot
    # Call Quick Sort for the elements before the pivot
    # Call Quick Sort for the elements after the pivot
    if low < high:
        index = partition(array, low, high)
        quick_sort(array, low, index - 1)
        quick_sort(array, index + 1, high)


def partition(array, low, high):
    """
    :param array: the current array to be partitioned
    :param low: the index of the first element in the current array
    :param high: the index of the last element in the current array
    :return: the index of the pivot (all elements on positions before it are < pivot and
        all elements on position after it are > pivot)
    """
    # Compute the pivot (the last element in the current given array
    pivot = array[high]

    # Compute the index of the first element greater than the pivot
    index = low - 1

    # From low to high - 1:
    # If the current element in the array is smaller than the pivot,
    # Increment the index of the first element greater than the pivot
    # Swap the current element with the one on the index position
    for j in range(low, high):
        if array[j] < pivot:
            index += 1
            array[index], array[j] = array[j], array[index]

    # At this point, all elements on positions <= index are < pivot
    # And on positions > index are > pivot but the pivot is still on the last position
    # Swap the pivot with the first element which is greater than it (on position index + 1)
    array[high], array[index + 1] = array[index + 1], array[high]

    return index + 1
