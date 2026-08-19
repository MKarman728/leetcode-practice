class MinStack:

    def __init__(self):
        self.stack = deque()
        self.mini = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mini) < 1:
            self.mini.append(val)
        else:
            min_val = val if val < self.mini[-1] else self.mini[-1]
            self.mini.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.mini.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.mini[-1]
