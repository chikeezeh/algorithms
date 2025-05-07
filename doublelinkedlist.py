"""
Implementation of a double linked list
Every Node points to the node before and after it.
head.prev = null
tail.next = null
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

