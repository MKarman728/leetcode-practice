class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.count = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, key, value):
        node = Node(key, value)
        self.count += 1
        #Point node to the head and to the next node.
        node.prev = self.head
        node.next = self.head.next
        #fix head and first to point to new node.
        self.head.next.prev = node
        self.head.next = node
        self.cache[key] = node

    def remove(self, key):
        node = self.cache[key]
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        node.next = None
        node.prev = None
        del self.cache[key]
        self.count -= 1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(key)
        self.add(node.key, node.value)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
        if self.count + 1 > self.capacity:
            self.remove(self.tail.prev.key)
        self.add(key, value)
