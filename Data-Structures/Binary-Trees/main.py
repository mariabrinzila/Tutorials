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

    def creation(self):
        data = int(input("Introduce the node's data: "))
        current = TreeNode(data)

        user_input = input("Does the node have a left child? (Y/N) ")

        if user_input == 'Y':
            current.left = self.creation()

        user_input = input("Does the node have a right child? (Y/N) ")

        if user_input == 'Y':
            current.right = self.creation()

        return current

    # To do: traversals implementations


# Creation
binary_tree = BinaryTree()
binary_tree.root = binary_tree.creation()
