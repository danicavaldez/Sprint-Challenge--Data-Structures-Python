"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next

        if self.next:
            self.next.prev = self.prev            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.tail = new_node
        else:
            new_node.next = self.head
        
        self.head = new_node
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return None
        
        elif self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        else: 
            value = self.head.value
            self.head = self.head.next
            self.length -= 1
            return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)

        if self.length == 0:
            self.head = new_node
        
        else:
            new_node.prev = self.tail
            new_node.prev.next = new_node
        
        self.tail = new_node
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None:
            return None

        elif self.head == self.tail:
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        else: 
            value = self.tail.value
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.length -= 1
            return value

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.head == self.tail:
            return self.length

        elif self.length == 2: 
            temp = self.head
            self.head = node
            self.tail= temp
            self.head.next = self.tail
            self.head.prev = None
            self.tail.prev = self.head
            self.tail.next = None
            return self.length

        else:
            value = node.value
            self.add_to_head(value)
            node.delete()
            self.length -= 1
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.head == self.tail:
            return self.length

        elif self.length == 2: 
            temp = self.tail
            self.tail = node
            self.head = temp
            self.head.next = self.tail
            self.head.prev = None
            self.tail.prev = self.head
            self.tail.next = None
            return self.length

        else:
            value = node.value
            self.delete(node)
            self.add_to_tail(value)
            # node.prev.next = node.next
            # node.next.prev = node.prev
            # self.tail.next = node
            # self.tail.next = None
            # node.prev = self.tail
            # self.tail = node
            # return self.length

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # if not self.length:
        #     return None
        
        # if self.length > 1:
        #     if node is self.head:
        #         node.next.prev = None
        #         self.head = node.next

        #     elif node is self.tail:
        #         node.prev.next = None
        #         self.tail = node.prev
            
        #     else:
        #         node.prev.next = node.next
        #         node.next.prev = node.prev
        
        # else:
        #     self.head = None
        #     self.tail = None
        
        # self.length -= 1
        if self.length == 0:
            return
                    
        elif self.length == 1:
            self.head = None
            self.tail = None

        elif self.head == node:
            self.head = self.head.next
            node.delete()
        
        elif self.tail == node:
            self.tail == self.tail.prev
            node.delete()
        
        else:
            node.delete()

        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None:
            return None
        
        cur_node = self.head
        cur_max = self.head.value

        while cur_node is not None:
            if cur_node.value > cur_max:
                cur_max = cur_node.value
            cur_node = cur_node.next
        
        return cur_max