from heapq import heappush, heappop, heapify


class MinHeap:
    def __init__(self):
        # The array in which we store the heap
        self.heap = []

    def creation(self, tree_root):
        """
        :param tree_root: the root of a complete binary tree that will be turned into a Min-Heap
        :return: True, if the complete binary tree given can be turned into a Min-Heap and False,
            otherwise
        """
        queue = [tree_root]

        # While there are still nodes in the binary tree to traverse:
        # Pop the first element from the queue and put it in the heap array
        # If the current root node has a left child, if its key is < its parent's key,
        # The heap condition is violated, otherwise put the child in the queue
        # If the current root node has a right child, if its key is < its parent's key,
        # The Min-Heap condition is violated, otherwise put the child in the queue
        while queue:
            current = queue.pop(0)
            self.heap.append(current.data)

            if current.left is not None:
                if current.left.data < current.data:
                    return False

                queue.append(current.left)

            if current.right is not None:
                if current.right.data < current.data:
                    return False

                queue.append(current.right)

        return True

    def get_minimum(self):
        """
        :return: the root in the heap (the smallest element)
        """
        return self.heap[0]

    def remove_minim(self):
        """
        :return: the root of the heap (the smallest element) before it's removed from the heap
        """
        return heappop(self.heap)
