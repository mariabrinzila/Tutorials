import time

import insertion_sort as insertion


def bucket_sort(array, n):
    """
    :param array: the array to be sorted
    :param n: the number of buckets (or slots for the range)
    :return: the sorted array
    """
    # Bucket sort for floating point numbers between 0.0 and 1.0
    # Compute n empty buckets
    buckets = [[] for i in range(n)]

    # Traverse the given array and put each element in the correct bucket
    size = len(array)

    for i in range(size):
        index = int(n * array[i])
        buckets[index].append(array[i])

    # Sort each bucket with Insertion Sort and concatenate all buckets together
    output = [0 for i in range(size)]
    index = 0

    for bucket in buckets:
        insertion.insertion_sort(bucket)

        bucket_size = len(bucket)

        for i in range(bucket_size):
            output[index] = bucket[i]
            index += 1

    # Start timer
    start = time.perf_counter()

    # End timer
    end = time.perf_counter()

    # Compute elapsed time
    timer = (end - start)

    print("Bucket Sort took " + f"{timer:0.4f} seconds")

    return output


def bucket_sort_integer(array, n):
    """
    :param array: the array to be sorted
    :param n: the number of buckets (or slots for the range)
    :return: the sorted array
    """
    # Bucket sort for numbers having integer part (the range isn't 0 - 1 anymore)
    # Compute the range
    maximum_element = max(array)
    minimum_element = min(array)
    elements_range = (maximum_element - minimum_element) / n

    # Compute n empty buckets
    buckets = [[] for i in range(n)]

    # Traverse the given array and put each element in the correct bucket
    size = len(array)

    for i in range(size):
        index = int((array[i] - minimum_element) / elements_range)

        if index == n:
            index -= 1

        buckets[index].append(array[i])

    # Sort each bucket with Insertion Sort and concatenate all buckets together
    output = [0 for i in range(size)]
    index = 0

    for bucket in buckets:
        insertion.insertion_sort(bucket)

        bucket_size = len(bucket)

        for i in range(bucket_size):
            output[index] = bucket[i]
            index += 1

    # Start timer
    start = time.perf_counter()

    # End timer
    end = time.perf_counter()

    # Compute elapsed time
    timer = (end - start)

    print("Bucket Sort took " + f"{timer:0.4f} seconds")

    return output
