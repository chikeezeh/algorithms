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
    def add_before_node(self, key, data):
        cur_node = self.head 
        while cur_node:
            if cur_node.prev is None and cur_node.data == key:
                self.prepend(data)
                return
            elif cur_node.data == key:
                new_node = Node(data)
                prev = cur_node.prev
                prev.next = new_node
                cur_node.prev = new_node
                new_node.next = cur_node
                new_node.prev = prev
                return 
            cur_node = cur_node.next
    def delete_node(self,key):
        cur_node = self.head
        while cur_node:
            if cur_node.data == key and cur_node == self.head:
                # if only the head node exist
                if not cur_node.next:
                    cur_node = None
                    self.head = None
                    return
                # deleting head node, but there is another node that will become
                # the new head node
                else:
                    new_head = cur_node.next
                    cur_node.next = None 
                    cur_node = None
                    new_head.prev = None
                    self.head = new_head
                    return
            # deleting non head node    
            elif cur_node.data == key and cur_node.next:
                prev = cur_node.prev
                nxt = cur_node.next
                prev.next = nxt
                nxt.prev = prev
                cur_node.next = None
                cur_node.prev = None
                cur_node = None
                return
            # deleting non head node that is a tail node
            elif cur_node.data == key and not cur_node.next:
                prev = cur_node.prev
                prev.next = None
                cur_node = None
                return
            cur_node = cur_node.next
    def reverse(self):
        tmp = None
        cur_node = self.head
        while cur_node: # loop till we get to tail node
            tmp = cur_node
            cur_node.prev, cur_node.next = cur_node.next, cur_node.prev
            cur_node = cur_node.prev # because prev/next are swapped
        self.head = tmp
    def remove_duplicates(self):
        # create an empty dictionary to house elements in our ll
        dup_dict = {}
        cur_node = self.head
        while cur_node:
            if cur_node.data in dup_dict:
                nxt = cur_node.next
                self.delete_node(cur_node.data)
                cur_node = nxt
            else:
                dup_dict[cur_node.data] = 1
                cur_node = cur_node.next


dll1 = DoublyLinkedList() 
dll1.prepend("A")
dll1.print_list()
dll1.append("A")
dll1.print_list()
dll1.append("G")
dll1.print_list()
dll1.append("A")
dll1.prepend(50)
dll1.print_list()
dll1.remove_duplicates()
dll1.print_list()




