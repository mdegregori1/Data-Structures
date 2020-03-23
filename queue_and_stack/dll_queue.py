import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

#notes
# ordered -> think of line 
# FIFO

#  * Should have the methods: `enqueue`, `dequeue`, and `len`.
#    * `enqueue` should add an item to the back of the queue.
#    * `dequeue` should remove and return an item from the front of the queue.
#    * `len` returns the number of items in the queue.
 
# ![Image of Queue](https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/600px-Data_Queue.svg.png)

#if doesn't work ask TL 

# print(DoublyLinkedList)

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        #back of queue is the head, or beginning of list
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        #should remove and return an item from the front of the queue.
        # front of queue = tail of the list
        #first, check on the length of the list
        if self.size > 0:
            self.size -= 1
            removed_list = self.storage.remove_from_tail()
            return removed_list
        else:
            return 


    def len(self):
        dll = self.size
        return dll

