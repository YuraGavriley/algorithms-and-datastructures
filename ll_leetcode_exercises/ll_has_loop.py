from ll_base import LinkedList

class LinkedListHasLoop(LinkedList):
    # def has_loop(self):
    #     slow = self.head.next
    #     fast = self.head.next.next
    #     while fast != slow and fast != self.tail and fast is not None:
    #         slow = slow.next
    #         fast = fast.next.next

    #     if fast == slow:
    #         return True
    #     return False

    def has_loop(self):
        slow = self.head
        fast = self.head

        # This stuff is a tricky one. If fast.next is not None goes first in the condition,
        # it could potentially be None.next which will throw an error.
        # But if we check fast first (if it is None), the loop will not check the second condition and will simply break.
        while fast is not None and fast.next is not None:
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
