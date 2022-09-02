def backtracking(initial_set, target_sum, solution, current_sum):
    """
    :param initial_set: the set of positive numbers from which we need to find numbers that add up
        to a given sum
    :param target_sum: the sum which the chosen numbers must add to
    :param solution: the current subset of numbers of the given set which is a potential solution
    :param current_sum: the current sum of the numbers in the current subset
    :return: void
    """
    # Base case
    if current_sum == target_sum:
        print(solution)

    # For each element in the initial set:
    # If the element hasn't been added to the solution already
    # And the sum of the currently computed sum and the current element is <= the target sum:
    # Add it to the solution and increment the currently computed sum
    # If the current element doesn't lead to a solution:
    # Backtrack (remove it from the solution and decrease the currently computed sum)
    for element in initial_set:
        if current_sum + element <= target_sum and element not in solution:
            current_sum += element
            solution.append(element)

            backtracking(initial_set, target_sum, solution, current_sum)

            current_sum -= element
            solution.remove(element)
