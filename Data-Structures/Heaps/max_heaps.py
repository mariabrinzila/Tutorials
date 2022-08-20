import numpy as np


class MaxHeap:
    def __init__(self):
        # The array in which we store the heap
        self.heap = []

    def creation(self, tree_root):
        """
        :param tree_root: the root of a complete binary tree that will be turned into a Max-Heap
        :return: True, if the complete binary tree given can be turned into a Max-Heap and False,
            otherwise
        """
        queue = [tree_root]

        # While there are still nodes in the binary tree to traverse:
        # Pop the first element from the queue and put it in the heap array
        # If the current root node has a left child, if its key is > its parent's key,
        # The heap condition is violated, otherwise put the child in the queue
        # If the current root node has a right child, if its key is > its parent's key,
        # The Min-Heap condition is violated, otherwise put the child in the queue
        while queue:
            current = queue.pop(0)
            self.heap.append(current.data)

            if current.left is not None:
                if current.left.data > current.data:
                    return False

                queue.append(current.left)

            if current.right is not None:
                if current.right.data > current.data:
                    return False

                queue.append(current.right)

        return True

    def get_maximum(self):
        """
        :return: the root in the heap (the greatest element)
        """
        return self.heap[0]

    def remove_maximum(self):
        """
        :return: the root of the heap (the greatest element) before it's removed from the heap
        """
        # Get the root of the heap
        maximum = self.heap[0]

        # Remake the heap moving down, if necessary
        if self.heap[1] > self.heap[2]:
            self.heap[0] = self.heap[1]
            self.remake_heap_down(1)
        else:
            self.heap[0] = self.heap[2]
            self.remake_heap_down(2)

        return maximum

    def remake_heap_down(self, position):
        """
        :param position: the position of the current root (parent) in the heap
        :return: void
        """
        # While we haven't gotten to the last level:
        # Pick the maximum key value out of the current node's children
        # Replace the parent's key with the maximum
        # After the traversal is over, delete the last node
        while position <= (len(self.heap) - 3) // 2:
            left = self.heap[2 * position + 1]
            right = self.heap[2 * position + 2]

            if left > right:
                self.heap[position] = left
                position = 2 * position + 1
            else:
                self.heap[position] = right
                position = 2 * position + 2

        del self.heap[position]

    def increase_key(self, position, new_key_value):
        """
        :param position: the position in the heap of the element whose value will change
        :param new_key_value: the new key value of the element on the given position in the heap
        :return: void
        """
        # Replace the key on the given position with the new value
        self.heap[position] = new_key_value
        parent_position = (position - 1) // 2

        self.remake_heap_up(position, parent_position)

    def remake_heap_up(self, position, parent_position):
        """
        :param position: the position of the current element in the heap (a child)
        :param parent_position: the position of the current element's parent in the heap
        :return: void
        """
        # While there are still elements positioned incorrectly in the heap
        # And we haven't reached the root:
        # Swap parent and child
        # Go up in the heap
        while position > 0 and self.heap[position] > self.heap[parent_position]:
            copy = self.heap[parent_position]
            self.heap[parent_position] = self.heap[position]
            self.heap[position] = copy

            position = parent_position
            parent_position = (position - 1) // 2

    def insertion(self, key_value):
        """
        :param key_value: the key value of the element which will be inserted in the heap
        :return: void
        """
        # Insert element at the end of the heap
        self.heap.append(key_value)

        # Remake the heap moving up, if it's necessary
        position = len(self.heap) - 1
        parent_position = (position - 1) // 2
        self.remake_heap_up(position, parent_position)

    def deletion(self, position):
        """
        :param position: the position in the heap of the element that will be deleted
        :return: void
        """
        # Increase the value of the element on the given position to inf
        # The element to be deleted will become the root of the heap
        self.increase_key(position, np.inf)

        # Pop the root of the heap (remove the greatest element)
        self.remove_maximum()
