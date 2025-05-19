from .ll_node import Node

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
        return True

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
        if self.length == 0:  # Edge case when we have 0 elements in the list
            return None

        node_to_pop = self.head
        self.head = self.head.next
        node_to_pop.next = None
        self.length -= 1
        if self.length == 0:  # Edge case when we have 1 element in the list
            self.tail = None
        return node_to_pop

    def get(self, index:int):
        # Check if indext is out of bounds
        if (index < 0) or (index >= self.length):
            return None

        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        return temp_node

    def set_value(self, index: int, value):
        temp_node = self.get(index)
        if not temp_node:  # If index is out of bounds
            return False
        temp_node.value = value
        return True

    def insert(self, index: int, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp_node = self.get(index - 1)
        new_node.next = temp_node.next
        temp_node.next = new_node
        self.length += 1
        return True

    def remove(self, index: int):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        temp_node = self.get(index - 1)
        node_to_remove = temp_node.next
        temp_node.next = node_to_remove.next
        node_to_remove.next = None
        self.length -= 1
        return node_to_remove

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        while temp:  # While temp is not pointing to None
            after = temp.next
            temp.next = before
            before = temp
            temp = after
