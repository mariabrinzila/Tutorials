class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        # Define a binary tree element (it has a value, a pointer to its left child, a pointer to its right
        # Child and a pointer to the next right node)
        # The next pointer basically computes a linked list level wise
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :param root: the perfect binary tree (all leaves are on the same level and every parent has 2
            children) which will have the next pointer populated for each node
        :return: the perfect binary tree with the next pointer populated
        """
        # Data structure <=> Binary Tree, Linked List

        # Time complexity <=> O(n * n), where n is the number of nodes in the perfect binary tree
        # Space complexity <=> O(n)

        # Base case <=> the perfect binary tree is empty or only has one node (the root)
        if root is None or (root.left is None and root.right is None):
            return root

        # While the queue isn't empty:
        # For each element on the current level in the queue:
        # Pop it and link them together using the next pointer
        queue = [root]

        while queue:
            size = len(queue)

            for i in range(size):
                current_node = queue.pop(0)

                if i != size - 1:
                    current_node.next = queue[0]

                if current_node.left is not None:
                    queue.append(current_node.left)

                if current_node.right is not None:
                    queue.append(current_node.right)

        return root

    def connect_bfs(self, root):
        """
        :param root: the perfect binary tree (all leaves are on the same level and every parent has 2
            children) which will have the next pointer populated for each node
        :return: the perfect binary tree with the next pointer populated
        """
        # Time complexity <=> O(n), where n is the number of nodes in the perfect binary tree
        # Space complexity <=> O(1)

        # While there are still nodes in the perfect binary tree:
        # Connect the appropriate nodes on that level using the next pointer to get access to all nodes
        # While the current node isn't empty:
        # If its left child isn't empty, make its next pointer point to its right child
        # As we know the binary tree is perfect so each node has both children
        # And if the current node's next pointer is None, make its right child's next point to
        # The current node's next left child
        # Otherwise (if the current node's left child is empty):
        # Stop the loop, since it means we got to a leaf node
        # Go on to the next node (on the left of the current node)
        tree_copy = root

        while root is not None:
            current = root

            while current is not None:
                if current.left is not None:
                    current.left.next = current.right

                    if current.next is not None:
                        current.right.next = current.next.left
                else:
                    break

                current = current.next

            root = root.left

        return tree_copy

    def connect_dfs(self, root):
        """
        :param root: the current node of the perfect binary tree (all leaves are on the same level and
            every parent has 2 children) which will have the next pointer populated for each node
        :return: the perfect binary tree with the next pointer populated
        """
        # Time complexity <=> O(n), where n is the number of nodes in the perfect binary tree
        # Space complexity <=> O(1) (O(log n) for the recursion stack)

        # If the root node isn't empty:
        # If the left child isn't empty (the root node isn't a leaf node):
        # Make the left child's next point to the right child
        # If the root node's next isn't None:
        # Make the right child's next point to the root node's next left child
        # Do the same for the left and right children
        if root is None:
            return None

        if root.left is not None:
            root.left.next = root.right

            if root.next is not None:
                root.right.next = root.next.left

            self.connect_dfs(root.left)
            self.connect_dfs(root.right)

        return root

    def print_linked_lists(self, root):
        """
        :param root: the perfect binary tree (all leaves are on the same level and every parent has 2
            children) which will have the next pointer populated for each node
        :return: the array of linked lists computed from the given perfect binary tree
            (each linked list is represented as an array of values)
        """
        # Time complexity <=> O(n * n), where n is the number of nodes in the perfect binary tree
        # Space complexity <=> O(n * 2)

        # Base case <=> the perfect binary tree is empty or only has one element (the root)
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [[-2000]]

        # While the queue isn't empty:
        # For each element on the current level in the queue:
        # Pop it and append its next node's value to the current linked list, if it isn't None
        # And append -2000, otherwise
        queue = [root]
        linked_lists = []

        while queue:
            current_linked_list = []
            size = len(queue)

            for i in range(size):
                current_node = queue.pop(0)

                if current_node.next is not None:
                    current_linked_list.append(current_node.next.val)
                else:
                    current_linked_list.append(-2000)

                if current_node.left is not None:
                    queue.append(current_node.left)

                if current_node.right is not None:
                    queue.append(current_node.right)

            linked_lists.append(current_linked_list)

        return linked_lists


# Example 1
root1 = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
solution = Solution()
root1 = solution.connect(root1)
root2 = solution.connect_bfs(root1)
root3 = solution.connect_dfs(root1)

print(solution.print_linked_lists(root1))
print(solution.print_linked_lists(root2))
print(solution.print_linked_lists(root3))
print("-------------------------------------")

# Example 2
root1 = None
solution = Solution()
root1 = solution.connect(root1)
root2 = solution.connect_bfs(root1)
root3 = solution.connect_dfs(root1)

print(solution.print_linked_lists(root1))
print(solution.print_linked_lists(root2))
print(solution.print_linked_lists(root3))
