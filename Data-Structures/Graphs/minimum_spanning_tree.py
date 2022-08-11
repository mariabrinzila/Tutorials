import numpy as np


class MinimumSpanningTree:
    def __init__(self, nr_vertices):
        self.v = nr_vertices
        self.matrix = np.zeros((self.v, self.v), int)
        self.edges = {}

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
