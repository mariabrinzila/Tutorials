import numpy as np


class WeightedDirectedGraph:
    def __init__(self, nr_vertices):
        self.v = nr_vertices

        # Each vertex has a None value at the beginning
        self.list = [None] * self.v

        self.edges = {}

    def compute_adjacency_list(self, edges_set):
        """
        :param edges_set: the set of pairs (u, v, cost) of edges
            (meaning there's an arc between u and v with the weight cost)
        :return: void
        """
        self.edges = edges_set

        for edge in edges_set:
            i = edge[0]
            j = edge[1]
            cost = edge[2]

            # Put j and the cost in i's list
            current = (j, cost)

            if self.list[i] is not None:
                self.list[i].append(current)
            else:
                self.list[i] = [current]

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

        if self.list[source_vertex] is not None:
            for neighbour in self.list[source_vertex]:
                distances[neighbour[0]] = neighbour[1]

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

            if self.list[vertex] is not None:
                for neighbour in self.list[vertex]:
                    if neighbour[1] != 0 and neighbour[0] not in spt and \
                            distances[neighbour[0]] > distances[vertex] + neighbour[1]:
                        # The distance from the source vertex to the chosen one +
                        # The cost of the edge between it and the neighbour <
                        # The distance that was already in distances for the neighbour
                        distances[neighbour[0]] = distances[vertex] + neighbour[1]
                        parents[neighbour[0]] = vertex

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
        distances = [np.inf] * self.v
        distances[source_vertex] = 0

        # Compute the shortest distances in a bottom-up manner
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

    def floyd_warshall(self):
        """
        :return: the matrix containing the shortest paths between every 2 vertices in the graph
        """
        # Initialize the matrix:
        # 0 on the main diagonal
        # The cost of the edges given
        # Infinity for the rest of the positions
        solution_matrix = np.full((self.v, self.v), np.inf)

        for i in range(self.v):
            solution_matrix[i][i] = 0

        for edge in self.edges:
            i = edge[0]
            j = edge[1]
            cost = edge[2]
            solution_matrix[i][j] = cost

        # Pick the intermediate vertex
        for k in range(self.v):
            # Pick the source vertex
            for i in range(self.v):
                # Pick the destination vertex
                for j in range(self.v):
                    # Update the shortest path from the source to the destination, if necessary
                    if solution_matrix[i][j] > solution_matrix[i][k] + solution_matrix[k][j]:
                        solution_matrix[i][j] = solution_matrix[i][k] + solution_matrix[k][j]

        return solution_matrix
