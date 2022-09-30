class Solution(object):
    def __init__(self):
        # Define 2 numbers representing the dimensions of the matrix
        self.m = 0
        self.n = 0

        # Define 2 movement arrays (we can either move vertically or horizontally, so 4 directions)
        self.move_line = [1, 0, -1, 0]
        self.move_column = [0, 1, 0, -1]

        # Define an array for marking an element as visited (its position / tuple of line, column will
        # Be appended to this array when an element is visited
        self.visited = []

    def exist(self, board, word):
        """
        :param board: the matrix of upper and lowercase English letters in which the string to be sought
            may or may not exist
        :param word: the string to be sought in the given matrix
        :return: True, if the string exists in the matrix and False, otherwise
        """
        # Data structure <=> Matrix and String
        # Algorithm <=> Backtracking

        # We need to check if there is a solution <=> backtracking
        # We'll traverse the matrix and once we find the current character in the string:
        # We look at its neighbours and see if the current character in the string
        # Corresponds to any of the neighbours
        # If it does, we go on that path and see if we reach the solution (the whole string)
        # Otherwise, we go back and look for that current character elsewhere in the matrix

        # Time complexity <=> O(m * n * 4 * s), where m and n are the dimensions of the matrix
        # And s is the size of the string
        # Space complexity <=> O(s)

        # Compute the dimensions of the matrix
        self.m = len(board)
        self.n = len(board[0])

        # Base case <=> the matrix only has one element
        if self.m == self.n == 1:
            if len(word) != 1 or (len(word) == 1 and word[0] != board[0][0]):
                return False
            elif len(word) == 1 and word[0] == board[0][0]:
                return True

        # Check if every character in the given string exists in the matrix
        # If a character in the given string doesn't exist in the matrix:
        # Ee already know we won't find the solution
        for character in word:
            if not any(character in sub for sub in board):
                return False

        # For each element in the matrix:
        # If it's equal to the first character in the given string, do backtracking from that position
        # Otherwise, keep searching
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    self.visited.append((i, j))

                    if self.backtracking(board, (i, j), word, 1):
                        return True

                    self.visited.remove((i, j))

        return False

    def backtracking(self, board, current, string, position):
        """
        :param board: the matrix of upper and lowercase English letters in which the string to be sought
            may or may not exist
        :param current:  the tuple (x, y) which is the current position in the matrix
            (line x, column y)
        :param string: the string to be sought in the given matrix
        :param position: the position in the given string of the current character to be sought
            in the matrix
        :return: True, if the solution can be computed from the current position in the matrix and
            False, otherwise
        """
        # Time complexity <=> O(4 * s), where s is the size of the string
        # Space complexity <=> O(s)

        # Base case <=> the position in the given string of the current character is the end
        # Of the string, so the solution has been reached
        if position == len(string):
            return True

        # If we haven't already reached a solution:
        # If the position in the given string of the current character isn't the end of the string:
        # For each valid neighbour (in the matrix and unvisited) of the current position in the matrix:
        # If it corresponds to the current character in the given string:
        # Go on from that point and see if it leads to the solution
        # If no neighbour corresponds, the current element doesn't lead to the solution
        for i in range(4):
            row = current[0] + self.move_line[i]
            column = current[1] + self.move_column[i]
            new = (row, column)

            if 0 <= row < self.m and 0 <= column < self.n and new not in self.visited \
                    and board[row][column] == string[position]:
                self.visited.append(new)

                if self.backtracking(board, new, string, position + 1):
                    return True

                self.visited.remove(new)


# Example 1
grid = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
s = "ABCCED"

print(Solution().exist(grid, s))
print("-------------------------------------")

# Example 2
grid = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
s = "SEE"

print(Solution().exist(grid, s))
print("-------------------------------------")

# Example 3
grid = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
s = "ABCB"

print(Solution().exist(grid, s))
print("-------------------------------------")

# Example 4
grid = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],
        ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"]]
s = "AAAAAAAAAAAAAAB"

print(Solution().exist(grid, s))
