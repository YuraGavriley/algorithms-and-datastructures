from ll_node import Node

class LinkedList:
    def __init__(self, value):
        self.node = Node(value)
        self.head = self.node
        self.tail = self.node
        self.length = 1
