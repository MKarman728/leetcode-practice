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
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            node = Node(key, value)
            self.insert(node)
            if len(self.cache) > self.capacity:
                del self.cache[self.tail.prev.key]
                self.remove(self.tail.prev)
        
    def insert(self, node: Node):
        self.cache[node.key] = node
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev