import binary_tree_nodes as btn
import binary_trees as bt
import binary_search_trees as bst

# Binary tree
# Creation
binary_tree = bt.BinaryTree()

# Interactive creation
# binary_tree.root = binary_tree.interactive_creation()

# Normal creation
""" binary_tree.root = btn.BinaryTreeNode('A')
binary_tree.root.left = btn.BinaryTreeNode('B')
binary_tree.root.right = btn.BinaryTreeNode('C')

binary_tree.root.left.left = btn.BinaryTreeNode('D')
binary_tree.root.right.left = btn.BinaryTreeNode('E')
binary_tree.root.right.right = btn.BinaryTreeNode('F')

binary_tree.root.right.left.left = btn.BinaryTreeNode('G') """

binary_tree.root = btn.BinaryTreeNode(1)
binary_tree.root.left = btn.BinaryTreeNode(2)
binary_tree.root.right = btn.BinaryTreeNode(3)

binary_tree.root.left.left = btn.BinaryTreeNode(4)
binary_tree.root.left.right = btn.BinaryTreeNode(5)
binary_tree.root.right.left = btn.BinaryTreeNode(6)
binary_tree.root.right.right = btn.BinaryTreeNode(7)

binary_tree.root.left.left.left = btn.BinaryTreeNode(8)
binary_tree.root.left.left.right = btn.BinaryTreeNode(9)
binary_tree.root.left.right.left = btn.BinaryTreeNode(10)
binary_tree.root.left.right.right = btn.BinaryTreeNode(11)
binary_tree.root.right.left.right = btn.BinaryTreeNode(13)
binary_tree.root.right.right.left = btn.BinaryTreeNode(14)

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

# Height
height = binary_tree.height(binary_tree.root)

print("The binary tree's height is " + str(height))
print("---------------------------------------")

# Search
result = binary_tree.search(4)

if not result:
    print("The node with the data 4 doesn't exist in the binary tree")
else:
    print("The node with the data 4 exists in the binary tree")

result = binary_tree.search(20)

if not result:
    print("The node with the data 20 doesn't exist in the binary tree")
else:
    print("The node with the data 20 exists in the binary tree")

print("---------------------------------------")

# Insertion
binary_tree.insertion(15)
binary_tree.traversal = []
binary_tree.bfs_traversal()

print("Inserted the node with the data 15 successfully: " + str(binary_tree.traversal))

binary_tree.insertion(16)
binary_tree.traversal = []
binary_tree.bfs_traversal()
print("Inserted the node with the data 16 successfully: " + str(binary_tree.traversal))

binary_tree.insertion(17)
binary_tree.traversal = []
binary_tree.bfs_traversal()
print("Inserted the node with the data 17 successfully: " + str(binary_tree.traversal))
print("---------------------------------------")

# Deletion
result = binary_tree.deletion(3)

if not result:
    print("There is no node with the data 3 in the binary tree")
else:
    binary_tree.traversal = []
    binary_tree.bfs_traversal()

    print("Deleted the node with the data 3 successfully: " + str(binary_tree.traversal))

result = binary_tree.deletion(16)

if not result:
    print("There is no node with the data 16 in the binary tree")
else:
    binary_tree.traversal = []
    binary_tree.bfs_traversal()

    print("Deleted the node with the data 16 successfully: " + str(binary_tree.traversal))

result = binary_tree.deletion(1)

if not result:
    print("There is no node with the data 1 in the binary tree")
else:
    binary_tree.traversal = []
    binary_tree.bfs_traversal()

    print("Deleted the node with the data 1 successfully: " + str(binary_tree.traversal))

result = binary_tree.deletion(31)

if not result:
    print("There is no node with the data 31 in the binary tree")
else:
    binary_tree.traversal = []
    binary_tree.bfs_traversal()

    print("Deleted the node with the data 31 successfully: " + str(binary_tree.traversal))

print("                                       ")
print("***************************************")
print("                                       ")

# Binary search tree
# Creation
binary_search_tree = bst.BinarySearchTree()

binary_search_tree.root = btn.BinaryTreeNode(8)
binary_search_tree.root.left = btn.BinaryTreeNode(3)
binary_search_tree.root.right = btn.BinaryTreeNode(10)

binary_search_tree.root.left.left = btn.BinaryTreeNode(1)
binary_search_tree.root.left.right = btn.BinaryTreeNode(6)
binary_search_tree.root.right.right = btn.BinaryTreeNode(14)

binary_search_tree.root.left.right.left = btn.BinaryTreeNode(4)
binary_search_tree.root.left.right.right = btn.BinaryTreeNode(7)
binary_search_tree.root.right.right.left = btn.BinaryTreeNode(13)

# Traversals
binary_search_tree.inorder_traversal(binary_search_tree.root)

print("Inorder traversal result is: " + str(binary_search_tree.traversal))

binary_search_tree.traversal = []
binary_search_tree.preorder_traversal(binary_search_tree.root)

print("Preorder traversal result is: " + str(binary_search_tree.traversal))

binary_search_tree.traversal = []
binary_search_tree.postorder_traversal(binary_search_tree.root)

print("Postorder traversal result is: " + str(binary_search_tree.traversal))

binary_search_tree.traversal = []
binary_search_tree.bfs_traversal()

print("BFS traversal result is: " + str(binary_search_tree.traversal))
print("---------------------------------------")

# Search
result = binary_search_tree.search(6, binary_search_tree.root)

if not result:
    print("There is no node with the data 6 in the binary search tree")
else:
    print("There is a node with the data " + str(result.data) + " in the binary tree")

result = binary_search_tree.search(56, binary_search_tree.root)

if not result:
    print("There is no node with the data 56 in the binary search tree")
else:
    print("There is a node with the data " + str(result.data) + " in the binary tree")

print("---------------------------------------")
