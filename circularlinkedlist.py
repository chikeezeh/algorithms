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
    def split_list(self):
        # function splits a circularLL in the middle and prints out the first and second halves.
        # check if the cll is empty
        if not self.head:
            return
        
        # we need to get the mid point
        size = len(self)
        # if size is == 1
        if size == 1:
            print(self)
            return
        # if greater than 1
        first_half = []
        first_half_cll = CircularLL()
        second_half = []
        second_half_cll = CircularLL()
        mid = size // 2
        cur_node = self.head
        for _ in range(mid):
            first_half.append(cur_node.data)
            cur_node = cur_node.next
        for _ in range(mid,size):
            second_half.append(cur_node.data)
            cur_node = cur_node.next
        
        for first in first_half:
            first_half_cll.append(first)
        for second in second_half:
            second_half_cll.append(second)
        print("firsthalf")
        first_half_cll.printlist()
        print("\n")
        print("secondhalf")
        second_half_cll.printlist()



# test code
# cll1 = CircularLL()
# cll1.printlist()
# cll1.prepend(1)
# cll1.prepend(2)
# cll1.prepend(4)
# cll1.prepend(7)
# cll1.printlist()

# cll2 = CircularLL()
# cll2.printlist()
# print(len(cll2))
# cll2.append(1)
# print(len(cll2))
# cll2.append(2)
# print(len(cll2))
# cll2.append(4)
# print(len(cll2))
# cll2.append(7)
# print(len(cll2))
# cll2.printlist()
cll2 = CircularLL()
cll2.append("A")
cll2.append("B")
cll2.append("C")
cll2.append("D")
cll2.append("E")
cll2.append("F")
cll2.printlist()
cll2.split_list()