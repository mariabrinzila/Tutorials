class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        # Define a binary tree element (it has a value, a pointer to its left child
        # And a pointer to its right child)
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def is_symmetric(self, root):
        """
        :param root: the binary tree that may or may not be symmetric around its center (a mirror
            of itself)
        :return: True, if the binary tree is symmetric around its center and False, otherwise
        """
        # Data structure <=> Binary Tree
        # Algorithm <=> DFS (Preorder)

        # The DFS preorder traversal <=> root, left, right
        # If the root's left and right subtree are identical, the binary tree is symmetric around
        # Its center
        # 2 binary trees are identical, if we're able to traverse them simultaneously
        # Without any problems (their heights are identical, all their element's values are the same
        # And the tree's structure is the same)

        # Time complexity <=> O(n), where n is the maximum number of nodes in one of the 2 binary trees
        # Space complexity <=> O(1)

        # For the root's left and right subtrees, do a simultaneous traversal
        # And check if they're identical
        return self.simultaneous_traversal(root.left, root.right)

    def simultaneous_traversal(self, p, q):
        """
        :param p: the first binary tree to be traversed simultaneously with the second binary tree
        :param q: the second binary tree
        :return: True, if the 2 given binary trees are identical and False, otherwise
        """
        # If both binary trees are empty, they're identical
        # If only one of them is empty, they're not identical
        # If the value of the current node in the first binary tree isn't equal to the value in
        # The current node in the second binary tree, they're not identical
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return self.simultaneous_traversal(p.left, q.left) \
            and self.simultaneous_traversal(p.right, q.right)


# Example 1
r = TreeNode(1, TreeNode(2, TreeNode(3, None), TreeNode(4, None)),
             TreeNode(2, TreeNode(3, None), TreeNode(4, None)))

print(Solution().is_symmetric(r))
print("-------------------------------------")

# Example 2
r = TreeNode(1, TreeNode(2, None, TreeNode(3, None)),
             TreeNode(2, None, TreeNode(3, None)))

print(Solution().is_symmetric(r))
print("-------------------------------------")

# Example 3
r = TreeNode(1, TreeNode(2, TreeNode(3, None), None),
             TreeNode(2, None, TreeNode(3, None)))

print(Solution().is_symmetric(r))
print("-------------------------------------")
