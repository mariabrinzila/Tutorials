class Solution(object):
    def __init__(self):
        # Define an array which will hold all the possible solutions
        self.solutions = []

    def permute(self, nums):
        """
        :param nums: the array of unique numbers that will be permuted in all possible ways
        :return: the array of all possible permutations of the given array (each permutation is an
            array)
        """
        # Data structure <=> Array
        # Algorithm <=> Backtracking

        # We need all possible solutions <=> backtracking
        # For each element in the given array, compute a solution with it on every possible position
        # Each element on the first position <=> n steps (n = len(nums))
        # Each second element will have all the elements minus the one that's first <=> n - 1 steps
        # For the rest of the position, we'll have n - 2 inversions
        # So the total is n * (n - 1) * (n - 2) steps = n! * (n - 2) steps

        # Time complexity <=> O(n! * (n - 2)) / O(n!) (if n <= 2), where n is the size of the array
        # Space complexity <=> O(n)

        # Base case <=> the given array only has one element
        if len(nums) == 1:
            return [[nums[0]]]

        current_solution = []

        self.backtracking(current_solution, nums)

        return self.solutions

    def backtracking(self, current_solution, nums):
        """
        :param current_solution: the array of numbers from the given array that constitute
            the current solution (no number is repeated in the solution)
        :param nums: the array of unique numbers that will be permuted in all possible ways
        :return: void
        """
        # Time complexity <=> O(n! * (n - 2)) / O(n!) (if n <= 2), where n is the size of the array
        # Space complexity <=> O(n)

        # For each element in the given array:
        # If the size of the current solution is equal to the size of the given array:
        # If the current solution isn't already in the array of solutions:
        # We've found a new solution, so add it to the array of solutions
        # Otherwise (the current solution isn't completed yet):
        # If the current element isn't visited already (it doesn't exist in the current solution already):
        # Add it and move on to the next position in the current solution
        # Backtrack and try another element for that position, when necessary
        for element in nums:
            if len(current_solution) == len(nums) and current_solution not in self.solutions:
                self.solutions.append(current_solution.copy())
            elif element not in current_solution:
                current_solution.append(element)

                self.backtracking(current_solution, nums)

                current_solution.remove(element)


# Example 1
numbers = [1, 2, 3]

print(Solution().permute(numbers))
print("-------------------------------------")

# Example 2
numbers = [0, 1]

print(Solution().permute(numbers))
print("-------------------------------------")

# Example 3
numbers = [1]

print(Solution().permute(numbers))
