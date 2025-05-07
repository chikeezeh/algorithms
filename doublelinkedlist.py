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

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        # add a node to the end of a dll
        pass

    def prepend(self,data):
        # add a node to the beginning of a dll
        pass

    def print_list(self):
        # print the nodes of a dll
        if self.head:
            result = []
            cur_node = self.head
            while cur_node:
                result.append(cur_node.data)
        print("null <--"+" <--> ".join(result) + " --> null")

