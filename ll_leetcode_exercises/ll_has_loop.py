from ll_find_middle_node import LinkedList

class LinkedListHasLoop(LinkedList):
    def has_loop(self):
        slow = self.head.next
        fast = self.head.next.next
        while fast != slow and fast != self.tail and fast is not None:
            slow = slow.next
            fast = fast.next.next

        if fast == slow:
            return True
        return False



my_linked_list_1 = LinkedListHasLoop(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop() ) # Returns True




my_linked_list_2 = LinkedListHasLoop(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop() ) # Returns False


"""
    EXPECTED OUTPUT:
    ----------------
    True
    False

"""
