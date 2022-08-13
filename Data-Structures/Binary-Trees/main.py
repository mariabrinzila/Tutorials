class TreeNode:
    def __init__(self, data):
        # The node's data
        self.data = data

        # The node's references to the left and right child
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = None

        # The array storing the current traversal result
        self.traversal = []

        # The array containing the binary tree's leafs
        self.leafs = []

    def interactive_creation(self):
        """
        :return: the binary tree created by interacting with the user
        """
        # Get the node's data
        data = int(input("Introduce the node's data: "))
        current = TreeNode(data)

        user_input = input("Does the node have a left child? (Y/N) ")

        if user_input == 'Y':
            # Continue with the left subtree
            current.left = self.interactive_creation()

        user_input = input("Does the node have a right child? (Y/N) ")

        if user_input == 'Y':
            # Continue with the right subtree
            current.right = self.interactive_creation()

        return current 

    def inorder_traversal(self, node):
        """
        :param node: the current node that we're exploring
        :return: void
        """
        # Left
        if node.left is not None:
            self.inorder_traversal(node.left)

        # Root
        self.traversal.append(node.data)

        # Right
        if node.right is not None:
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        """
        :param node: the current node that we're exploring
        :return: void
        """
        # Root
        self.traversal.append(node.data)

        # Left
        if node.left is not None:
            self.preorder_traversal(node.left)

        # Right
        if node.right is not None:
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        """
        :param node: the current node that we're exploring
        :return: void
        """
        # Left
        if node.left is not None:
            self.postorder_traversal(node.left)

        # Right
        if node.right is not None:
            self.postorder_traversal(node.right)

        # Root
        self.traversal.append(node.data)

    def bfs_traversal(self):
        """
        :return: void
        """
        queue = [self.root]

        # While the queue isn't empty (there are still nodes to traverse):
        # Pop the first node in the queue and put it in the traversal array
        # Put its children in the queue, if they aren't None
        # If both children are None, put the node in the leafs array
        while queue:
            current = queue.pop(0)
            self.traversal.append(current.data)

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

            if current.left is None and current.right is None:
                self.leafs.append(current.data)


# Creation
binary_tree = BinaryTree()
# binary_tree.root = binary_tree.interactive_creation()

"""binary_tree.root = TreeNode(1)
binary_tree.root.left = TreeNode(2)
binary_tree.root.right = TreeNode(3)

binary_tree.root.left.left = TreeNode(4)
binary_tree.root.left.right = TreeNode(5)"""

binary_tree.root = TreeNode(1)
binary_tree.root.left = TreeNode(2)
binary_tree.root.right = TreeNode(3)

binary_tree.root.left.left = TreeNode(4)
binary_tree.root.left.right = TreeNode(5)
binary_tree.root.right.left = TreeNode(6)
binary_tree.root.right.right = TreeNode(7)

binary_tree.root.left.left.left = TreeNode(8)
binary_tree.root.left.left.right = TreeNode(9)
binary_tree.root.left.right.left = TreeNode(10)
binary_tree.root.left.right.right = TreeNode(11)
binary_tree.root.right.left.right = TreeNode(13)
binary_tree.root.right.right.left = TreeNode(14)

# Inorder traversal
binary_tree.inorder_traversal(binary_tree.root)

print("Inorder traversal result is: " + str(binary_tree.traversal))
print("---------------------------------------")

# Preorder traversal
binary_tree.traversal = []
binary_tree.preorder_traversal(binary_tree.root)

print("Preorder traversal result is: " + str(binary_tree.traversal))
print("---------------------------------------")

# Postorder traversal
binary_tree.traversal = []
binary_tree.postorder_traversal(binary_tree.root)

print("Postorder traversal result is: " + str(binary_tree.traversal))
print("---------------------------------------")

# BFS traversal
binary_tree.traversal = []
binary_tree.bfs_traversal()

print("BFS traversal result is: " + str(binary_tree.traversal))
print("---------------------------------------")

# Number of leafs
print("There are " + str(len(binary_tree.leafs)) +
      " leafs in the tree and they are: " + str(binary_tree.leafs))
print("---------------------------------------")
