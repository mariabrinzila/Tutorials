import numpy as np


def rat_maze_initialization(size, start, destination, available_positions):
    """
    :param size: the size of the maze (size * size)
    :param start: the tuple (x, y) which is the position of the start(line x, column y)
    :param destination: the tuple (x, y) which is the position of the destination (line x, column y)
    :param available_positions: the array of possible positions the rat may go to (which will be marked
        with 1)
    :return: void
    """
    # Compute movement arrays (the rat can move in 4 directions)
    move_line = [-1, 1, 0, 0]
    move_column = [0, 0, -1, 1]

    # Compute the maze matrix
    maze = np.zeros((size, size), int)
    maze[start[0]][start[1]] = 2
    maze[destination[0]][destination[1]] = 2

    for position in available_positions:
        line = position[0]
        column = position[1]
        maze[line][column] = 1

    # Compute the path from start to destination, if it exists
    result = rat_maze(size, maze, destination, start, move_line, move_column)

    if result:
        print("There is a path from the start position to the destination one: ")

        for i in range(size):
            row = ""

            for j in range(size):
                row += str(maze[i][j]) + " "

            print(row)
    else:
        print("There is no possible path from the start position to the destination one")


def rat_maze(size, maze, destination, current_position, move_line, move_column):
    """
    :param size: the size of the maze (size * size)
    :param maze: the maze matrix given initially where the start and the destination are marked with 2,
        the available positions are marked with 1 and the unavailable positions are marked with 0
    :param destination: the tuple (x, y) which is the position of the destination (line x, column y)
    :param current_position: the tuple (x, y) which is the position the rat is currently on in the
        matrix (line x, column y)
    :param move_line: the array of possible positions line wise from any starting position i
    :param move_column: the array of possible positions column wise from any starting position i
    :return: True, if there is a path from the source to the destination and False, otherwise
    """
    # Base case <=> the current position is the destination
    if current_position[0] == destination[0] and current_position[1] == destination[1]:
        return True

    # For every possible direction from the current position:
    # Compute the new position
    # Check if it's a valid position
    # If it is, mark it with a 2 to show it's on the path
    # Otherwise, backtrack and find another way, if possible
    for i in range(4):
        x = current_position[0] + move_line[i]
        y = current_position[1] + move_column[i]
        new_position = (x, y)

        if valid_position(size, maze, new_position, destination):
            maze[x][y] = 2

            if rat_maze(size, maze, destination, new_position, move_line, move_column):
                return True

            maze[x][y] = 1

    return False


def valid_position(size, maze, position, destination):
    """
    :param size: the size of the maze (size * size)
    :param maze: the maze matrix given initially where the start and the destination are marked with 2,
        the available positions are marked with 1 and the unavailable positions are marked with 0
    :param position: the tuple (x, y) which is the position the rat is currently on in the
        matrix (line x, column y)
    :param destination: the tuple (x, y) which is the position of the destination (line x, column y)
    :return: True, if the current position is valid and False, otherwise
    """
    # Valid position <=> in the maze matrix and the position is available, or it's the destination
    line = position[0]
    column = position[1]

    if 0 <= line < size and 0 <= column < size and (maze[line][column] == 1 or position == destination):
        return True

    return False
