from ll_node import Node

class LinkedList:
    def __init__(self, value):
        self.node = Node(value)
        self.head = self.node
        self.tail = self.node
        self.length = 1

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def pop(self):
        # Empty linked list
        if self.head is None:
            return None

        # Linked list with 1 element
        # self.head and self.tail point to the same place
        elif self.head.next is None:
            last_node = self.tail
            self.head = None
            self.tail = self.head
            self.length -= 1

            return last_node

        # Linked list with more then 1 element
        else:
            temp_node = self.head
            last_node = self.tail

            while temp_node.next is not last_node:
                temp_node = temp_node.next


            self.tail = temp_node
            self.tail.next = None
            self.length -= 1

            return last_node

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.tail = new_node

        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None

        node_to_pop = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = node_to_pop.next
            node_to_pop.next = None

        self.length -= 1
        return node_to_pop
