class ListNode(object):
    def __init__(self, val=0, next=None):
        # Define a linked list element (it has a value and a pointer to the next element)
        self.val = val
        self.next = next


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        # Define a binary tree element (it has a value, a pointer to its left child
        # And a pointer to its right child)
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sorted_list_to_BST(self, head):
        """
        :param head: the sorted linked list (in ascending order) to be turned into a
            height balanced binary search tree (for every node in a BST, its left subtree contains
            values that are smaller than it, its right subtree contains values that are greater than
            it, both the left and right subtrees must also be BSTs and the height balanced BST
            is a binary tree in which the depth of the 2 subtrees of every node never differs by more
            than one)
        :return: the height balanced binary search tree (BST)
        """
        # Data structure <=> Linked List, Binary Search Tree, Array
        # Algorithm <=> Divide and Conquer

        # We need to create the binary search tree that is also height balanced from the linked list
        # So we can compute the array of values from the given linked list and
        # We can use the divide and conquer algorithm by splitting the array of values in order to
        # Find the next node to put in the BST
        # At every step, we find the middle of the array / section of the array
        # Put the element as the current root node in the BST
        # And compute its left and right children by splitting the part before and after the middle
        # And repeating the process until there's only one element left
        # This way we insert the right value at every step and don't have to remake the BST
        # To make sure the properties are being followed

        # Time complexity <=> O(n * 2), where n is the size of the linked list
        # Space complexity <=> O(n)

        # Compute the array of elements (values) in the given linked list
        values = self.traverse_linked_list(head)
        size = len(values)

        # Base case <=> the linked list is empty or only has one element
        if size == 0:
            return None
        elif size == 1:
            return TreeNode(values[0])

        return self.compute_BST(values, 0, size)

    def traverse_linked_list(self, linked_list):
        """
        :param linked_list: the linked list to be traversed
        :return: the array of elements (values) in the given linked list
        """
        # Time complexity <=> O(n), where n is the size of the linked list
        # Space complexity <=> O(n)

        # While the current element in the given linked list isn't None:
        # Put its value in the array of values
        # Make the current element the one after it
        elements = []

        while linked_list is not None:
            elements.append(linked_list.val)
            linked_list = linked_list.next

        return elements

    def compute_BST(self, array, left, right):
        """
        :param array: the array of elements (values) in the given linked list
        :param left: the index where the search interval (array section) begins
        :param right: the index where the search interval (array section) ends
        :return: the BST
        """
        # Time complexity <=> O(n), where n is the size of the linked list
        # Space complexity <=> O(1) (O(n) for the recursion stack)

        # If we still have elements to put in the section of the array between left and right:
        # Compute the middle of the section of the array
        # Create a binary tree node with the element in the section of the array on the middle position
        # The node's left subtree will have the elements of the section of the array
        # Between left and middle and the node's right subtree will have the elements of the section of
        # The array between middle + 1 and right
        # So at every step we create a node whose value is the element in the middle of the section
        # And we keep splitting the array and putting the elements before the middle in the left subtree
        # And the elements after the middle in the right subtree of the current node
        if left >= right:
            return None

        middle = (left + right) // 2
        current_node = TreeNode(array[middle])

        current_node.left = self.compute_BST(array, left, middle)
        current_node.right = self.compute_BST(array, middle + 1, right)

        return current_node

    def level_order(self, root):
        """
        :param root: the binary search tree that will be traversed in a level-order manner (from left to
            right, on every level)
        :return: the array representing the level-order traversal (each position i will contain a list
            of elements representing the nodes in the correct order on level i)
        """
        # Time complexity <=> O(n * n), where n is the number of nodes in the binary search tree
        # Space complexity <=> O(nr_l * m + 2 * n), where nr_l is the number of levels and m is
        # The maximum number of nodes on a level in the binary search tree

        # Base case <=> the binary search tree is empty or only has one node (the root)
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [[root.val]]

        # While the queue isn't empty:
        # Append the list of values for the current level to the traversal array
        # For each element on the current level in the queue:
        # Pop it and put its non-empty children in the queue
        queue = [root]
        current_level_values = [root.val]
        level_traversal = []

        while queue:
            level_traversal.append(current_level_values)
            size = len(queue)
            current_level_values = []

            for i in range(size):
                current_node = queue.pop(0)

                if current_node.left is not None:
                    queue.append(current_node.left)
                    current_level_values.append(current_node.left.val)

                if current_node.right is not None:
                    queue.append(current_node.right)
                    current_level_values.append(current_node.right.val)

        return level_traversal


# Example 1
lists1 = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
solution = Solution()
root1 = solution.sorted_list_to_BST(lists1)

print(solution.level_order(root1))
print("-------------------------------------")

# Example 2
lists1 = ListNode(-20, ListNode(-9, ListNode(0, ListNode(1,
                                                         ListNode(2,
                                                                  ListNode(3,
                                                                           ListNode(4,
                                                                                    ListNode(5,
                                                                                             ListNode(25)))))))))
solution = Solution()
root1 = solution.sorted_list_to_BST(lists1)

print(solution.level_order(root1))
print("-------------------------------------")

# Example 3
lists1 = None
solution = Solution()
root1 = solution.sorted_list_to_BST(lists1)

print(solution.level_order(root1))
