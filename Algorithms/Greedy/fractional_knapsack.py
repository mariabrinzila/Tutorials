def fractional_knapsack(items, knapsack_capacity):
    """
    :param items: the array of possible items to put in the knapsack containing (weight, value) tuples
    :param knapsack_capacity: the knapsack's total weight capacity
    :return: the knapsack's value which should be maximized to fill the knapsack
        (items can be put in the knapsack whole or broken into fractions)
    """
    # Sort the array of items in ascending order based on the ratio of value / weight
    # In order to be able to maximize the knapsack's value
    items.sort(key=lambda it: (it[1] / it[0]), reverse=True)

    # Traverse the sorted items array and always choose the local optimal solution
    # Local optimal solution <=> an item that can be put whole in knapsack and its value is maximal
    # At the end, if there is still space in the knapsack, put a fraction of the next item
    knapsack_value = 0.0
    items_number = len(items)

    for i in range(0, items_number):
        item_weight = items[i][0]
        item_value = items[i][1]

        if knapsack_capacity - item_weight >= 0:
            knapsack_capacity -= item_weight
            knapsack_value += item_value
        else:
            knapsack_value += item_value * knapsack_capacity / item_weight

    return knapsack_value
