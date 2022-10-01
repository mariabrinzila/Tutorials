class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        # Define a binary tree element (it has a value, a pointer to its left child
        # And a pointer to its right child)
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.diameter = 0

    def diameter_of_binary_tree(self, root):
        """
        :param root: the binary tree whose diameter (the length of the longest path between any two nodes
            in the binary tree) will be computed
        :return: the binary tree's diameter
        """
        # Data structure <=> Binary Tree
        # Algorithm <=> DFS

        # We need to traverse the whole binary tree and compute the diameter of every node <=> DFS
        # And store the maximum diameter of a node

        # Time complexity <=> O(n * n), where n is the number of nodes in the binary tree
        # Space complexity <=> O(1)

        # Base case <=> the binary tree is empty or has maximum 1 child
        if root is None:
            return -1
        elif root.left is None and root.right is None:
            return 0
        elif (root.left is None and root.right is not None and root.right.left is None
              and root.right.right is None) or (root.right is None and root.left is not None
                                                and root.left.left is None and root.left.right is None):
            return 1

        self.dfs(root)

        return self.diameter

    def dfs(self, node):
        """
        :param node: the current binary tree node for which we'll compute the diameter
        :return: the current node's diameter
        """
        # Time complexity <=> O(n * n), where n is the number of nodes in the binary tree
        # Space complexity <=> O(1) (O(n) for the recursion stack)

        # If the current node isn't empty:
        # Compute the left subtree's diameter by going as far down as possible in it
        # Compute the right subtree's diameter by going as far down as possible in it
        # If the sum between these 2 computed diameters is greater than the overall maximum diameter:
        # Change the maximum's value
        # The diameter of the current node will be the maximum between the 2 computed diameters + 1
        # Otherwise (the current node is empty), its diameter is 0
        if node is None:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        self.diameter = max(self.diameter, left + right)

        return max(left, right) + 1


# Example 1
root1 = TreeNode(1,
                 TreeNode(2,
                          TreeNode(4),
                          TreeNode(5)),
                 TreeNode(3))

print(Solution().diameter_of_binary_tree(root1))
print("-------------------------------------")

# Example 2
root1 = TreeNode(1, TreeNode(2), None)

print(Solution().diameter_of_binary_tree(root1))
print("-------------------------------------")

# Example 3
root1 = TreeNode(2,
                 TreeNode(3,
                          TreeNode(1),
                          None),
                 None)

print(Solution().diameter_of_binary_tree(root1))
