# Ugly number <=> a number whose only prime factors are 2, 3 and 5 (1, 2, 3, 5, 6, 8, 9, 10, 12, ...)

# Dynamic programming approach:
# Compute all n ugly numbers starting from 1 (top down)
# At every step, choose the smallest multiple of 2, 3 and 5

# Time complexity <=> O(n)
# Space complexity <=> O(n)


def ugly_numbers_memorization(n):
    """
    :param n: the position in the ugly numbers sequence of the wanted element
    :return: the n-th ugly number
    """
    # Base case
    ugly = [1]
    index2 = index3 = index5 = 0
    next_multiple2 = 2
    next_multiple3 = 3
    next_multiple5 = 5

    # For every i from 1 to n:
    # Choose the smallest value of the 3 possible ones (the next multiple of 2, 3 and 5)
    # Append the value to the ugly array and increment the according index
    while len(ugly) < n:
        current_ugly = min(next_multiple2, next_multiple3, next_multiple5)

        if current_ugly not in ugly:
            ugly.append(current_ugly)

        if current_ugly == next_multiple2:
            index2 += 1
            next_multiple2 = ugly[index2] * 2
        elif current_ugly == next_multiple3:
            index3 += 1
            next_multiple3 = ugly[index3] * 3
        else:
            index5 += 1
            next_multiple5 = ugly[index5] * 5

    return ugly[n - 1]
