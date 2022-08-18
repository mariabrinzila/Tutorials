import binary_tree_nodes as btn
import binary_trees as bt


class BinarySearchTree (bt.BinaryTree):
    def __init__(self):
        # Binary search trees inherit all the functionalities of a binary tree
        # With a few modifications
        super().__init__()

    def search(self, node_data, root_node):
        """
        :param node_data: the node data that we're searching for in the binary search tree
        :param root_node: the current root node
        :return: the node, if there is a node with the given node data in the binary search tree
            and False, otherwise
        """
        # The root is None, so we've reached the end of the possible path, and we haven't found the node
        if root_node is None:
            return False

        # The root's data is equal to the given node data, so the node has been found
        if node_data == root_node.data:
            return root_node

        # If the root's data is < the given data, we need to explore the left subtree
        if node_data < root_node.data:
            return self.search(node_data, root_node.left)

        # If the root's data is > the given data, we need to explore the right subtree
        return self.search(node_data, root_node.right)

    def insertion(self, node_data, root_node):
        """
        :param node_data: the node data that we want to insert in the binary search tree
        :param root_node: the current root node
        :return: the inserted node
        """
        if root_node is None:
            # We've reached the end of the tree
            return btn.BinaryTreeNode(node_data)
        elif root_node.data == node_data:
            # There already is a none with the given key
            print(node_data)
            return root_node
        elif root_node.data > node_data:
            # We need to go in the left subtree (root > given key)
            root_node.left = self.insertion(node_data, root_node.left)
        else:
            # We need to go in the right subtree (root < given key)
            root_node.right = self.insertion(node_data, root_node.right)

        return root_node

    def deletion(self, node_data):
        """
        :param node_data: the node data that we want to delete from the binary search tree
        :return: False, if there is no node in the binary tree with the given data and True,
            if there is one and was deleted
        """
        # Search the binary search tree for the given key
        result = self.search(node_data, self.root)

        if not result:
            # There is no node with the given key in the tree
            return False

        if result.left is None and result.right is None:
            # The node is a leaf
            # Delete the leaf from the binary search tree
            previous = self.compute_previous(node_data, self.root)

            if not previous:
                return False
            else:
                if previous.left.data == node_data:
                    previous.left = None
                elif previous.right.data == node_data:
                    previous.right = None
        elif result.left is not None and result.right is None:
            # The node only has the left child
            # The left child's data becomes the node's data
            # Delete the left child
            result.data = result.left.data
            result.left = result.left.left
            result.right = result.left.right
        elif result.right is not None and result.left is None:
            # The node only has the right child
            # The right child's data becomes the node's data
            # Delete the right child
            result.data = result.right.data
            result.left = result.right.left
            result.right = result.right.right
        else:
            # The node has 2 children
            self.traversal = []
            self.inorder_traversal(self.root)

            # Find the node's successor in the inorder traversal
            index = self.traversal.index(result.data)
            successor = self.traversal[index + 1]

            successor_node = self.search(successor, self.root)

            if not successor_node:
                return False
            else:
                # The successor's data becomes the node's data
                # Delete the successor
                data = successor_node.data
                previous = self.compute_previous(successor_node.data, self.root)

                if not previous:
                    return False
                else:
                    if previous.left is not None and previous.left.data == successor_node.data:
                        previous.left = successor_node.left
                    elif previous.right is not None and previous.right.data == successor_node.data:
                        previous.right = successor_node.right

                result.data = data

        return True

    def compute_previous(self, node_data, root_node):
        """
        :param node_data: the data of the node we want to compute the predecessor of in the
            binary search tree
        :param root_node: the current root node
        :return: False, if the predecessor can't be computed and the predecessor node, otherwise
        """
        # The root is None, so we've reached the end of the possible path, and we haven't found the node
        if root_node is None:
            return False

        # The root's left child's data is equal to the given node data, so the node has been found
        if root_node.left is not None and node_data == root_node.left.data:
            return root_node

        # The root's right child's data is equal to the given node data, so the node has been found
        if root_node.right is not None and node_data == root_node.right.data:
            return root_node

        # If the root's data is < the given data, we need to explore the left subtree
        if node_data < root_node.data:
            return self.compute_previous(node_data, root_node.left)

        # If the root's data is > the given data, we need to explore the right subtree
        return self.compute_previous(node_data, root_node.right)
