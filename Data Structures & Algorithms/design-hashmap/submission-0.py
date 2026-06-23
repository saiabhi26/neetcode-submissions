class MyHashMap:

    def __init__(self):
        self.keyarr = [False]*1000001
        self.valarr = [-1]*1000001

    def put(self, key: int, value: int) -> None:
        self.keyarr[key] = True
        self.valarr[key] = value

    def get(self, key: int) -> int:
        return self.valarr[key]

    def remove(self, key: int) -> None:
        self.keyarr[key] = False
        self.valarr[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)