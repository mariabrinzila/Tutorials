import numpy as np


def maze_initialization(size_line, size_column, start, destination, available_positions):
    """
    :param size_line: the number of lines in the maze matrix
    :param size_column: the number of columns in the maze matrix
    :param start: the tuple (x, y) which is the position of the start(line x, column y)
    :param destination: the tuple (x, y) which is the position of the destination (line x, column y)
    :param available_positions: the array of possible / available positions (which will be marked
        with 1)
    :return: void
    """
    # Compute movement arrays (4 possible directions)
    move_line = [-1, 1, 0, 0]
    move_column = [0, 0, -1, 1]

    # Compute the maze matrix
    maze = np.zeros((size_line, size_column), int)
    maze[start[0]][start[1]] = 2
    maze[destination[0]][destination[1]] = 2

    for position in available_positions:
        line = position[0]
        column = position[1]
        maze[line][column] = 1

    # Compute the shortest path from start to destination, if it exists
    result = shortest_path(size_line, size_column, maze, start, destination, move_line, move_column)

    if result != -1:
        print("There is a path from the start position to the destination one of length "
              + str(result) + ": ")

        for i in range(size_line):
            row = ""

            for j in range(size_column):
                row += str(maze[i][j]) + " "

            print(row)
    else:
        print("There is no possible path from the start position to the destination one")


def shortest_path(size_line, size_column, maze, start, destination, move_line, move_column):
    """
    :param size_line: the number of lines in the maze matrix
    :param size_column: the number of columns in the maze matrix
    :param maze: the maze matrix given initially where the start and the destination are marked with 2,
        the available positions are marked with 1 and the unavailable positions are marked with 0
    :param start: the tuple (x, y) which is the starting point (line x, column y)
    :param destination: the tuple (x, y) which is the position of the destination (line x, column y)
    :param move_line: the array of possible positions line wise from any starting position i
    :param move_column: the array of possible positions column wise from any starting position i
    :return: the path's length, if there is a path from the source to the destination and
        -1, otherwise
    """
    # While the queue isn't empty:
    # Pop an element from the queue
    # If the element is the destination, return the path length
    # For each possible neighbour:
    # If it's valid, add it to the queue, increment the path length and mark it as part of the path (with 2)
    queue = [start]
    path_length = 0

    while len(queue) > 0:
        current = queue.pop(0)

        if current == destination:
            return path_length

        for i in range(4):
            x = current[0] + move_line[i]
            y = current[1] + move_column[i]
            neighbour = (x, y)

            if valid_position(size_line, size_column, maze, neighbour, destination):
                path_length += 1
                queue.append(neighbour)
                maze[x][y] = 2

    return -1


def valid_position(size_line, size_column, maze, position, destination):
    """
    :param size_line: the number of lines in the maze matrix
    :param size_column: the number of columns in the maze matrix
    :param maze: the maze matrix given initially where the start and the destination are marked with 2,
        the available positions are marked with 1 and the unavailable positions are marked with 0
    :param position: the tuple (x, y) which is the current position in the matrix (line x, column y)
    :param destination: the tuple (x, y) which is the position of the destination (line x, column y)
    :return: True, if the current position is valid and False, otherwise
    """
    # Valid position <=> in the maze matrix and the position is available, or it's the destination
    line = position[0]
    column = position[1]

    if 0 <= line < size_line and 0 <= column < size_column and \
            (maze[line][column] == 1 or position == destination):
        return True

    return False


m = 5
n = 5
s = (0, 0)
d = (2, 1)
available = [(0, 2), (0, 3), (0, 4), (1, 0), (1, 2), (1, 4), (2, 0), (2, 2), (2, 4),
             (3, 4), (4, 0), (4, 1), (4, 2), (4, 4)]

maze_initialization(m, n, s, d, available)
