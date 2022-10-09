import numpy as np


class Solution(object):
    def find_order(self, num_courses, prerequisites):
        """
        :param num_courses: the number of courses that we'll determine if we can take and we'll find
            an ordering in which to take them
        :param prerequisites: the array of arrays [a, b] representing the fact that you must take course b
            first, if you want to take course a
        :return: the array containing the ordering in which all the courses will be taken, if it's possible
            to take the given number of courses given the prerequisites and an empty array, otherwise
        """
        # Data structure <=> Array, Graph
        # Algorithm <=> DFS, Topological Sorting

        # We can see the courses as vertices in a graph and the reversed prerequisite pairs as arcs between
        # The vertices ([a, b] is the arc between b and a) <=> directed graph
        # Finding an order in which to take the courses so that the prerequisites are applied
        # Comes down to finding an ordering in the graph such that for every arc (u, v),
        # Vertex u comes before vertex v in the ordering <=> topological sorting
        # But to do topological sorting, we must make sure the graph doesn't contain cycles
        # Which is how we'll know if the ordering can be done or not <=> modified DFS
        # In the modified DFS, we check if a visited vertex is also already in the recursion stack
        # So to compute the ordering in which the courses can be taken
        # We need to check the computed graph doesn't contain any cycles
        # And then do topological sorting which will give us the ordering

        # Time complexity <=> O((V + E) * 2), where V is the number of courses
        # And E is the size of the array
        # Space complexity <=> O(V)

        # Base case <=> the given number of courses is 1
        if num_courses == 1:
            return [0]

        # Compute the directed graph represented with an adjacency matrix (it'll have the same number
        # Of vertices as the total number of courses)
        # And the edges will be the reversed prerequisite pairs (pair [a, b] will be arc (b, a) in order
        # To keep the condition for the topological sorting that
        # For every arc (u, v), u must be between v in the ordering)
        graph = np.zeros((num_courses, num_courses), int)

        for prerequisite in prerequisites:
            graph[prerequisite[1]][prerequisite[0]] = 1

        # For each vertex in the graph:
        # Do the modified DFS and if the result is True, the graph contains cycles
        # And so we can't perform topological sorting
        visited = [False] * (num_courses + 1)
        stack = [False] * (num_courses + 1)

        for i in range(num_courses):
            if not visited[i]:
                if self.modified_dfs(i, num_courses, graph, visited, stack):
                    return []

        # If the graph, doesn't contain any cycles, we can do topological sorting
        # The topological sorting algorithm is basically a modified DFS where we process the neighbours
        # Of the current vertex, their neighbours etc. (we add them to the ordering array first)
        # And then we add the current vertex
        # For each vertex in the graph:
        # If the current vertex hasn't been visited yet:
        # Do the modified DFS from it
        # At the end, the ordering will be the reversed computed one
        ordering = []
        visited = []

        for i in range(num_courses):
            if i not in visited:
                self.topological_sorting(i, num_courses, graph, visited, ordering)

        return ordering[::-1]

    def modified_dfs(self, current_vertex, v, graph, visited, stack):
        """
        :param current_vertex: the number of the current vertex which will have its neighbours traversed
        :param v: the number representing the total number of vertices in the directed graph
        :param graph: the matrix representing the directed graph
        :param visited: the array of already visited vertices
        :param stack: the array representing the recursion stack for the modified DFS
        :return: True, if the graph contains cycles and False, otherwise
        """
        # Time complexity <=> O(V + E), where V is the number of courses and E is the size of the array
        # Space complexity <=> O(V)

        # Mark the current vertex as visited and add it to the recursion stack
        # For each neighbour of the current vertex:
        # If the current neighbour isn't visited, do the modified DFS from it
        # If the recursive function returns true for the current neighbour, the graph has a cycle
        # Otherwise (the current neighbour is visited):
        # If it's in the recursion stack, the graph has a cycle
        # If by the end there haven't been any cycles found, pop the current vertex from the recursion stack
        visited[current_vertex] = True
        stack[current_vertex] = True

        for i in range(v):
            if graph[current_vertex][i] == 1:
                if not visited[i]:
                    if self.modified_dfs(i, v, graph, visited, stack):
                        return True
                elif stack[i]:
                    return True

        stack[current_vertex] = False

        return False

    def topological_sorting(self, vertex, v, graph, visited, ordering):
        """
        :param vertex: the number of the current vertex which will have its neighbours traversed
        :param v: the number representing the total number of vertices in the directed graph
        :param graph: the matrix representing the directed graph
        :param visited: the array of already visited vertices
        :param ordering: the array representing the order of the vertices in the topological sorting
              ordering
        :return: void
        """
        # Time complexity <=> O(V + E), where V is the number of courses and E is the size of the array
        # Space complexity <=> O(V)

        # Mark the current vertex as visited
        # For every adjacent vertex of the current vertex (every neighbour):
        # If the current neighbour has not already been visited, go from it deeper in the graph
        # At the end (after all the current vertex's neighbours have been processed and their neighbours
        # And so on), add the current vertex to the ordering array
        # Its neighbours and their neighbours and so on have already been added to the ordering array
        visited.append(vertex)

        for i in range(v):
            if graph[vertex][i] == 1 and i not in visited:
                self.topological_sorting(i, v, graph, visited, ordering)

        ordering.append(vertex)


# Example 1
num = 2
pre = [[1, 0]]

print(Solution().find_order(num, pre))
print("-------------------------------------")

# Example 2
num = 4
pre = [[1, 0], [2, 0], [3, 1], [3, 2]]

print(Solution().find_order(num, pre))
print("-------------------------------------")

# Example 3
num = 1
pre = []

print(Solution().find_order(num, pre))
