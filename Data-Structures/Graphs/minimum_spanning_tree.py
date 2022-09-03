import numpy as np


class MinimumSpanningTree:
    def __init__(self, nr_vertices):
        self.v = nr_vertices
        self.matrix = np.zeros((self.v, self.v), int)
        self.edges = {}

    def compute_adjacency_matrix(self, edges_set):
        """
        :param edges_set: the set of pairs (u, v, cost) of edges
            (meaning there's an edge between u and v and v and u with the weight cost)
        :return: void
        """
        self.edges = edges_set

        for edge in edges_set:
            i = edge[0]
            j = edge[1]
            cost = edge[2]

            # Set both edges (i, j) and (j, i) in the matrix to the cost ((i, j) = (j, i))
            self.matrix[i][j] = cost
            self.matrix[j][i] = cost

    def Kruskal(self):
        """
        :return: the array of edges in the computed MST and the weight of it
        """
        mst = []
        parents = [-1] * self.v
        smallest_edge_index = 0
        mst_weight = 0

        # Sort the edges in decreasing order based on the weight
        self.edges = sorted(self.edges, key=lambda item: item[2])

        # While the MST doesn't have V - e edges:
        # Pick the smallest edge
        # Check if it creates a cycle with the edges already added in the MST (the union-find algorithm)
        # If it creates a cycle, discard it
        # Otherwise, add it to the MST
        while len(mst) < self.v - 1:
            edge = self.edges[smallest_edge_index]
            i = edge[0]
            j = edge[1]
            cost = edge[2]
            smallest_edge_index += 1

            # Find i and j's parents
            parent_i = self.compute_parent(parents, i)
            parent_j = self.compute_parent(parents, j)

            # If including the (i, j) edge doesn't cost a cycle, include it in the MST
            # Otherwise, move on to the next edge
            if parent_i != parent_j:
                mst_weight += cost
                mst.append((i, j, cost))
                parents[parent_i] = parent_j

        return mst, mst_weight

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

    def Prim(self):
        """
        :return: the array of edges in the computed MST and the weight of it
        """
        # While not all vertices are in the MST:
        # Pick the vertex u with the smallest key value
        # Include u in the mst array
        # Update the key value of all adjacent vertices of u
        # For every adjacent vertex v, update its key value, if the cost of the (u, v) edge < keys[v]
        mst_vertices = []
        mst = []
        keys = [np.inf] * self.v
        previous = [-1] * self.v
        keys[0] = 0
        mst_weight = 0

        while len(mst_vertices) != self.v:
            smallest_key_value = np.inf
            smallest_key_value_vertex = -1

            for i in range(len(keys)):
                if keys[i] < smallest_key_value and i not in mst_vertices:
                    smallest_key_value = keys[i]
                    smallest_key_value_vertex = i

            mst_vertices.append(smallest_key_value_vertex)

            for i in range(self.v):
                if 0 < self.matrix[smallest_key_value_vertex][i] < keys[i] and i not in mst_vertices:
                    keys[i] = self.matrix[smallest_key_value_vertex][i]
                    previous[i] = smallest_key_value_vertex

        # Compute mst edges and weight using the array named previous
        for i in range(1, self.v):
            mst_weight += self.matrix[i][previous[i]]
            edge = (previous[i], i, self.matrix[i][previous[i]])
            mst.append(edge)

        return mst, mst_weight
