import undirected_graphs as ug
import directed_graphs as dg
import weighted_undirected_graphs as wug
import weighted_directed_graphs as wdg
import minimum_spanning_tree as mst


# Example 1
v = 6
edges = {(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)}

""" v = 5
edges = {(0, 1), (1, 3), (2, 3)} """

""" v1 = 6
edges1 = {(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (3, 4), (3, 5), (4, 5)} """

""" v1 = 9
edges1 = {(0, 3), (1, 0), (2, 1), (3, 2), (4, 2), (4, 6), (5, 4), (6, 5), (6, 7), (8, 7)} """

# Example 2
v1 = 6
edges1 = {(2, 3), (3, 1), (4, 0), (4, 1), (5, 0), (5, 2)}

# Undirected graph
# Creation (matrix)
undirected_graph = ug.UndirectedGraph(v)

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

# Cycles (the Union-Find algorithm)
result = undirected_graph.union_find()

if result:
    print("The graph contains cycles")
else:
    print("The graph is acyclic")
print("---------------------------------------")

# Connectivity
if undirected_graph.connected():
    print("The graph is connected")
else:
    print("The graph is NOT connected and its connected components are:")

    print(undirected_graph.connected_components())

print("                                       ")
print("***************************************")
print("                                       ")

# Directed graph
# Creation (matrix)
directed_graph = dg.DirectedGraph(v1)

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

# Topological sorting
print("Topological sorting result is: ")

print(directed_graph.topological_sorting())

print("                                       ")
print("***************************************")
print("                                       ")

# Example 1
v2 = 9
edges2 = {(0, 1, 4), (0, 7, 8), (1, 7, 11), (1, 2, 8), (2, 8, 2), (2, 3, 7), (2, 5, 4),
          (3, 4, 9), (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 8, 6), (6, 7, 1), (7, 8, 7)}

# Example 2
v3 = 5
edges3 = {(1, 0, -1), (1, 2, 4), (0, 2, 3), (0, 3, 2), (0, 4, 2), (3, 0, 1), (3, 2, 5),
          (4, 3, -3)}

""" v3 = 4
edges3 = {(0, 1, 5), (0, 3, 10), (1, 2, 3), (2, 3, 1)} """

# Weighted undirected graph
# Creation (matrix)
weighted_undirected_graph = wug.WeightedUndirectedGraph(v2)

weighted_undirected_graph.compute_adjacency_matrix(edges2)

print("Weighted undirected graph adjacency matrix: ")

weighted_undirected_graph.print_matrix()

print("---------------------------------------")

# Dijkstra's algorithm  (matrix)
distances, paths = weighted_undirected_graph.dijkstra_distances(0)

print("Dijkstra distances from source vertex 0 to all vertices are: ")
print(distances)
print("---------------------------------------")

print("Dijkstra paths from source vertex 0 to all vertices are: ")
print(paths)
print("---------------------------------------")

# The Bellman-Ford algorithm
result = weighted_undirected_graph.bellman_ford(0)

if not result:
    print("The graphs contains negative weight cycles and the distances can't be computed")
else:
    print("Bellman-Ford distances from source vertex 0 to all vertices are: ")
    print(result)

print("                                       ")
print("***************************************")
print("                                       ")

# Weighted directed graph
# Creation (list)
weighted_directed_graph = wdg.WeightedDirectedGraph(v3)

weighted_directed_graph.compute_adjacency_list(edges3)

print("Weighted directed graph adjacency list: ")
print(weighted_directed_graph.list)
print("---------------------------------------")

# Dijkstra's algorithm (list)
distances, paths = weighted_directed_graph.dijkstra_distances(0)

print("Dijkstra distances from source vertex 0 to all vertices are: ")
print(distances)
print("---------------------------------------")

print("Dijkstra paths from source vertex 0 to all vertices are: ")
print(paths)
print("---------------------------------------")

# The Bellman-Ford algorithm
result = weighted_directed_graph.bellman_ford(1)

if not result:
    print("The graphs contains negative weight cycles and the distances can't be computed")
else:
    print("Bellman-Ford distances from source vertex 1 to all vertices are: ")
    print(result)

print("---------------------------------------")

# The Floyd Warshall algorithm
solution = weighted_directed_graph.floyd_warshall()

print("Floyd Warshall distance matrix is: ")
print(solution)

print("                                       ")
print("***************************************")
print("                                       ")

# Minimum spanning tree (MST)
# Kruskal's algorithm
""" v4 = 4
edges4 = {(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)} """

v4 = 5
edges4 = {(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)}

minimum_spanning_tree = mst.MinimumSpanningTree(v4)

minimum_spanning_tree.compute_adjacency_matrix(edges4)

# Kruskal's algorithm
result, cost = minimum_spanning_tree.Kruskal()

print("The minimum spanning tree computed with Kruskal's algorithm has the weight " + str(cost) +
      " and the edges: ")
print(result)
print("---------------------------------------")

# Prim's algorithm
minimum_spanning_tree = mst.MinimumSpanningTree(v2)

minimum_spanning_tree.compute_adjacency_matrix(edges2)
result, cost = minimum_spanning_tree.Prim()

print("The minimum spanning tree computed with Prim's algorithm has the weight " + str(cost) +
      " and the edges: ")
print(result)
print("---------------------------------------")
