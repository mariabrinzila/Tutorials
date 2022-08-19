import binary_tree_nodes as btn
import min_heaps as minh
import max_heaps as maxh

# Complete binary tree 1
root = btn.BinaryTreeNode(1)
root.left = btn.BinaryTreeNode(3)
root.right = btn.BinaryTreeNode(6)

root.left.left = btn.BinaryTreeNode(5)
root.left.right = btn.BinaryTreeNode(9)
root.right.left = btn.BinaryTreeNode(8)

# Complete binary tree 2
root1 = btn.BinaryTreeNode(1)
root1.left = btn.BinaryTreeNode(3)
root1.right = btn.BinaryTreeNode(6)

root1.left.left = btn.BinaryTreeNode(2)
root1.left.right = btn.BinaryTreeNode(9)
root1.right.left = btn.BinaryTreeNode(8)

# Complete binary tree 3
root2 = btn.BinaryTreeNode(100)
root2.left = btn.BinaryTreeNode(40)
root2.right = btn.BinaryTreeNode(50)

root2.left.left = btn.BinaryTreeNode(10)
root2.left.right = btn.BinaryTreeNode(15)
root2.right.left = btn.BinaryTreeNode(50)
root2.right.right = btn.BinaryTreeNode(40)

""" root2 = btn.BinaryTreeNode(100)
root2.left = btn.BinaryTreeNode(90)
root2.right = btn.BinaryTreeNode(80)

root2.left.left = btn.BinaryTreeNode(70)
root2.left.right = btn.BinaryTreeNode(80)
root2.right.left = btn.BinaryTreeNode(30)
root2.right.right = btn.BinaryTreeNode(20)

root2.left.left.left = btn.BinaryTreeNode(50)
root2.left.left.right = btn.BinaryTreeNode(40)
root2.left.right.left = btn.BinaryTreeNode(30)
root2.left.right.right = btn.BinaryTreeNode(10)
root2.right.left.left = btn.BinaryTreeNode(11)
root2.right.left.right = btn.BinaryTreeNode(12)
root2.right.right.left = btn.BinaryTreeNode(18)
root2.right.right.right = btn.BinaryTreeNode(9) """

# Complete binary tree 4
root3 = btn.BinaryTreeNode(100)
root3.left = btn.BinaryTreeNode(40)
root3.right = btn.BinaryTreeNode(50)

root3.left.left = btn.BinaryTreeNode(45)
root3.left.right = btn.BinaryTreeNode(15)
root3.right.left = btn.BinaryTreeNode(50)
root3.right.right = btn.BinaryTreeNode(40)

# Min-Heap
# Creation
min_heap = minh.MinHeap()
result = min_heap.creation(root1)

if not result:
    print("Can't create a Min-Heap from the given complete binary tree since there is "
          "at least one node with a key < its parent")
else:
    print("The Min-Heap created is: " + str(min_heap.heap))

min_heap.heap = []
result = min_heap.creation(root)

if not result:
    print("Can't create a Min-Heap from the given complete binary tree since there is "
          "at least one node with a key < its parent")
else:
    print("The Min-Heap created is: " + str(min_heap.heap))

print("---------------------------------------")

# Get minimum
print("The smallest element in the heap is: " + str(min_heap.get_minimum()))
print("---------------------------------------")

# Remove minimum
result = min_heap.remove_minim()

print("The smallest element in the Min-Heap was " + str(result) +
      ". After its removal, the heap is: " + str(min_heap.heap))
print("---------------------------------------")

print("                                       ")
print("***************************************")
print("                                       ")

# Max-Heap
# Creation
max_heap = maxh.MaxHeap()
result = max_heap.creation(root3)

if not result:
    print("Can't create a Max-Heap from the given complete binary tree since there is "
          "at least one node with a key > its parent")
else:
    print("The Max-Heap created is: " + str(max_heap.heap))

max_heap.heap = []
result = max_heap.creation(root2)

if not result:
    print("Can't create a Max-Heap from the given complete binary tree since there is "
          "at least one node with a key > its parent")
else:
    print("The Max-Heap created is: " + str(max_heap.heap))

print("---------------------------------------")

# Get maximum
print("The greatest element in the heap is: " + str(max_heap.get_maximum()))
print("---------------------------------------")

# Remove maximum
result = max_heap.remove_maximum()

print("The greatest element in the Max-Heap was " + str(result) +
      ". After its removal, the heap is: " + str(max_heap.heap))
print("---------------------------------------")
