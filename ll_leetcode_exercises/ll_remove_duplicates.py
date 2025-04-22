from ll_base import LinkedList

class LinkedListRemoveDuplicates(LinkedList):
    def remove_duplicates(self):
        if self.head is None:
            return None
        previous = self.head
        current = previous.next
        unique_vals = set()
        unique_vals.add(previous.value)

        while current:
            if current.value not in unique_vals:
                unique_vals.add(current.value)
                previous = previous.next
            else:
                previous.next = current.next
                current.next = None
            current = previous.next

def test_remove_duplicates(linked_list, expected_values):
    print("Before: ", end="")
    linked_list.print_list()
    linked_list.remove_duplicates()
    print("After:  ", end="")
    linked_list.print_list()

    # Collect values from linked list after removal
    result_values = []
    node = linked_list.head
    while node:
        result_values.append(node.value)
        node = node.next

    # Determine if the test passes
    if result_values == expected_values:
        print("Test PASS\n")
    else:
        print("Test FAIL\n")

# Test 1: List with no duplicates
ll = LinkedListRemoveDuplicates(1)
ll.append(2)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 2: List with some duplicates
ll = LinkedListRemoveDuplicates(1)
ll.append(2)
ll.append(1)
ll.append(3)
ll.append(2)
test_remove_duplicates(ll, [1, 2, 3])

# Test 3: List with all duplicates
ll = LinkedListRemoveDuplicates(1)
ll.append(1)
ll.append(1)
test_remove_duplicates(ll, [1])

# Test 4: List with consecutive duplicates
ll = LinkedListRemoveDuplicates(1)
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 5: List with non-consecutive duplicates
ll = LinkedListRemoveDuplicates(1)
ll.append(2)
ll.append(1)
ll.append(3)
ll.append(2)
ll.append(4)
test_remove_duplicates(ll, [1, 2, 3, 4])

# Test 6: List with duplicates at the end
ll = LinkedListRemoveDuplicates(1)
ll.append(2)
ll.append(3)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 7: Empty list
ll = LinkedListRemoveDuplicates(None)
ll.head = None  # Directly setting the head to None
ll.length = 0   # Adjusting the length to reflect an empty list
test_remove_duplicates(ll, [])
