class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def delete_node(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Testing the implementation
dll = DoublyLinkedList()

dll.insert_at_beginning(1)
dll.insert_at_beginning(2)
dll.insert_at_beginning(3)
dll.insert_at_end(4)
dll.insert_at_end(5)

dll.print_list()  # Output: 3 2 1 4 5

temp = dll.head
while temp.next is not None:
    temp = temp.next
dll.delete_node(temp)

dll.print_list()  # Output: 3 2 1 4