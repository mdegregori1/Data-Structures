import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

#  * `enqueue` should add an item to the back of the queue.
#    * `dequeue` should remove and return an item from the front of the queue.
#    * `len` returns the number of items in the queue.
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
        
    def len(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        # check if its empty
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
    
    
