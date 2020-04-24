import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    # self is a node    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check where it fits 
        if value >= self.value:
        # look right
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        else:
            # if less
            # look left
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target > self.value:
            # look right
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
        if target < self.value:
            if self.left is not None:
                return self.left.contains(target)
            else: 
                return False


    # Return the maximum value found in the tree
    def get_max(self):
        #can ignore left
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    # apply the callback function to every single node of our life
    # at least 0(n), really depends on  the callback
    def for_each(self, cb):
        # apply the callback
        cb(self.value)
        # call the cb on the children of this node
        # lets check that it does even have children
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right:
            self.right.in_order_print(self.right)
    

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # line
        # enque -> add to head
        # deque -> delete from tail
        queue = Queue()
        queue.enqueue(node)
        
        while queue.len() > 0:
            delete_queue = queue.dequeue()
            print(delete_queue.value)
            if delete_queue.left:
                queue.enqueue(delete_queue.left)
            if delete_queue.right:
                queue.enqueue(delete_queue.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Last in, first out
        stack = Stack()
        #delete
        stack.push(node)

        while stack.len() > 0:
            delete_stack = stack.pop()
            print(delete_stack.value)
            if delete_stack.left:
                stack.push(delete_stack.left)
            if delete_stack.right:
                stack.push(delete_stack.right)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass