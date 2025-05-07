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
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        # print the nodes of a dll
        result = []
        cur_node = self.head
        while cur_node:
            result.append(str(cur_node.data))
            cur_node = cur_node.next
        print("null <-- "+" <--> ".join(result) + " --> null")
    def add_after_node(self,key,data):
        # add a node to a dll after a node.data = key
        cur_node = self.head
        while cur_node:
            if not cur_node.next and cur_node.data == key:
                self.append(data)
                return
            elif cur_node.data == key:
                new_node = Node(data)
                nxt = cur_node.next #keep track on the next of current node before we swapp pointers.
                cur_node.next = new_node
                new_node.next = nxt
                new_node.prev = cur_node
                nxt.prev = new_node
                return
            cur_node = cur_node.next

dll1 = DoublyLinkedList()
dll1.prepend("F")
dll1.print_list()
dll1.append("A")
dll1.print_list()
dll1.append("B")
dll1.print_list()
dll1.append("C")
dll1.prepend(50)
dll1.print_list()

dll1.add_after_node("F","X")
dll1.print_list()

