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
