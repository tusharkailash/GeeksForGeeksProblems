###To check if the binary tree is a BST

INT_MAX = 4294967296
INT_MIN = -4294967296



class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Returns true if the given tree is a binary search tree

def isBST(node):
    return (isBSTUtil(node, INT_MIN, INT_MAX))


# Retusn true if the given tree is a BST and its values
# >= min and <= max
def isBSTUtil(node, min, max):
    # An empty tree is BST
    if node is None:
        return True

    # False if this node violates min/max constraint
    if node.val <= min or node.val >= max:
        return False

    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.left, min, node.val) and
            isBSTUtil(node.right, node.val, max))



root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if (isBST(root)):
    print "Binary Tree Is BST"
else:
    print "Binary Tree is not a BST"