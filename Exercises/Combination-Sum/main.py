class Solution(object):
    def __init__(self):
        # Define an array which will hold all the possible solutions
        self.solution_list = []

    def combination_sum(self, candidates, target):
        """
        :param candidates: the array of possible distinct numbers that can each be chosen multiples times
            to sum up to the target sum
        :param target: the number which is the target sum
        :return: the array of all possible combinations of the numbers in the given array that sum up
            to the target sum
        """
        # Data structure <=> Array
        # Algorithm <=> Backtracking

        # We need all possible solutions <=> backtracking
        # For each element in the given array, see if it leads to a solution
        # By trying to make one with each of the other elements (including itself)
        # If an element doesn't lead to a solution, backtrack and try another candidate

        # Time complexity <=> O(n * n), where n is the size of the array
        # Space complexity <=> O(n * n)

        # Base case <=> the given array only contains one number
        if len(candidates) == 1 and candidates[0] != target:
            return []
        elif len(candidates) == 1 and candidates[0] == target:
            return [candidates[0]]

        current_solution = []
        current_sum = 0

        self.backtracking(current_solution, current_sum, target, candidates)

        return self.solution_list

    def backtracking(self, current_solution, current_sum, target, candidates):
        """
        :param current_solution: the array of candidate numbers that constitute the current solution
        :param current_sum: the number that the numbers in the current solution add up to
        :param target: the number which is the given target sum
        :param candidates: the array of possible distinct numbers that can each be chosen multiples times
            (can be added to the current solution) to sum up to the target sum
        :return: void
        """
        # Time complexity <=> O(n * n), where n is the size of the array
        # Space complexity <=> O(n * n)

        # For each candidate number in the given array:
        # If adding the current candidate to the current sum doesn't exceed the target sum:
        # Add it to the current solution and increment the current sum
        # If the current sum is now equal to the target sum:
        # We've found a new solution, so add it to the array of solutions
        # Repeat this step with the current sum and the current solution
        # If the current candidate doesn't lead to a solution:
        # Backtrack and try another one, so delete it from the current solution and decrease the sum
        for candidate in candidates:
            if current_sum + candidate <= target:
                current_solution.append(candidate)
                current_sum += candidate

                if current_sum == target:
                    solution = sorted(current_solution)

                    if solution not in self.solution_list:
                        self.solution_list.append(solution)

                self.backtracking(current_solution, current_sum, target, candidates)

                current_solution.remove(candidate)
                current_sum -= candidate


# Example 1
candidates_list = [2, 3, 6, 7]
target_sum = 7

print(Solution().combination_sum(candidates_list, target_sum))
print("-------------------------------------")

# Example 2
candidates_list = [2, 3, 5]
target_sum = 8

print(Solution().combination_sum(candidates_list, target_sum))
print("-------------------------------------")

# Example 3
candidates_list = [2]
target_sum = 1

print(Solution().combination_sum(candidates_list, target_sum))
print("-------------------------------------")

# Example 4
candidates_list = [7, 3, 2]
target_sum = 18

print(Solution().combination_sum(candidates_list, target_sum))
