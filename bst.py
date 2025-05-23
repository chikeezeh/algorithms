class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class Bst:
    def __init__(self, root) -> None:
        self.root = Node(root)
    
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False
    
    def preorder_print(self, start, traversal):
        """Root -> Left -> Right"""
        if start:
            traversal += (str(start.value) + ' ')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left -> Root -> Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + ' ')
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left -> Right -> Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + ' ')
        return traversal

# Example usage
tree = Bst(10)
tree.root.left = Node(5)
tree.root.right = Node(15)
tree.root.left.left = Node(2)
tree.root.left.right = Node(5)
tree.root.left.left.left = Node(1)
tree.root.right.left = Node(13)
tree.root.right.right = Node(22)
tree.root.right.left.right = Node(14)
print("Inorder traversal: " + tree.print_tree("inorder"))
print("Preorder traversal: " + tree.print_tree("preorder"))
print("Postorder traversal: " + tree.print_tree("postorder"))