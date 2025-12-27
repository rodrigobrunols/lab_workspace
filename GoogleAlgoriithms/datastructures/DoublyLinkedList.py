class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

# john<=ben<=mathew<=peter
# john=>ben=>mathew=>peter


def delete_aux(current_node):
    if current_node.next:
        current_node.next.prev = current_node.prev
    if current_node.prev:
        current_node.prev.next = current_node.next


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Time: O(1)
    # Space: O(1)
    def insert_head(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Time: O(1)
    # Space: O(1)
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
            new_node.prev = current

    # Time: O(n)
    # Space: O(1)
    def print_list(self):
        if not self.head:
            print("empty linked list")
            return
        current_node = self.head

        while current_node:
            print(current_node)
            current_node = current_node.next

    # Time: O(n)
    # Space: O(1)
    def delete_node(self, data):
        current_node = self.head

        while current_node:
            if current_node.data == data:
                delete_aux(current_node)
                return

            else:
                current_node = current_node.next

    # Time: O(n)
    # Space: O(1)
    def reverse_list(self):
        prev = None
        curr = self.head

        while curr:
            aux = curr.next
            curr.next = prev
            prev = curr
            curr = aux
        self.head = prev



linkedList = DoublyLinkedList()
linkedList.insert("john")
linkedList.insert("ben")
linkedList.insert("mathew")
linkedList.insert("peter")
linkedList.print_list()

linkedList.delete_node("mathew")
print()
linkedList.print_list()

linkedList.delete_node("teste")
print()
linkedList.print_list()
