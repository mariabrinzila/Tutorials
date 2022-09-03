def merge_sort(array):
    """
    :param array: the current array to be sorted
    :return: void
    """
    # If the array has more than one element:
    # Compute the middle of the current array and divide the array into 2 array halves
    # Call Merge Sort for the first half array
    # Call Merge Sort for the second half array
    # Merge the 2 array halves so the larger array is sorted
    length = len(array)

    if length > 1:
        middle = length // 2
        left_part = array[:middle]
        right_part = array[middle:]

        merge_sort(left_part)
        merge_sort(right_part)

        i = j = k = 0
        left_length = len(left_part)
        right_length = len(right_part)

        # Put the elements in both halves in an initial array (sorting them)
        while i < left_length and j < right_length:
            if left_part[i] < right_part[j]:
                array[k] = left_part[i]
                i += 1
                k += 1
            else:
                array[k] = right_part[j]
                j += 1
                k += 1

        # There are still some elements in the first half
        while i < left_length:
            array[k] = left_part[i]
            i += 1
            k += 1

        # There are still some elements in the second half
        while j < right_length:
            array[k] = right_part[j]
            j += 1
            k += 1
