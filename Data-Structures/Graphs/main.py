import numpy as np


class UndirectedGraph:
    def __init__(self, nr_vertices):
        self.v = nr_vertices
        self.matrix = np.zeros((self.v, self.v), int)

        # Each vertex has a None value at the beginning
        self.list = [None] * self.v

    def compute_adjacency_matrix(self, edges_set):
        """
        :param edges_set: the set of pairs (u, v) of edges (meaning there's an edge between u and v
            and v and u
        :return: void
        """
        for edge in edges_set:
            i = edge[0]
            j = edge[1]

            # Set both edges (i, j) and (j, i) in the matrix to 1 ((i, j) = (j, i))
            self.matrix[i][j] = 1
            self.matrix[j][i] = 1

    def compute_adjacency_list(self, edges_set):
        """
        :param edges_set: the set of pairs (u, v) of edges (meaning there's an edge between u and v
            and v and u
        :return: void
        """
        for edge in edges_set:
            i = edge[0]
            j = edge[1]

            # Put j in i's list
            if self.list[i] is not None:
                self.list[i].append(j)
            else:
                self.list[i] = [j]

            # Put i in j's list
            if self.list[j] is not None:
                self.list[j].append(i)
            else:
                self.list[j] = [i]

    def bfs_matrix(self, start_vertex):
        """
        :param start_vertex: the vertex from which the traversal of the graph starts
        :return: the string containing the traversal result of the graph
        """
        queue = [start_vertex]
        visited_vertices = [start_vertex]
        traversal_result = "Matrix BFS result is: "

        # While the queue isn't empty (there are still vertices to traverse):
        # Print the first element in the queue
        # Put all its neighbours in the queue
        while queue:
            current = queue.pop(0)
            traversal_result += str(current) + " "

            for i in range(self.v):
                if self.matrix[current][i] == 1 and i not in visited_vertices:
                    queue.append(i)
                    visited_vertices.append(i)

        return traversal_result

    def dfs_list(self, start_vertex):
        """
        :param start_vertex: the vertex from which the traversal of the graph starts
        :return: the array containing the traversal result of the graph
        """
        visited_vertices = [start_vertex]
        self.backtracking(start_vertex, visited_vertices)

        return visited_vertices

    def backtracking(self, current_vertex, visited):
        """
        :param current_vertex: the vertex which will have its neighbours traversed
        :param visited: the array of visited vertices
        :return: void
        """
        if self.list[current_vertex] is not None:
            for neighbour in self.list[current_vertex]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    self.backtracking(neighbour, visited)

    def cycles_matrix(self):
        """
        :return: true, if the graph has cycles and false, otherwise
        """
        traversed_vertices = []

        for i in range(self.v):
            visited_vertices = []

            if self.dfs_modified(i, visited_vertices, traversed_vertices):
                return True

        return False

    def dfs_modified(self, vertex, visited, traversed):
        visited.append(vertex)
        traversed.append(vertex)

        for i in range(self.v):
            if self.matrix[vertex][i] == 1 and i not in visited:
                if i in traversed:
                    return True

                if self.dfs_modified(i, visited, traversed):
                    return True

        return False

    def print_matrix(self):
        """
        :return: void (but prints the adjacency matrix)
        """
        for i in range(self.v):
            row = ""

            for j in range(self.v):
                row += str(self.matrix[i][j]) + " "

            print(row)


class DirectedGraph:
    def __init__(self, nr_vertices):
        self.v = nr_vertices
        self.matrix = np.zeros((self.v, self.v), int)

        # Each vertex has a None value at the beginning
        self.list = [None] * self.v

    def compute_adjacency_matrix(self, edges_set):
        """
        :param edges_set: the set of pairs (u, v) of edges (meaning there's an edge between u and v
        :return: void
        """
        for edge in edges_set:
            i = edge[0]
            j = edge[1]

            # Only set edge (i, j) in the matrix to 1 ((i, j) != (j, i))
            self.matrix[i][j] = 1

    def compute_adjacency_list(self, edges_set):
        """
        :param edges_set: the set of pairs (u, v) of edges (meaning there's an edge between u and v
        :return: void
        """
        for edge in edges_set:
            i = edge[0]
            j = edge[1]

            # Put j in i's list
            if self.list[i] is not None:
                self.list[i].append(j)
            else:
                self.list[i] = [j]

    def bfs_list(self, start_vertex):
        """
        :param start_vertex: the vertex from which the traversal of the graph starts
        :return: the string containing the traversal result of the graph
        """
        queue = [start_vertex]
        visited_vertices = [start_vertex]
        traversal_result = "List BFS result is: "

        # While the queue isn't empty (there are still vertices to traverse):
        # Print the first element in the queue
        # Put all its neighbours in the queue
        while queue:
            current = queue.pop(0)
            traversal_result += str(current) + " "

            if self.list[current] is not None:
                for neighbour in self.list[current]:
                    if neighbour not in visited_vertices:
                        queue.append(neighbour)
                        visited_vertices.append(neighbour)

        return traversal_result

    def dfs_matrix(self, start_vertex):
        """
        :param start_vertex: the vertex from which the traversal of the graph starts
        :return: the array containing the traversal result of the graph
        """
        visited_vertices = [start_vertex]
        self.backtracking(start_vertex, visited_vertices)

        return visited_vertices

    def backtracking(self, current_vertex, visited):
        """
        :param current_vertex: the vertex which will have its neighbours traversed
        :param visited:
        :return: the array of visited vertices
        """
        for i in range(self.v):
            if self.matrix[current_vertex][i] == 1 and i not in visited:
                visited.append(i)
                self.backtracking(i, visited)

    def print_matrix(self):
        """
        :return: void (but prints the adjacency matrix)
        """
        for i in range(self.v):
            row = ""

            for j in range(self.v):
                row += str(self.matrix[i][j]) + " "

            print(row)


v = 5
edges = {(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)}

v = 4
edges = {(0, 1), (1, 2), (2, 3)}

v1 = 6
edges1 = {(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (3, 4), (3, 5), (4, 5)}

# Undirected graph
# Creation (matrix)
undirected_graph = UndirectedGraph(v)
undirected_graph.compute_adjacency_matrix(edges)

print("Undirected graph adjacency matrix: ")
undirected_graph.print_matrix()
print("---------------------------------------")

# Creation (list)
undirected_graph.compute_adjacency_list(edges)

print("Undirected graph adjacency list: ")
print(undirected_graph.list)
print("---------------------------------------")

# BFS (matrix)
print(undirected_graph.bfs_matrix(0))
print("---------------------------------------")

# DFS (list)
print("List DFS result is: ")
print(undirected_graph.dfs_list(0))
print("---------------------------------------")

# Cycles (list)
cycles = undirected_graph.cycles_matrix()

if cycles:
    print("The graph has cycles")
else:
    print("The graph is acyclic")
print("---------------------------------------")

# Directed graph
# Creation (matrix)
directed_graph = DirectedGraph(v1)
directed_graph.compute_adjacency_matrix(edges1)

print("Directed graph adjacency matrix: ")
directed_graph.print_matrix()
print("---------------------------------------")

# Creation (list)
directed_graph.compute_adjacency_list(edges)

print("Directed graph adjacency list: ")
print(directed_graph.list)
print("---------------------------------------")

# BFS (list)
print(directed_graph.bfs_list(0))
print("---------------------------------------")

# DFS (matrix)
print("Matrix DFS result is: ")
print(directed_graph.dfs_matrix(0))
print("---------------------------------------")
