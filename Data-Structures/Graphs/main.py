import numpy as np
from random import randrange


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
        :return: the array containing the traversal result of the graph
        """
        queue = [start_vertex]
        visited_vertices = [start_vertex]

        # While the queue isn't empty (there are still vertices to traverse):
        # Pop the first element in the queue
        # Put all its neighbours in the queue and visit them
        while queue:
            current = queue.pop(0)

            for i in range(self.v):
                if self.matrix[current][i] == 1 and i not in visited_vertices:
                    queue.append(i)
                    visited_vertices.append(i)

        return visited_vertices

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
        # While there are still unvisited neighbours from the current vertex:
        # Visit the first unvisited neighbour
        # Go to its neighbours (one level down)
        if self.list[current_vertex] is not None:
            for neighbour in self.list[current_vertex]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    self.backtracking(neighbour, visited)

    def connected(self):
        """
        :return: true, if the given graph is connected and false, otherwise
        """
        # Select a random vertex
        arbitrary = randrange(0, self.v)

        # Compute BFS traversal from that random vertex
        bfs_result = self.bfs_matrix(arbitrary)

        if len(bfs_result) == self.v:
            # The BFS traversal contains all the nodes so the graph is connected
            return True

        return False

    def connected_components(self):
        """
        :return: the array containing the graph's connected components
        """
        connected_components = []
        visited_vertices = []

        for i in range(self.v):
            if i not in visited_vertices:
                # Compute DFS traversal (the connected component) from every unvisited vertex
                visited_vertices = self.dfs_list(i)
                connected_components.append(visited_vertices)

        return connected_components

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

    def strongly_connected(self):
        """
        :return: true, if the graph is strongly connected and false, otherwise
        """
        # Kosaraju’s DFS based simple algorithm
        # Compute DFS traversal from the first vertex
        dfs_result = self.dfs_matrix(0)

        if len(dfs_result) != self.v:
            # Not strongly connected
            return False
        else:
            # Compute reversed graph
            transpose_graph = self.reversed_graph()
            matrix_copy = self.matrix.copy()
            self.matrix = transpose_graph.copy()

            # Compute DFS traversal from that random vertex on the reversed graph
            dfs_result = self.dfs_matrix(0)
            self.matrix = matrix_copy.copy()

            if len(dfs_result) != self.v:
                # Not strongly connected
                return False

        return True

    def reversed_graph(self):
        """
        :return: the matrix representation of the transpose / reversed graph
        """
        transpose_graph = np.zeros((self.v, self.v), int)

        for i in range(self.v):
            for j in range(self.v):
                if self.matrix[i][j] == 1:
                    # (i, j) in the original graph => (j, i) in the reversed one
                    # And vice versa
                    transpose_graph[j][i] = 1

        return transpose_graph

    def strongly_connected_components(self):
        """
        :return: the array containing the graph's strongly connected components
        """
        # Kosaraju’s algorithm
        strongly_connected_components = []
        stack = []
        visited_vertices = [0]

        for i in range(self.v):
            # Compute DFS traversal from the current vertex
            self.dfs_strongly_connected_component(i, visited_vertices, stack)

        # Compute reversed graph
        transpose_graph = self.reversed_graph()
        matrix_copy = self.matrix.copy()
        self.matrix = transpose_graph.copy()

        visited_vertices = []

        # While the stack isn't empty:
        # Pop an element
        # Compute DFS traversal from it (which will compute its strongly connected component)
        while stack:
            vertex = stack.pop()
            component = []

            self.dfs_reversed(vertex, visited_vertices, component)

            if len(component) > 0:
                strongly_connected_components.append(component)

        self.matrix = matrix_copy.copy()

        return strongly_connected_components

    def dfs_strongly_connected_component(self, vertex, visited, stack):
        """
        :param vertex: the vertex from which the traversal of the graph starts
        :param visited: the array of visited vertices
        :param stack: the array (stack) of vertices (in the order that they finish the recursion)
        :return: void
        """
        for i in range(self.v):
            if self.matrix[vertex][i] == 1 and i not in visited:
                visited.append(i)
                self.dfs_strongly_connected_component(i, visited, stack)

        if vertex not in stack:
            stack.append(vertex)

    def dfs_reversed(self, vertex, visited, component):
        """
        :param vertex: the vertex from which the traversal of the graph starts
        :param visited: the array of visited vertices
        :param component: the array of vertices in the current strongly connected component
        :return: void
        """
        if vertex not in visited and vertex not in component:
            visited.append(vertex)
            component.append(vertex)

        for i in range(self.v):
            if self.matrix[vertex][i] == 1 and i not in visited and i not in component:
                self.dfs_reversed(i, visited, component)

    def print_matrix(self):
        """
        :return: void (but prints the adjacency matrix)
        """
        for i in range(self.v):
            row = ""

            for j in range(self.v):
                row += str(self.matrix[i][j]) + " "

            print(row)


v = 6
edges = {(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)}

""" v = 5
edges = {(0, 1), (1, 3), (2, 3)} """

""" v1 = 6
edges1 = {(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (3, 4), (3, 5), (4, 5)} """

v1 = 9
edges1 = {(0, 3), (1, 0), (2, 1), (3, 2), (4, 2), (4, 6), (5, 4), (6, 5), (6, 7), (8, 7)}

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
print("Matrix BFS result is: ")
print(undirected_graph.bfs_matrix(0))
print("---------------------------------------")

# DFS (list)
print("List DFS result is: ")
print(undirected_graph.dfs_list(0))
print("---------------------------------------")

# Connectivity
if undirected_graph.connected():
    print("The graph is connected")
else:
    print("The graph is NOT connected and its connected components are:")
    print(undirected_graph.connected_components())
print("---------------------------------------")

# Directed graph
# Creation (matrix)
directed_graph = DirectedGraph(v1)
directed_graph.compute_adjacency_matrix(edges1)

print("Directed graph adjacency matrix: ")
directed_graph.print_matrix()
print("---------------------------------------")

# Creation (list)
directed_graph.compute_adjacency_list(edges1)

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

# Strong connectivity
if directed_graph.strongly_connected():
    print("The graph is strongly connected")
else:
    print("The graph is NOT strongly connected and its connected components are:")
    print(directed_graph.strongly_connected_components())
print("---------------------------------------")
