class Solution(object):
    def __init__(self):
        # Define a movement array on the line and column (we can only move horizontally or vertically)
        self.move_line = [-1, 0, 1, 0]
        self.move_column = [0, -1, 0, 1]

    def num_islands(self, grid):
        """
        :param grid: the matrix only containing 1 (land) and 0 (water) from which the number of
            islands will be computed (an island is surrounded by water and is formed by connecting
            adjacent lands horizontally or vertically)
        :return: the number of islands in the given matrix
        """
        # Data structure <=> Matrix
        # Algorithm <=> Backtracking (DFS)

        # We need to find all islands (adjacent lands)
        # So when we find a land element, we must explore its neighbours and then their neighbours
        # And so on
        # So we explore the neighbours in depth <=> backtracking

        # Time complexity <=> O(m * n * m * n), where m, n are the dimensions of the matrix
        # Space complexity <=> O(4)

        # Base case <=> the matrix only has 1 element
        m = len(grid)
        n = len(grid[0])

        if m == 1 and n == 1:
            if grid[0][0] == "0":
                return 0
            else:
                return 1

        # For each element in the given matrix:
        # If the current element is an unvisited land (1):
        # Increment the number of islands
        # Start backtracking from that position to find all the land elements in that island
        islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1

                    self.backtracking(grid, m, n, (i, j))

        return islands

    def backtracking(self, grid, m, n, current_position):
        """
        :param grid: the m x n matrix only containing 1 (land) and 0 (water) from which the number of
            islands will be computed (an island is surrounded by water and is formed by connecting
            adjacent lands horizontally or vertically)
        :param m: the number of lines in the matrix
        :param n: the number of columns in the matrix
        :param current_position: the tuple (line, column) representing the current position
        :return: void
        """
        # Time complexity <=> O(m * n), where m, n are the dimensions of the matrix
        # Space complexity <=> O(4)

        # If the element on the current position is available (in the matrix)
        # And an unvisited land (1):
        # Mark it as visited (by changing its value to -1)
        # For each possible neighbouring position:
        # Do backtracking to find all the other lands in the current island
        if 0 <= current_position[0] < m and 0 <= current_position[1] < n \
                and grid[current_position[0]][current_position[1]] == "1":
            grid[current_position[0]][current_position[1]] = "-1"

            for k in range(4):
                new_i = current_position[0] + self.move_line[k]
                new_j = current_position[1] + self.move_column[k]

                self.backtracking(grid, m, n, (new_i, new_j))


# Example 1
grid1 = [["1", "1", "1", "1", "0"],
         ["1", "1", "0", "1", "0"],
         ["1", "1", "0", "0", "0"],
         ["0", "0", "0", "0", "0"]]

print(Solution().num_islands(grid1))
print("-------------------------------------")

# Example 2
grid1 = [["1", "1", "0", "0", "0"],
         ["1", "1", "0", "0", "0"],
         ["0", "0", "1", "0", "0"],
         ["0", "0", "0", "1", "1"]]

print(Solution().num_islands(grid1))
print("-------------------------------------")

# Example 3
grid1 = [["0"]]

print(Solution().num_islands(grid1))
print("-------------------------------------")

# Example 4
grid1 = [["1", "0", "1", "1", "0", "1", "1"]]

print(Solution().num_islands(grid1))
print("-------------------------------------")

# Example 5
grid1 = [["0", "0", "0", "0", "0", "0", "1"]]

print(Solution().num_islands(grid1))
