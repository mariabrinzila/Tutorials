import numpy as np


class WeightedUndirectedGraph:
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

    def dijkstra_distances(self, source_vertex):
        """
        :param source_vertex: the vertex from which the shortest path and distance to all vertices
            will be computed
        :return: the array of distances from the source vertex to each vertex and the array of
            paths from the source vertex to each vertex
        """
        distances = [np.inf] * self.v
        parents = [source_vertex] * self.v
        spt = [source_vertex]
        distances[source_vertex] = 0
        parents[source_vertex] = 0

        for i in range(self.v):
            if self.matrix[source_vertex][i] > 0:
                distances[i] = self.matrix[source_vertex][i]

        # While not all vertices are in spt:
        # Compute the minimum distance and the vertex where that is
        # Push that vertex in spt
        # Compute the new distances
        while len(spt) != self.v:
            min_distance = np.inf
            vertex = -1

            for i in range(self.v):
                if i not in spt and distances[i] < min_distance:
                    min_distance = distances[i]
                    vertex = i

            if min_distance == np.inf:
                # Nothing more can be done since all distances are infinity
                break

            spt.append(vertex)

            for i in range(self.v):
                if self.matrix[vertex][i] != 0 and i not in spt and \
                        distances[i] > distances[vertex] + self.matrix[vertex][i]:
                    # The distance from the source vertex to the chosen one +
                    # The cost of the edge between it and i <
                    # The distance that was already in distances for i
                    distances[i] = distances[vertex] + self.matrix[vertex][i]
                    parents[i] = vertex

        # Compute paths from the source vertex to all vertices
        paths = self.dijkstra_paths(parents, distances, source_vertex)

        return distances, paths

    def dijkstra_paths(self, parents, distances, source_vertex):
        """
        :param parents: the array of predecessors for each vertex on the path from the source vertex
            to it
        :param distances: the array of minimum distances from the source vertex to each vertex
        :param source_vertex: the vertex from which the shortest path and distance to all vertices
            was computed
        :return: the array of paths from the source vertex to each vertex
        """
        # For each vertex:
        # If the distance between the source vertex and the current vertex is infinity, there is no path
        # Otherwise, compute the path by going through the parents array until finding the source vertex
        paths = []

        for i in range(self.v):
            if distances[i] == np.inf:
                paths.append([None])
            else:
                current_path = [i]

                while current_path[len(current_path) - 1] != source_vertex:
                    current_path.append(parents[current_path[len(current_path) - 1]])

                # Reverse the path so it starts with the source vertex
                paths.append(current_path[::-1])

        return paths

    def bellman_ford(self, source_vertex):
        """
        :param source_vertex: the vertex from which the shortest path and distance to all vertices
            will be computed
        :return: the array of distances from the source vertex to each vertex, if the graph doesn't
            contain negative weight cycles and False, otherwise
        """
        # Compute the shortest distances in a bottom-up manner
        distances = [np.inf] * self.v
        distances[source_vertex] = 0

        for i in range(self.v - 1):
            for edge in self.edges:
                u = edge[0]
                v = edge[1]
                cost = edge[2]

                if distances[u] != np.inf and distances[v] > distances[u] + cost:
                    distances[v] = distances[u] + cost

        # Check for negative weight cycles
        for edge in self.edges:
            u = edge[0]
            v = edge[1]
            cost = edge[2]

            if distances[u] != np.inf and distances[v] > distances[u] + cost:
                return False

        return distances

    def print_matrix(self):
        """
        :return: void (but prints the adjacency matrix)
        """
        for i in range(self.v):
            row = ""

            for j in range(self.v):
                row += str(self.matrix[i][j]) + " "

            print(row)
