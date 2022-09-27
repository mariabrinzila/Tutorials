class Solution(object):
    def __init__(self):
        # Define a number which represents the minimum sum
        self.min_sum = 400000

        # Define 2 movement arrays (we can either move down or right)
        self.move_line = [1, 0]
        self.move_column = [0, 1]

    def min_path_sum(self, grid):
        """
        :param grid: the matrix of positive numbers from which the minimum sum path from the top left
            position to the bottom right position will be computed
        :return: the sum of the numbers on the minimum sum path
        """
        # Data structure <=> Matrix
        # Algorithm <=> Dynamic Programming

        # We need the optimal solution (the one which has a minimum sum) <=> backtracking
        # But the size of the grid is big, so we need an optimization <=> dynamic programming
        # We need partial sums on the first row and first column
        # And with that we can compute the rest of the partial sums
        # At the end, the result will be on the bottom right corner of the matrix

        # Time complexity <=> O(m * n + m + n), where n is the size of the linked list
        # Space complexity <=> O(m * n)

        # Base case <=> the matrix only has one element
        m = len(grid)
        n = len(grid[0])
        partial_sums = grid[:]

        if m == 1 and n == 1:
            return grid[0][0]

        # Compute the partial sums on the first row
        # By adding the current number with the one before it
        for i in range(1, n):
            partial_sums[0][i] = grid[0][i - 1] + partial_sums[0][i]

        # Compute the partial sums on the first column
        # By adding the current number with the one before it
        for i in range(1, m):
            partial_sums[i][0] = grid[i - 1][0] + partial_sums[i][0]

        # Compute the partial sums in the rest of the matrix
        # By finding the minimum between the previous number row wise and the previous one column wise
        # And adding it with the current number
        for i in range(1, m):
            for j in range(1, n):
                partial_sums[i][j] = min(partial_sums[i - 1][j], partial_sums[i][j - 1]) \
                                     + partial_sums[i][j]

        return partial_sums[m - 1][n - 1]

    def min_path_sum_backtracking(self, grid):
        """
        :param grid: the matrix of positive numbers from which the minimum sum path from the top left
            position to the bottom right position will be computed
        :return: the sum of the numbers on the minimum sum path
        """
        # Data structure <=> Matrix
        # Algorithm <=> Backtracking

        # We need the optimal solution (the one which has a minimum sum) <=> backtracking
        # For each possible neighbour of a position, see if it leads to a solution
        # If an element doesn't lead to a solution, backtrack and try another neighbour

        # Time complexity <=> O(2 ^ (m * n)), where n is the size of the linked list
        # Space complexity <=> O(1)

        # Compute the start and the destination
        m = len(grid)
        n = len(grid[0])
        start = (0, 0)
        destination = (m - 1, n - 1)

        self.backtracking(m, n, grid, destination, start, grid[0][0])

        return self.min_sum

    def backtracking(self, m, n, grid, destination, current_position, current_sum):
        """
        :param m: the number of lines in the grid
        :param n: the number of columns in the grid
        :param grid: the matrix of positive numbers from which the minimum sum path from the top left
            position to the bottom right position will be computed
        :param destination: the tuple (x, y) which is the position of the destination (line x, column y)
        :param current_position: the tuple (x, y) which is the current position in the matrix
            (line x, column y)
        :param current_sum: the sum of the numbers so far on the current path
        :return: void
        """
        # Base case <=> the current position is the destination
        if current_position[0] == destination[0] and current_position[1] == destination[1]:
            if current_sum < self.min_sum:
                self.min_sum = current_sum

        # For every neighbour from the current position:
        # Compute the new position
        # Check if it's a valid position
        # If it is, add the number to the sum and move on from that position
        # Otherwise, backtrack and try another neighbour
        for i in range(2):
            line = current_position[0] + self.move_line[i]
            column = current_position[1] + self.move_column[i]
            new_position = (line, column)

            if self.valid_position(m, n, new_position):
                current_sum += grid[line][column]

                self.backtracking(m, n, grid, destination, new_position, current_sum)

                current_sum -= grid[line][column]

    def valid_position(self, m, n, position):
        """
        :param m: the number of lines in the grid
        :param n: the number of columns in the grid
        :param position: the tuple (x, y) which is the current position in the matrix
            (line x, column y)
        :return: True, if the current position is valid and False, otherwise
        """
        # Valid position <=> in the matrix
        line = position[0]
        column = position[1]

        if 0 <= line < m and 0 <= column < n:
            return True

        return False


# Example 1
grid1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

print(Solution().min_path_sum(grid1))
print("-------------------------------------")

# Example 2
grid1 = [[1, 2, 3], [4, 5, 6]]

print(Solution().min_path_sum(grid1))
print("-------------------------------------")

# Example 3
grid1 = [[1, 2], [5, 6], [1, 1]]

print(Solution().min_path_sum(grid1))
print("-------------------------------------")

# Example 4
grid1 = [[1, 4, 8, 6, 2, 2, 1, 7], [4, 7, 3, 1, 4, 5, 5, 1], [8, 8, 2, 1, 1, 8, 0, 1], [8, 9, 2, 9, 8, 0, 8, 9],
         [5, 7, 5, 7, 1, 8, 5, 5], [7, 0, 9, 4, 5, 6, 5, 6], [4, 9, 9, 7, 9, 1, 9, 0]]

print(Solution().min_path_sum(grid1))
