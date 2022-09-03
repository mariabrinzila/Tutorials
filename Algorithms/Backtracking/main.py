import subset_sum as ss
import rat_in_a_maze as rm


# Subset sum
initial_set = {15, 22, 14, 26, 32, 9, 16, 8}
target_sum = 53

ss.subset_sum(initial_set, target_sum, [], 0)

print("---------------------------------------")

# Rat in a maze
size = 4
start = (0, 0)
destination = (3, 3)
available_positions = [(1, 0), (1, 1), (3, 1), (2, 1), (3, 0), (3, 1), (3, 2)]

rm.rat_maze_initialization(size, start, destination, available_positions)
