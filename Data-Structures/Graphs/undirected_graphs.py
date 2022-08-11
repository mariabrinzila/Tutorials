import numpy as np
from random import randrange


class UndirectedGraph:
    def __init__(self, nr_vertices):
        self.v = nr_vertices
        self.matrix = np.zeros((self.v, self.v), int)
        self.edges = {}

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
        self.edges = edges_set

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

    def union_find(self):
        """
        :return: true, if the graph contains cycles and false, otherwise
        """
        # Initialization
        parents = [-1] * self.v

        # Process every edge
        for edge in self.edges:
            i = edge[0]
            j = edge[1]

            # Find
            parent_i = self.compute_parent(parents, i)
            parent_j = self.compute_parent(parents, j)

            # The 2 vertices have the same parent, so they're in the same subset
            if parent_i == parent_j:
                return True

            # Union
            parents[parent_i] = parent_j

        return False

    def compute_parent(self, parents, vertex):
        """
        :param parents: the array of parents for each vertex in which we keep track of the
            subset each vertex is in
        :param vertex: the vertex whose parent we want to compute
        :return: the vertex's parent (subset)
        """
        if parents[vertex] == -1:
            return vertex

        return self.compute_parent(parents, parents[vertex])

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
