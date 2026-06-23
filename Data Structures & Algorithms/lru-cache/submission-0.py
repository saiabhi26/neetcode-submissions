class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.back = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.back = self.head
    
    def remove(self, node):
        prev = node.back
        nxt = node.next
        prev.next = nxt
        nxt.back = prev
    
    def insert(self, node):
        temp = self.tail.back
        temp.next = node
        node.back = temp
        node.next = self.tail
        self.tail.back = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            temp = self.head.next
            self.remove(temp)
            del self.cache[temp.key]



