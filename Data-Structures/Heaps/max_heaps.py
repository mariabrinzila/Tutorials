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
        maximum = self.heap[0]

        if self.heap[1] > self.heap[2]:
            self.heap[0] = self.heap[1]
            self.remake_heap(1)
        else:
            self.heap[0] = self.heap[2]
            self.remake_heap(2)

        return maximum

    def remake_heap(self, i):
        """
        :param i: the current positin of a root (parent) in the heap
        :return: void
        """
        # While we haven't gotten to the last level:
        # Pick the maximum key value out of the current node's children
        # Replace the parent's key with the maximum
        # After the traversal is over, delete the last node
        while i < (len(self.heap) - 2) / 2:
            left = self.heap[2 * i + 1]
            right = self.heap[2 * i + 2]

            if left > right:
                self.heap[i] = left
                i = 2 * i + 1
            else:
                self.heap[i] = right
                i = 2 * i + 2

        del self.heap[i]
