class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        # Define a binary tree element (it has a value, a pointer to its left child
        # And a pointer to its right child)
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        # Define an array of root to leaf node paths (each path is represented as an array of the values
        # Of the nodes on that path)
        self.paths = []

    def path_sum(self, root, target_sum):
        """
        :param root: the binary tree which may or may not have at least one path from the root to a
            leaf node (a node with no children) that adds up to the target sum
        :param target_sum: the sum that the values of the nodes from a root to leaf node path
            must add up to
        :return: the array of root to leaf node paths (each path is represented as an array of the values
            of the nodes on that path
        """
        # Data structure <=> Binary Tree, Array
        # Algorithm <=> DFS (Preorder)

        # We need to find all the paths from the root to a leaf node that add up to the target sum
        # So we need DFS since we need to go in depth in the binary tree (to find the leafs)
        # And we need the path from the root <=> the preorder traversal
        # Preorder <=> root, left, right

        # Time complexity <=> O(n), where n is the number of nodes in the binary tree
        # Space complexity <=> O(2 ^ level * (level + 1)), where level is the number of levels
        # In the binary tree (the root is on level 0)

        # Base cases <=> the root is empty, or the root is the only node in the binary tree
        if root is None:
            return []
        elif root.left is None and root.right is None and target_sum == root.val:
            return [[root.val]]
        elif root.left is None and root.right is None and target_sum != root.val:
            return []

        self.preorder(root, 0, target_sum, [])

        return self.paths

    def preorder(self, root, current_sum, target_sum, current_path):
        """
        :param root: the current node in the given binary tree which may or may not have at least one
            path from the root to a leaf node (a node with no children) that adds up to the target sum
        :param current_sum: the current sum of the nodes in the binary tree that have already
            been traversed
        :param target_sum: the sum that the values of the nodes from a root to leaf node path
            must add up to
        :param current_path: the array of values of the nodes on the current path from the root to
            a leaf node
        :return: void
        """
        # Time complexity <=> O(n), where n is the number of nodes in the binary tree
        # Space complexity <=> O(2 ^ level * (level + 1)), where level is the number of levels
        # In the binary tree (the root is on level 0)

        # Append the current node's value to the current path and add it to the current sum
        # If the current node is a leaf and the current sum is equal to the target sum:
        # Append the current path to the array of paths
        # Otherwise (the current node isn't a leaf node):
        # If its left subtree isn't empty, go in it
        # If its right subtree isn't empty, go in it
        # After the children the subtrees have been traversed and we are back to the current node:
        # Pop the node from the current path and subtract it from the current sum
        current_path.append(root.val)
        current_sum += root.val

        if root.left is None and root.right is None:
            if current_sum == target_sum:
                self.paths.append(current_path[:])
        else:
            if root.left is not None:
                self.preorder(root.left, current_sum, target_sum, current_path)

            if root.right is not None:
                self.preorder(root.right, current_sum, target_sum, current_path)

        current_path.pop(len(current_path) - 1)
        current_sum -= root.val


# Example 1
root1 = TreeNode(5,
                 TreeNode(4,
                          TreeNode(11,
                                   TreeNode(7),
                                   TreeNode(2)),
                          None),
                 TreeNode(8,
                          TreeNode(13),
                          TreeNode(4,
                                   TreeNode(5),
                                   TreeNode(1))))

print(Solution().path_sum(root1, 22))
print("-------------------------------------")

# Example 2
root1 = TreeNode(1,
                 TreeNode(2),
                 TreeNode(3))

print(Solution().path_sum(root1, 6))
print("-------------------------------------")

# Example 3
root1 = TreeNode(1,
                 TreeNode(2),
                 None)

print(Solution().path_sum(root1, 0))
print("-------------------------------------")

# Example 4
root1 = TreeNode(1,
                 TreeNode(2),
                 None)

print(Solution().path_sum(root1, 1))
print("-------------------------------------")

# Example 5
root1 = TreeNode(1,
                 TreeNode(-2,
                          TreeNode(1,
                                   TreeNode(-1),
                                   None),
                          TreeNode(3)),
                 TreeNode(-3,
                          TreeNode(-2),
                          None))

print(Solution().path_sum(root1, 2))
