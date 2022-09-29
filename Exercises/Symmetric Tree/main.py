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
        # Algorithm <=> DFS

        # We need to simultaneously traverse both subtrees of the root to check the symmetry <=> DFS

        # Time complexity <=> O(n - 1), where n is the number of nodes in the binary tree
        # Space complexity <=> O(1)

        # Base case <=> we have maximum 3 nodes in the binary tree
        if root.left is None and root.right is None:
            return True
        elif (root.left is None and root.right is not None) \
                or (root.left is not None and root.right is None):
            return False
        elif root.left is not None and root.right is not None \
                and root.left.left is None and root.left.right is None \
                and root.right.left is None and root.right.right is None:
            if root.left.val == root.right.val:
                return True
            else:
                return False

        return self.symmetric_subtrees(root.left, root.right)

    def symmetric_subtrees(self, l, r):
        """
        :param l: the current left subtree of the given binary tree
        :param r: the current right subtree of the given binary tree
        :return: True, if the left and right subtrees are symmetrical (mirrored) and False, otherwise
        """
        # If the subtrees' root's values don't correspond, they're not symmetrical
        # If both subtrees have no children, they're symmetrical
        # If one subtree has at least one child and they other one is empty, they're not symmetrical
        # If both subtrees have one child:
        # If the child is on opposing sides (one is on the left and the other on the right or vice-versa):
        # Keep exploring if they're symmetrical from that child for both subtrees
        # Otherwise, they're not symmetrical
        # If one subtree has one child and the other has 2, they're not symmetrical
        # If both subtrees have 2 children:
        # If their values are opposed (the value of the first subtree's left child corresponds
        # To the value of the second subtree's right child and vice-versa):
        # Keep exploring if they're symmetrical from both children for both subtrees,
        # So keep exploring the corresponding pair (left - right and right - left)
        if l.val != r.val:
            return False

        if l.left is None and l.right is None and r.left is None and r.right is None:
            return True

        if (l.left is not None or l.right is not None) and r.left is None and r.right is None \
                or (r.left is not None or r.right is not None) and l.left is None and l.right is None:
            return False

        if l.left is None and r.left is None:
            return False
        elif l.left is None and r.right is None:
            if l.right.val == r.left.val:
                return self.symmetric_subtrees(l.right, r.left)
            else:
                return False

        if l.right is None and r.right is None:
            return False
        elif l.right is None and r.left is None:
            if l.left.val == r.right.val:
                return self.symmetric_subtrees(l.left, r.right)
            else:
                return False

        if (l.left is not None and l.right is not None
            and (r.left is not None and r.right is None or r.left is None and r.right is not None)) \
                or (r.left is not None and r.right is not None
                    and (l.left is not None and l.right is None or l.left is None and l.right is not None)):
            return False

        if l.left.val == r.right.val and l.right.val == r.left.val \
                or (l.left.val == r.right.val == l.right.val == r.left.val):
            return self.symmetric_subtrees(l.left, r.right) and self.symmetric_subtrees(l.right, r.left)
        else:
            return False


# Example 1
root1 = TreeNode(1, TreeNode(2, TreeNode(3, None), TreeNode(4, None)),
                 TreeNode(2, TreeNode(4, None), TreeNode(3, None)))

print(Solution().is_symmetric(root1))
print("-------------------------------------")

# Example 2
root1 = TreeNode(1, TreeNode(2, None, TreeNode(3, None)),
                 TreeNode(2, None, TreeNode(3, None)))

print(Solution().is_symmetric(root1))
print("-------------------------------------")

# Example 3
root1 = TreeNode(1, TreeNode(2, TreeNode(3, None), None),
                 TreeNode(2, None, TreeNode(3, None)))

print(Solution().is_symmetric(root1))
print("-------------------------------------")

# Example 4
root1 = TreeNode(0,
                 TreeNode(-37,
                          TreeNode(80,
                                   TreeNode(-93,
                                            TreeNode(32, TreeNode(-99), TreeNode(89)),
                                            TreeNode(43, None, TreeNode(-96))),
                                   TreeNode(9,
                                            TreeNode(-8, None, TreeNode(-45)),
                                            TreeNode(-50, TreeNode(57), None))),
                          TreeNode(-71,
                                   TreeNode(26,
                                            TreeNode(76, TreeNode(-87), None),
                                            TreeNode(76, TreeNode(-90), None)),
                                   None)),
                 TreeNode(-37,
                          TreeNode(-71,
                                   None,
                                   TreeNode(26,
                                            TreeNode(76, None, TreeNode(-90)),
                                            TreeNode(76, None, TreeNode(-87)))),
                          TreeNode(80,
                                   TreeNode(9,
                                            TreeNode(-50, None, TreeNode(57)),
                                            TreeNode(-8, TreeNode(-45), None)),
                                   TreeNode(-93,
                                            TreeNode(43, TreeNode(-96), None),
                                            TreeNode(32, TreeNode(89), TreeNode(-99))))))

print(Solution().is_symmetric(root1))
print("-------------------------------------")
