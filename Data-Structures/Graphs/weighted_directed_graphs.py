import numpy as np


class WeightedDirectedGraph:
    def __init__(self, nr_vertices):
        self.v = nr_vertices

        # Each vertex has a None value at the beginning
        self.list = [None] * self.v

    def compute_adjacency_list(self, edges_set):
        """
        :param edges_set: the set of pairs (u, v, cost) of edges
            (meaning there's an arc between u and v with the weight cost)
        :return: void
        """
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
