from linked_lists.ll_node import Node
class DoublyNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.prev = None
