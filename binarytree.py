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
    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.value) + "->"
            traversal = self.inorder_print(start.right, traversal)
        return traversal
    def post_order_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.pre_order_print(start.left, traversal)
            traversal = self.pre_order_print(start.right, traversal)
            traversal += str(start.value) + "->"
        return traversal
    


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

tree2 = BinaryTree("F")
tree2.root.left = Node("B")
tree2.root.right = Node("G")
tree2.root.left.left = Node("A")
tree2.root.left.right = Node("D")
tree2.root.left.right.left = Node("C")
tree2.root.left.right.right = Node("E")
tree2.root.right.right = Node("I")
tree2.root.right.right.left = Node("H")

print(tree2.pre_order_print(tree2.root, ""))
print(tree2.inorder_print(tree2.root, ""))
print(tree2.post_order_print(tree2.root, ""))