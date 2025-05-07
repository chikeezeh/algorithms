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
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node
        new_node.prev = cur_node



    def prepend(self,data):
        # add a node to the beginning of a dll
        pass

    def print_list(self):
        # print the nodes of a dll
        result = []
        cur_node = self.head
        while cur_node:
            result.append(cur_node.data)
            cur_node = cur_node.next
        print("null <-- "+" <--> ".join(result) + " --> null")

dll1 = DoublyLinkedList()
dll1.print_list()
dll1.append("A")
dll1.print_list()
dll1.append("B")
dll1.print_list()

