"""
A circular linked list is a version of singlely linked list where the next of the tail
Node points to the head node.
A --> B --> C --> D --> A
A is the head node
D is the tail node.

"""
class Node:
    """
    A simple node class with two attributes, data and next
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLL:
    """
    Creates a simplle CircularLL with a head Node of None,
    This will have different methods for adding elements(Nodes)  to the CircularLL
    """
    def __init__(self):
        self.head = None
    def prepend(self, data):
        # add an element to the beginning of the circularll
        # if the cll is empty
        if not self.head:
            new_node = Node(data)
            self.head = new_node
            self.head.next = self.head
    def append(self, data):
        # add a node to the end of the circularll
        # if the cll is empty
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        cur_node = self.head
        while cur_node:
            if cur_node.next == self.head:
                cur_node.next = new_node
                new_node.next = self.head
                break
            cur_node = cur_node.next
    def printlist(self):
        # print out the circularll in a nice manner
        # loop till we get to the end, print every data.
        if not self.head:
            print("Empty Cll")
            return
        cur_node = self.head
        result = []
        while cur_node:
            result.append(str(cur_node.data))
            cur_node = cur_node.next
            if cur_node == self.head:
                break
        print(" --> ".join(result) + " --> (head)")


# test code
cll1 = CircularLL()
cll1.printlist()
cll1.append(1)
cll1.append(2)
cll1.append(4)
cll1.append(4)
cll1.printlist()