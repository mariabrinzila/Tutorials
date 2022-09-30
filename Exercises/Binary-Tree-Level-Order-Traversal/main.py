class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        # Define a binary tree element (it has a value, a pointer to its left child
        # And a pointer to its right child)
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def level_order(self, root):
        """
        :param root: the binary tree that will be traversed in a level-order manner (from left to right,
            on every level)
        :return: the array representing the level-order traversal (each position i will contain a list
            of elements representing the nodes in the correct order on level i)
        """
        # Data structure <=> Binary Tree, Queue, Array
        # Algorithm <=> BFS

        # We need to traverse the nodes on each level <=> BFS

        # Time complexity <=> O(n * n), where n is the number of nodes in the binary tree
        # Space complexity <=> O(nr_l * m + 2 * n), where nr_l is the number of levels and m is
        # The maximum number of nodes on a level in the binary tree

        # Base case <=> the binary tree is empty or only has one node (the root)
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
root1 = TreeNode(3,
                 TreeNode(9),
                 TreeNode(20,
                          TreeNode(15, None),
                          TreeNode(7, None)))

print(Solution().level_order(root1))
print("-------------------------------------")

# Example 2
root1 = TreeNode(4,
                 TreeNode(5,
                          TreeNode(8, None),
                          TreeNode(10,
                                   TreeNode(14),
                                   None)),
                 TreeNode(6,
                          TreeNode(2,
                                   None,
                                   TreeNode(15)),
                          TreeNode(11)))

print(Solution().level_order(root1))
print("-------------------------------------")

# Example 3
root1 = TreeNode(1)

print(Solution().level_order(root1))
print("-------------------------------------")

# Example 4
root1 = None

print(Solution().level_order(root1))
