class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        # Define a binary tree element (it has a value, a pointer to its left child
        # And a pointer to its right child)
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        # Define an array of elements / values (the binary tree node's values)
        self.elements = []

        # Define an element representing the last element in the inorder traversal
        self.last_element = None

    def is_valid_BST(self, root):
        """
        :param root: the binary tree that may or may not be a binary search tree (for every node in a BST,
            its left subtree contains values that are smaller than it, its right subtree contains
            values that are greater than it and both the left and right subtrees must also be BSTs)
        :return: True, if the given binary tree is a BST (binary search tree) and False, otherwise
        """
        # Data structure <=> Binary Tree, Binary Search Tree
        # Algorithm <=> DFS (Inorder)

        # The DFS inorder traversal <=> left, root, right
        # For a BST, the inorder traversal produces a sorted result
        # So we can produce the inorder traversal, store it in an array
        # And check if the array is sorted or not

        # Time complexity <=> O(2 * n), where n is the total number of nodes in the binary tree
        # Space complexity <=> O(n)

        # Base case <=> the binary tree only has one node (the root)
        if root.left is None and root.right is None:
            return True

        # Compute the inorder traversal result
        self.inorder(root)

        # For each element in the inorder traversal result:
        # If the previous element of the current element's value is > the current element's value,
        # The binary tree isn't a BST (the array isn't sorted)
        n = len(self.elements)

        for i in range(n):
            if i != 0:
                if self.elements[i - 1] >= self.elements[i]:
                    return False

        return True

    def inorder(self, node):
        """
        :param node: the current node in the given binary tree to be traversed
        :return: void
        """
        # Time complexity <=> O(n), where n is the total number of nodes in the binary tree
        # Space complexity <=> O(n)

        # If the node isn't empty:
        # If the left subtree isn't empty, traverse it
        # Add the root to the array of elements
        # If the right subtree isn't empty, traverse it
        if node is not None:
            # Left
            if node.left is not None:
                self.inorder(node.left)

            # Root
            self.elements.append(node.val)

            # Right
            if node.right is not None:
                self.inorder(node.right)


# Example 1
root1 = TreeNode(2, TreeNode(1, None), TreeNode(3, None))

print(Solution().is_valid_BST(root1))
print("-------------------------------------")

# Example 2
root1 = TreeNode(5, TreeNode(1, None), TreeNode(4, TreeNode(3, None), TreeNode(6, None)))

print(Solution().is_valid_BST(root1))
print("-------------------------------------")

# Example 3
root1 = TreeNode(5, TreeNode(4, None), TreeNode(6, TreeNode(3, None), TreeNode(7, None)))

print(Solution().is_valid_BST(root1))
