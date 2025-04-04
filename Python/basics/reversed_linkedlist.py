#reversed linked list
class Node1:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList1:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node1(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

llist = LinkedList1()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

print("original")
llist.print_list()

llist.reverse()

print("reversed")
llist.print_list()