"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            # if previous from deleted node, then it's next changes
            self.prev.next = self.next
        if self.next:
            # if next from deleted node, then it's previous changes
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            # means its empty
            self.head = new_node
            self.tail = new_node
        else:
            # means there's currently a head and/or a tail
            # old head is now next from node we're going to add (new head)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            



    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            # means its empty
            self.head = new_node
            self.tail = new_node
        else:
            # means there's currently a head and/or a tail
            # old tail is now prev from node we're going to add (new tail)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
            return 
        # if its not the head, then add the node value to head, and then delete its previous node
        value = node.value
        self.add_to_head(value)
        self.delete(node)


    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return 
        # if its not the tail, then add the node value to head, and then delete its previous node
        value = node.value
        self.add_to_tail(value)
        self.delete(node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self.length -= 1
        # this is the only node
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # its the head
        elif node is self.head:
            self.head = node.next
            node.delete()
        # its the tail
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        # its in the middle
        else:
            # change the pointers in either direction
            node.delete()

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        #starting at the top
        current = self.head
        # create max var
        max_value = self.head.value
        # why while loop? 
        while(current is not None):
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value

        # loop through nodes here
        # compare value in node to max found
        # return max found
            
