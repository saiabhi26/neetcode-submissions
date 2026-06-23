class MinStack:

    def __init__(self):
        self.st = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if len(self.minstack) == 0 or val <= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self) -> None:
        if self.st[-1] == self.minstack[-1]:
            self.minstack.pop()
        self.st.pop()        

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
