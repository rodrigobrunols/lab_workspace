class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert(self, data):
        new_node = Node(data)

        # head->node1->node2
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        if not self.head:
            print("empty linked list")
            return
        current_node = self.head

        while current_node:
            print(current_node)
            current_node = current_node.next

    # john=>ben=>mathew=>peter
    # result = john<=ben<=mathew<=peter
    # current,prev
    def reverse_list(self):
        prev = None
        curr = self.head

        while curr:
            aux = curr.next
            curr.next = prev
            prev = curr
            curr = aux
        self.head = prev


linkedList = LinkedList()
linkedList.insert("john")
linkedList.insert("ben")
linkedList.insert("mathew")
linkedList.insert("peter")
print()
linkedList.print_list()
linkedList.reverse_list()
print()
print("reversed")
linkedList.print_list()

linkedList = LinkedList()
linkedList.insert_head("john")
linkedList.insert_head("ben")
linkedList.insert_head("mathew")
linkedList.insert_head("peter")

print()
linkedList.print_list()

linkedList = LinkedList()
print()
linkedList.print_list()
