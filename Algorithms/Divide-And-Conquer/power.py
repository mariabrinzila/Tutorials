def power(x, n):
    """
    :param x: the number which will be multiplied with itself n times
    :param n: the number of times x will be multiplied with itself
    :return: x to the n-th power
    """
    # x ^ i = x ^ (i / 2) * x ^ (i / 2), if i is even and x ^ i = x ^ (i / 2) * x ^ (i / 2) * x, otherwise
    # Subproblems <=> finding x ^ (i / 2)
    # Base cases <=> x ^ 1 = x, x ^ 0 = 1, 0 ^ n = 0, 1 ^ n = 1
    if n == 1:
        return x

    if n == 0:
        return 1

    if x == 0:
        return 0

    if x == 1:
        return 1

    # Compute power(x, n // 2) first and store it in a variable to save performance
    number = power(x, n // 2)

    if n % 2 == 0:
        # n is even
        return number * number
    else:
        # n is odd
        return number * number * x
