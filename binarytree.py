class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    def pre_order_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += str(start.value) + "->"
            traversal = self.pre_order_print(start.left, traversal)
            traversal = self.pre_order_print(start.right, traversal)
        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)