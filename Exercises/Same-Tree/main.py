class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        # Define a binary tree element (it has a value, a pointer to its left child
        # And a pointer to its right child)
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def is_same_tree(self, p, q):
        """
        :param p: a binary tree that may or may not be identical to the second binary tree
        :param q: the second binary tree
        :return: True, if the 2 given binary trees are identical and False, otherwise
        """
        # Data structure <=> Binary Tree
        # Algorithm <=> DFS (Preorder)

        # The DFS preorder traversal <=> root, left, right
        # If the 2 binary trees are identical, we'll be able to traverse them simultaneously
        # Without any problems (their heights are identical, all their element's values are the same
        # And the tree's structure is the same)

        # Time complexity <=> O(n), where n is the maximum number of nodes in one of the 2 binary trees
        # Space complexity <=> O(1)

        # Base case <=> 0 or 1 elements in both binary trees
        if p is None and q is None:
            return True
        elif (p is None and q is not None) or (q is None and p is not None):
            return False
        elif p is not None and q is not None and p.left is None and p.right is None and q.left is None \
                and q.right is None and p.val != q.val:
            return False
        elif p is not None and q is not None and p.left is None and p.right is None and q.left is None \
                and q.right is None and p.val == q.val:
            return True

        return self.preorder(p, q)

    def preorder(self, node_p, node_q):
        """
        :param node_p: the current node in the first given binary tree to be traversed
        :param node_q: the current node in the second given binary tree to be traversed
        :return: True, if the 2 given binary trees are identical and False, otherwise
        """
        # Time complexity <=> O(n), where n is the maximum number of nodes in one of the 2 binary trees
        # Space complexity <=> O(1)

        # If the current node in the first binary tree is empty and the one in the second binary tree isn't
        # Or vice-versa, the 2 given binary trees are not identical
        # Otherwise, if the value of the current node in the first binary tree isn't equal to
        # The value of the current node in the second binary tree, the 2 given binary trees are not identical
        # Otherwise, if the left subtree of the current node in the first binary tree is empty and
        # The left subtree of the current node in the second binary tree isn't empty
        # Or vice-versa, the 2 given binary trees are not identical
        # Otherwise, if the right subtree of the current node in the first binary tree is empty and
        # The right subtree of the current node in the second binary tree isn't empty
        # Or vice-versa, the 2 given binary trees are not identical
        # Otherwise, go in the left and right subtrees and keep traversing
        if node_p is None and node_q is None:
            return True
        elif (node_p is None and node_q is not None) or (node_q is None and node_p is not None):
            return False
        elif node_p is not None and node_q is not None:
            # Root
            if node_q.val != node_p.val:
                return False

            # Left
            if (node_p.left is None and node_q.left is not None) \
                    or (node_q.left is None and node_p.left is not None):
                return False

            # Right
            if (node_p.right is None and node_q.right is not None) \
                    or (node_q.right is None and node_p.right is not None):
                return False

            # Keep traversing the subtrees
            if (node_p.left is not None and node_q.left is not None) and \
                    (node_p.right is not None and node_q.right is not None):
                return self.preorder(node_p.left, node_q.left) and self.preorder(node_p.right, node_q.right)
            elif (node_p.left is not None and node_q.left is not None) and \
                    (node_p.right is None and node_q.right is None):
                return self.preorder(node_p.left, node_q.left)
            else:
                return self.preorder(node_p.right, node_q.right)

    def easier_is_same_tree(self, p, q):
        """
        :param p: a binary tree that may or may not be identical to the second binary tree
        :param q: the second binary tree
        :return: True, if the 2 given binary trees are identical and False, otherwise
        """
        # If both current nodes are None, the 2 given binary trees are identical
        # If only one of the current nodes is None, the 2 given binary trees aren't identical
        # If the values of the current nodes aren't identical, the 2 given binary trees aren't identical
        # Keep traversing the left and right subtrees
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return self.easier_is_same_tree(p.left, q.left) and self.easier_is_same_tree(p.right, q.right)


# Example 1
p1 = TreeNode(1, TreeNode(2, None), TreeNode(3, None))
q1 = TreeNode(1, TreeNode(2, None), TreeNode(3, None))

print(Solution().is_same_tree(p1, q1))
print(Solution().easier_is_same_tree(p1, q1))
print("-------------------------------------")

# Example 2
p1 = TreeNode(1, TreeNode(2, None), None)
q1 = TreeNode(1, None, TreeNode(3, None))

print(Solution().is_same_tree(p1, q1))
print(Solution().easier_is_same_tree(p1, q1))
print("-------------------------------------")

# Example 3
p1 = TreeNode(1, TreeNode(2, None), TreeNode(1, None))
q1 = TreeNode(1, TreeNode(1, None), TreeNode(2, None))

print(Solution().is_same_tree(p1, q1))
print(Solution().easier_is_same_tree(p1, q1))
print("-------------------------------------")

# Example 4
p1 = TreeNode(1, TreeNode(2, None), TreeNode(3, TreeNode(4, None), TreeNode(5, None)))
q1 = TreeNode(1, TreeNode(2, None), TreeNode(3, None))

print(Solution().is_same_tree(p1, q1))
print(Solution().easier_is_same_tree(p1, q1))
