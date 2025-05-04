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
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        cur_node = self.head
        while cur_node:
            if cur_node.next == self.head:
                cur_node.next = new_node
                new_node.next = self.head
                self.head = new_node
                break
            cur_node = cur_node.next
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
    def __len__(self):
        """
        find the length of a circular ll
        """
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            if cur_node.next == self.head:
                break
            cur_node = cur_node.next
        return count


# test code
# cll1 = CircularLL()
# cll1.printlist()
# cll1.prepend(1)
# cll1.prepend(2)
# cll1.prepend(4)
# cll1.prepend(7)
# cll1.printlist()

cll2 = CircularLL()
cll2.printlist()
print(len(cll2))
cll2.append(1)
print(len(cll2))
cll2.append(2)
print(len(cll2))
cll2.append(4)
print(len(cll2))
cll2.append(7)
print(len(cll2))
cll2.printlist()