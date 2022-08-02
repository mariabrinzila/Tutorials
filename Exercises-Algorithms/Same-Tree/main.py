class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree_recursive(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    check_simple_nodes(p, q)

    return is_same_tree_recursive(p.right, q.right) and is_same_tree_recursive(p.left, q.left)


def check_simple_nodes(p, q):
    # p and q are both None
    if p is None and q is None:
        return True

    # either p is None or q is None
    if p is None or q is None:
        return False

    if p.val != q.val:
        return False


p1 = TreeNode(1, TreeNode(2, None))
q1 = TreeNode(1, None, TreeNode(2, None))
print(is_same_tree_recursive(p1, q1))
