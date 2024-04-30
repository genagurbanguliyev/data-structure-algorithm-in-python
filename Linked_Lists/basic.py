class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.num_nodes = 0

    # O(1) running time complexity
    def insert_start(self, data):
        self.num_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    # O(N) running time complexity
    def insert_end(self,data):
        self.num_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            actual_node: Node = self.head

            while actual_node.next_node is not None:
                actual_node = actual_node.next_node

            actual_node.next_node = new_node

    # O(N) running time complexity
    def size_of_list(self):
        return self.num_nodes

    # O(N) running time complexity
    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node


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

    ll = LinkedList()
    ll.insert_end(0)
    ll.insert_end(1)
    ll.insert_end(2)
    ll.insert_end(3)
    ll.traverse()
    print("Size of linked list: ", ll.size_of_list())
    ll.remove_node(3)
    ll.traverse()


    end_time = time.time()
    print("Time taken:", end_time - start_time, "seconds")