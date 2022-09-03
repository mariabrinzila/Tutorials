import binary_tree_nodes as btn


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
        current = btn.BinaryTreeNode(data)
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
        # While the queue isn't empty (there are still nodes to traverse):
        # Pop the first node in the queue and put it in the traversal array
        # Put its children in the queue, if they aren't None
        # If both children are None, put the node in the leafs array
        queue = [self.root]

        while queue:
            current = queue.pop(0)
            self.traversal.append(current.data)

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

            if current.left is None and current.right is None:
                self.leafs.append(current.data)

    def height(self, node):
        """
        :param node: the current node whose height we're going to compute
        :return: the node's height
        """
        if node is None:
            # We can't go any further down (we got bellow a leaf)
            return -1

        # Go in the left subtree as far as possible
        left = self.height(node.left)

        # Go in the right subtree as far as possible
        right = self.height(node.right)

        # The node's height is the largest number of edges on a path from it to a leaf
        return max(left, right) + 1

    def search(self, node_data):
        """
        :param node_data: the node data that we're searching for in the binary tree
        :return: False, if there is no node with that data in the binary and
            the node, otherwise
        """
        if self.root.data == node_data:
            return self.root

        # While the queue isn't empty (there are still nodes to traverse):
        # Pop the first node in the queue
        # If its left child is the node we're looking for, return the current node
        # Otherwise put it in the queue (if it's not None)
        # If its right child is the node we're looking for, return the current node
        # Otherwise put it in the queue (if it's not None)
        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.left is not None and current.left.data == node_data:
                return current.left
            elif current.left is not None:
                queue.append(current.left)

            if current.right is not None and current.right.data == node_data:
                return current.right
            elif current.right is not None:
                queue.append(current.right)

        return False

    def insertion(self, node_data):
        """
        :param node_data: the node data that we want to insert in the binary tree
        :return: the inserted node
        """
        if self.root is None:
            self.root = btn.BinaryTreeNode(node_data)
            return self.root

        # While the queue isn't empty (there are still nodes to traverse):
        # Pop the first node in the queue
        # If its left child is empty, create a new node with the given node data
        # Otherwise put it in the queue
        # If its right child is empty, create a new node with the given node data
        # Otherwise put it in the queue
        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.left is None:
                new_node = btn.BinaryTreeNode(node_data)
                current.left = new_node
                return new_node
            else:
                queue.append(current.left)

            if current.right is None:
                new_node = btn.BinaryTreeNode(node_data)
                current.right = new_node
                return new_node
            else:
                queue.append(current.right)

    def deletion(self, node_data):
        """
        :param node_data: the node data that we want to delete from the binary tree
        :return: False, if there is no node in the binary tree with the given data and True,
            if there is one and was deleted
        """
        # Search for the node with the given data
        node_to_be_deleted = self.search(node_data)

        if not node_to_be_deleted:
            return False

        # Compute the deepest and rightmost node in the binary tree
        queue = [self.root]
        deepest_node = None

        while queue:
            current = queue.pop(0)

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

            if current.left is None and current.right is None:
                deepest_node = current

        # Replace the deepest and rightmost node’s data with the one from the node to be deleted
        node_to_be_deleted.data = deepest_node.data

        # Delete the deepest and rightmost node
        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.left is not None and current.left == deepest_node:
                current.left = None
                break
            elif current.left is not None:
                queue.append(current.left)

            if current.right is not None and current.right == deepest_node:
                current.right = None
                break
            elif current.right is not None:
                queue.append(current.right)

        return True
