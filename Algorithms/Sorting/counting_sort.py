import time


def counting_sort(array, m, n):
    """
    :param array: the array to be sorted
    :param m: the lower limit of the range of values in the given array
    :param n: the upper limit of the range of values in the given array
    :return: the sorted array
    """
    # Start timer
    start = time.perf_counter()
    size = len(array)

    count = [0 for i in range(m, n + 1)]
    output = [0 for i in range(size)]

    # Compute the count of each element in the given array
    for i in range(size):
        count[array[i]] += 1

    # Modify the count array by adding the previous counts for each element
    for i in range(m, n + 1):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(size):
        count[array[i]] -= 1
        output[count[array[i]]] = array[i]

    # End timer
    end = time.perf_counter()

    # Compute elapsed time
    timer = (end - start)

    print("Counting Sort took " + f"{timer:0.4f} seconds")

    return output
