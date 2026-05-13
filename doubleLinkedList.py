from node import Node

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def print_multilist(self, level=0):
        if self.head is None:
            print ("Empty List"); return
        current = self.head
        while current:
            print(\"  \" * level + str(current))
            if current.sub_list:
                current.sub_list.print_multilinked_list(level + 1)
            current = current.next
    
    def search_by_attr(self, attr, value):
        current = self.head
        while current:
            if getattr(current, attr) == value:
                return current
            current = current.next
        return None
    