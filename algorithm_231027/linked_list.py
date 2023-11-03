class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
    
    def append(self, data):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)
    
    def get_node(self, index):
        current = self.head
        count = 0
        while count < index:
            current = current.next
            count += 1
        return current
    
    def delete(self, index):
        if index == 0:
            del_data = self.head.data
            self.head = self.head.next
            return del_data
        node = self.get_node(index - 1)
        del_data = node.next.data
        node.next = node.next.next
        return del_data