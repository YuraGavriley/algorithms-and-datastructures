from .dll_node import DoublyNode


class DoublyLinkedList:
    def __init__(self, value):
        self.node = DoublyNode(value)
        self.head = self.node
        self.tail = self.node
        self.length = 1

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def append(self, value):
        new_node = DoublyNode(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True

dll = DoublyLinkedList(101)
dll.append(-1)
dll.print_list()
