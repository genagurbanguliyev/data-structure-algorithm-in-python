class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None

    def __repr__(self):
        return str(self.data)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_nodes = 0

    # O(1) running time complexity
    def insert_start(self, data):
        self.num_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

    # O(N) running time complexity
    def size_of_list(self):
        return self.num_nodes

    # we can traverse a doubly linked list in both directions
    def traverse_forward(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node

    def traverse_backward(self):
        actual_node = self.tail

        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.prev_node



    # O(N) running time complexity
    def remove_node(self, data):
        if self.head is None:
            return

        actual_node = self.head
        prev_node = None

        while actual_node is not None and actual_node.data != data:
            prev_node = actual_node
            actual_node = actual_node.next_node

        # Search miss
        if actual_node is None:
            return

        if prev_node is None:
            self.head = actual_node.next_node
        else:
            prev_node.next_node = actual_node.next_node

import time
if __name__ == '__main__':
    start_time = time.time()

    ll = DoublyLinkedList()
    ll.insert_start(0)
    ll.insert_start(1)
    ll.insert_start(2)
    ll.insert_start(3)
    ll.traverse_forward()
    print("Size of linked list: ", ll.size_of_list())
    ll.traverse_backward()


    end_time = time.time()
    print("Time taken:", end_time - start_time, "seconds")