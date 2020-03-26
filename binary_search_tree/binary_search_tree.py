import sys
sys.path.append('../queue_and_stack')

from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #here, we're going to compare the value to the root
        if value >= self.value:
            #look right
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                # if no node, add here
                self.right.insert(value)
        else:
            # look left if value is smaller than self.value
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                #if no node, add here
                self.left.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            #check left
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False
              
        else:
            #check right
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
              


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is not None:
            # if a child to the right, seek max value on the right side
            return self.right.get_max()
        else:
            #if no right child, return this value
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        #call back on each node
        cb(self.value)
        # if both sides of tree are not none 
        if self.left is not None and self.right is not None:
            #target both sides using for_each func
            self.left.for_each(cb)
            self.right.for_each(cb)
        elif self.right is not None:
            self.right.for_each(cb)
        elif self.left is not None:
            self.left.for_each(cb)
        else: 
            return self.value

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass