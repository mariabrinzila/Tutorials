# Base state <=> 0! = 1
# Transition <=> n! = (n - 1)! * n
# Overlapping subproblems <=> each i! before n! needs to be computed at least twice
# Optimal substructure <=> the optimal solution for i!, i < n leads to the optimal solution of n!


def factorial_tabulation(n):
    """
    :param n: the number for which the factorial will be computed
    :return: the number n!
    """
    # Base state
    if n == 0:
        return 1

    fact = [None] * (n + 1)
    fact[0] = 1

    # Compute all states before n! <=> i!, 0 < i <= n
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i

    return fact[n]


def factorial_memorization(n, lookup):
    """
    :param n: the current number for which the factorial will be computed
    :param lookup: the array of already computed solutions
    :return: the current number n!
    """
    # Base states
    if n == 0:
        return 1

    # If the solution hasn't been computed yet, recursively compute it
    # Otherwise, return it
    if lookup[n] is None:
        lookup[n] = factorial_memorization(n - 1, lookup) * n

    return lookup[n]
