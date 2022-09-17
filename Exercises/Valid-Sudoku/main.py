class Value:
    def __init__(self, row, column, box):
        # Define a value object (it contains a row, column and a sub-box)
        self.row = row
        self.column = column
        self.box = box


class Solution(object):
    def is_valid_sudoku(self, board):
        """
        :param board: a 9 x 9 matrix only containing '.' or digits (1 - 9) representing a Sudoku board
        :return: True, if the board is a valid Sudoku board (there must be no digit repetitions on rows,
            columns or in the 3 x 3 sub-boxes and only the filled cells should be validated) and False,
            otherwise
        """
        # Data structure <=> Hash Map and Matrix

        # Key <=> the digit (1 - 9)
        # Value <=> the corresponding object containing the current row, column and sub-box of the key
        # Hash function <=> H(i) = object, 1 <= i <= 9
        # Collisions will occur since every digit doesn't only appear once on the board
        # Each digit can appear maximum 9 times on the board (once in each sub-box)
        # In case of collisions <=> separate chaining (every index has an array of value objects)

        # Time complexity <=> O(81 * 9) = O(729) in the worst case
        # Space complexity <=> O(9)

        # For each element in the matrix (on the board):
        # If the element isn't '.':
        # Compute the object (the row, column and sub-box)
        # If the digit doesn't already exist in the hash map:
        # Add it with the computed object as the value
        # Otherwise, check if there are any collisions on the rows, columns or sub-boxes
        # If there are, the board is invalid
        # Otherwise, add the current object in the array of values for that key
        hash_map = dict()

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    key = int(board[i][j])
                    box = self.compute_sub_box(i, j)
                    value = Value(i, j, box)

                    if hash_map.get(key) is None:
                        hash_map[key] = [value]
                    else:
                        for value_object in hash_map[key]:
                            if value_object.row == i or value_object.column == j \
                                    or value_object.box == box:
                                return False

                        hash_map[key].append(value)

        return True

    def compute_sub_box(self, i, j):
        """
        :param i: the number which is the row index of the current element on the board
        :param j: the number which is the column index of the current element on the board
        :return: the number of the sub-box the current element on the board belongs to
        """
        # Time complexity <=> O(1)
        # Space complexity <=> O(1)

        # Sub-box 0
        if 0 <= i <= 2 and 0 <= j <= 2:
            return 0

        # Sub-box 1
        if 0 <= i <= 2 and 3 <= j <= 5:
            return 1

        # Sub-box 2
        if 0 <= i <= 2 and 6 <= j <= 8:
            return 2

        # Sub-box 3
        if 3 <= i <= 5 and 0 <= j <= 2:
            return 3

        # Sub-box 4
        if 3 <= i <= 5 and 3 <= j <= 5:
            return 4

        # Sub-box 5
        if 3 <= i <= 5 and 6 <= j <= 8:
            return 5

        # Sub-box 6
        if 6 <= i <= 8 and 0 <= j <= 2:
            return 6

        # Sub-box 7
        if 6 <= i <= 8 and 3 <= j <= 5:
            return 7

        # Sub-box 8
        return 8


# Example 1
board1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(Solution().is_valid_sudoku(board1))
print("-------------------------------------")

# Example 2
board1 = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(Solution().is_valid_sudoku(board1))
