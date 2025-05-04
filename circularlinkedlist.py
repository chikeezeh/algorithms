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
        # add an element to the end of the circularll
        pass
    def append(self, data):
        # add a node to the beginning of the circularll
        pass
    def printlist(self, data):
        # print out the circularll in a nice manner
        pass
