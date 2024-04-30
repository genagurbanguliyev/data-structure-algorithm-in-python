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


import time
if __name__ == '__main__':
    start_time = time.time()
    ll = LinkedList()
    for i in range(500000):
        ll.insert_start(i)
    end_time = time.time()
    print("Length of Linked List:", ll.num_nodes, "\tTime complexity for Linked List:", end_time - start_time, "seconds")

    start_time = time.time()
    arr = []
    for i in range(500000):
        arr.insert(0, i)
    end_time = time.time()
    print("Length of Array", len(arr),"\tTime complexity for Array:", end_time - start_time, "seconds")