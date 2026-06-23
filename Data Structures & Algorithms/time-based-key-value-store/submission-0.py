class TimeMap:

    def __init__(self):
        self.hmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[(key,timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        curstamp = timestamp
        while curstamp > 0:
            if (key,curstamp) in self.hmap:
                return self.hmap[(key,curstamp)]
            else:
                curstamp-=1
        return ""
