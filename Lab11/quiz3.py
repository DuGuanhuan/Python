class TreeNode:
    """
    Representing a tree node consisting of
    - datum: the datum stored at the node
    - left: reference to the left child node
    - right: reference to the right child node
    """

    def __init__(self, datum, left=None, right=None):
        self.datum = datum
        self.left = left
        self.right = right


class MyBinaryTree:
    """
    Implementation of a binary tree
    """

    def __init__(self):
        """
        Constructs an empty tree
        """
        self.root = None

    def print_in_order(self):
        """
        Use in-order traversal and print each tree node's datum
        """
        self._in_order_traversal(self.root)

    def _in_order_traversal(self, node):
        if node:
            self._in_order_traversal(node.left)
            print(node.datum, end=" ")
            self._in_order_traversal(node.right)

    def print_pre_order(self):
        """
        Use pre-order traversal and print each tree node's datum
        """
        self._pre_order_traversal(self.root)

    def _pre_order_traversal(self, node):
        if node:
            print(node.datum, end=" ")
            self._pre_order_traversal(node.left)
            self._pre_order_traversal(node.right)

    def print_post_order(self):
        """
        Use post-order traversal and print each tree node's datum
        """
        self._post_order_traversal(self.root)

    def _post_order_traversal(self, node):
        if node:
            self._post_order_traversal(node.left)
            self._post_order_traversal(node.right)
            print(node.datum, end=" ")


nodeA = TreeNode(1)
nodeB = TreeNode(2)
nodeC = TreeNode(3)
nodeD = TreeNode(4)
nodeE = TreeNode(5)
nodeF = TreeNode(6)
nodeH = TreeNode(7)
nodeI = TreeNode(8)
nodeJ = TreeNode(9)
nodeK = TreeNode(10)
nodeL = TreeNode(11)
nodeM = TreeNode(12)

nodeA.left = nodeB
nodeA.right = nodeC
nodeB.left = nodeE
nodeB.right = nodeE
nodeE.left = nodeI
nodeE.right = nodeJ
nodeC.left = nodeF
nodeF.left = nodeK
nodeF.right = nodeL
nodeH.left = nodeM

binary_tree = MyBinaryTree()
binary_tree.root = nodeA

print("In-order traversal:")
binary_tree.print_in_order()
