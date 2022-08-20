from heapq import heappush, heappop, heapify
import numpy as np


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

    def decrease_key(self, position, new_key_value):
        """
        :param position: the position in the heap of the element whose value will change
        :param new_key_value: the new key value of the element on the given position in the heap
        :return: void
        """
        # Replace the key on the given position with the new value
        self.heap[position] = new_key_value
        parent_position = (position - 1) // 2

        # The heap has to be remade in order to maintain the heap property
        if new_key_value < self.heap[parent_position]:
            heapify(self.heap)

    def insertion(self, key_value):
        """
        :param key_value: the key value of the element which will be inserted in the heap
        :return: void
        """
        heappush(self.heap, key_value)

    def deletion(self, position):
        """
        :param position: the position in the heap of the element that will be deleted
        :return: void
        """
        # Decrease the value of the element on the given position to -inf
        # The element to be deleted will become the root of the heap
        self.decrease_key(position, (-1) * np.inf)

        # Pop the root of the heap (remove the smallest element)
        self.remove_minim()
