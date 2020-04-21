import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        # pop() is an inbuilt function in Python that removes and returns last value from the list or the given index value.
        # last value in stack would be head
        if self.size == 0:
            return 
        else:
            self.size -= 1
            removed = self.storage.remove_from_head()
            return removed

    def len(self):
        return self.size