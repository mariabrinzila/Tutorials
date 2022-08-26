import time


def radix_sort(array):
    """
    :param array: the array to be sorted
    :return: the sorted given array
    """
    # Start timer
    start = time.perf_counter()

    # Compute maximum element (to know the number of sorting, which is equal to the number of digits)
    maximum_element = max(array)

    # Do Counting Sort on every digit (the digit will be 1, 10, 100 etc.)
    digit = 1

    # While there are still digits based on which to sort:
    # Do Counting Sort on the current digit
    # Go up with the digit
    sorted_array = array

    while maximum_element // digit >= 1:
        sorted_array = counting_sort(sorted_array, digit)
        digit *= 10

    # End timer
    end = time.perf_counter()

    # Compute elapsed time
    timer = (end - start)

    print("Radix Sort took " + f"{timer:0.4f} seconds")

    return sorted_array


def counting_sort(array, current_digit):
    """
    :param array: the current array to be sorted based on a digit
    :param current_digit: the current digit based on which the current array will be sorted
    :return: the sorted current array based on the given digit
    """
    size = len(array)

    # Count will hold the count of the last digit resulted from the array[i] // current_digit
    count = [0 for i in range(10)]
    output = [0 for i in range(size)]

    # Compute the count of each element in the given array
    for i in range(size):
        index = (array[i] // current_digit) % 10
        count[index] += 1

    # Modify the count array by adding the previous counts for each element
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    # Starting from the end of count, so we get the elements in the order they are in array
    for i in range(size - 1, -1, -1):
        index = (array[i] // current_digit) % 10
        count[index] -= 1
        output[count[index]] = array[i]

    return output
