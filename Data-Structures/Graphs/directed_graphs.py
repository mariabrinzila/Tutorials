import numpy as np


class DirectedGraph:
    def __init__(self, nr_vertices):
        self.v = nr_vertices
        self.matrix = np.zeros((self.v, self.v), int)

        # Each vertex has a None value at the beginning
        self.list = [None] * self.v

    def compute_adjacency_matrix(self, edges_set):
        """
        :param edges_set: the set of pairs (u, v) of edges (meaning there's an arc between u and v
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
        # While the queue isn't empty (there are still vertices to traverse):
        # Print the first element in the queue
        # Put all its neighbours in the queue
        queue = [start_vertex]
        visited_vertices = [start_vertex]
        traversal_result = "List BFS result is: "

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

    def topological_sorting(self):
        """
        :return: the stack containing the topological sorting of the DAG
        """
        stack = []
        visited_vertices = []

        # For every unvisited vertex:
        # Do the modified DFS from it
        for i in range(self.v):
            if i not in visited_vertices:
                self.topological_sorting_recursion(i, visited_vertices, stack)

        # Return the stack (reversed to keep the principle of a stack)
        return stack[::-1]

    def topological_sorting_recursion(self, vertex, visited, stack):
        """
        :param vertex: the vertex from which the traversal of the graph starts
        :param visited: the array of visited vertices
        :param stack: the array (stack) of vertices in the topological order
        :return: void
        """
        # Mark the vertex as visited
        visited.append(vertex)

        # For every adjacent vertex of vertex:
        # If it's not already been visited, do the modified DFS from it
        for i in range(self.v):
            if self.matrix[vertex][i] == 1 and i not in visited:
                self.topological_sorting_recursion(i, visited, stack)

        # Push the vertex to the stack when all its adjacent vertices and so on have been visited
        stack.append(vertex)

    def print_matrix(self):
        """
        :return: void (but prints the adjacency matrix)
        """
        for i in range(self.v):
            row = ""

            for j in range(self.v):
                row += str(self.matrix[i][j]) + " "

            print(row)
