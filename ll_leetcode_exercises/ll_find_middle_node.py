from ll_base import LinkedList


class LinkedListFindMiddleNode(LinkedList):
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast != self.tail and fast is not None:
            slow = slow.next
            fast = fast.next.next
        return slow



my_linked_list = LinkedListFindMiddleNode(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3

"""
