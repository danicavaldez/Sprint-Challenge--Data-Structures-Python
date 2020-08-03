import sys
sys.path.append('.doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == self.capacity:
            if self.storage.tail == self.current:
                self.current = self.storage.head
                self.storage.head.value = item
            else:
                self.current = self.current.next
                self.current.value = item
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

    def get(self):
        buffer_list = []

        item = self.storage.head

        while item:
            buffer_list.append(item.value)
            item = item.next
        
        return buffer_list

