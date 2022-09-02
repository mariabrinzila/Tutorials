import subset_sum as ss

# Subset sum
initial_set = {15, 22, 14, 26, 32, 9, 16, 8}
target_sum = 53

ss.backtracking(initial_set, target_sum, [], 0)

print("---------------------------------------")
