# Base states <=> fib(0) = 0, fib(1) = 1
# Transition <=> fib(n) = fib(n - 1) + fib(n - 2)
# Overlapping subproblems <=> each fib(i) before fib(n) needs to be computed at least twice
# Optimal substructure <=> the optimal solution for fib(i), i < n leads to the optimal solution of fib(n)

# Time complexity <=> O(n)
# Space complexity <=> O(n)


def fibonacci_tabulation(n):
    """
    :param n: the position in the Fibonacci sequence of the wanted element
    :return: the n-th Fibonacci element
    """
    # Base states
    if n == 0:
        return 0

    if n == 1:
        return 1

    fib = [None] * (n + 1)
    fib[0] = 0
    fib[1] = 1

    # Compute all states before fib(n) <=> fib(i), 1 < i <= n
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


def fibonacci_memorization(n, lookup):
    """
    :param n: the current position in the Fibonacci sequence of the wanted element
    :param lookup: the array of already computed solutions
    :return: the current n-th Fibonacci element
    """
    # Base states
    if n == 0:
        return 0

    if n == 1:
        return 1

    # If the solution hasn't been computed yet, recursively compute it
    # Otherwise, return it
    if lookup[n] is None:
        lookup[n] = fibonacci_memorization(n - 1, lookup) + fibonacci_memorization(n - 2, lookup)

    return lookup[n]
