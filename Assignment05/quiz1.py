class Node:
    def __init__(self, datum, next=None):
        self.datum = datum
        self.next = next

class MyDigitQueue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None

    def front(self):
        return self.front_node.datum if self.front_node else None

    def enqueue(self, item):
        if isinstance(item, int) and 0 <= item <= 9:
            new_node = Node(item)
            if not self.front_node:
                self.front_node = new_node
                self.rear_node = new_node
            else:
                self.rear_node.next = new_node
                self.rear_node = new_node

    def dequeue(self):
        if self.front_node:
            datum = self.front_node.datum
            self.front_node = self.front_node.next
            return datum
        else:
            return None
