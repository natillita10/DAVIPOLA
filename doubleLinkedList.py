from node import Node

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_child(self, parent:Node, child:Node):
        if parent.sub_list is None:
            sublist = LinkedList()
            sublist.head = child
            sublist.tail = child
            parent.sub_list = sublist
        else:
            current = parent.sub_list.tail
            current.next = child
            child.prev = current
            parent.sub_list.tail = child
        return parent.sub_list