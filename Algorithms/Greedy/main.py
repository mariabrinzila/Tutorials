import activity_selection as acs
import fractional_knapsack as fk

# Activity selection problem
activities = [(5, 9), (0, 6), (3, 4), (5, 7), (8, 9), (1, 2)]

print("The maximum selected activities are: " + str(acs.activity_selection(activities)))
print("---------------------------------------")

# Fractional knapsack problem
items = [(10, 60), (20, 100), (30, 120)]
capacity = 50
print("The knapsack's maximum value is: " + str(fk.fractional_knapsack(items, capacity)))
