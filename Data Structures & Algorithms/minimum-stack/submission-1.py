class MinStack:

    def __init__(self):
        self.stack_struct = []
        self.min_stack = []
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        self.stack_struct.append(val)
        if val < self.minimum:
            self.minimum = val
        self.min_stack.append(self.minimum)

    def pop(self) -> None:
        self.stack_struct.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if len(self.stack_struct) == 0:
            return "Error no values"
        return self.stack_struct[-1]

    def getMin(self) -> int:
        length = len(self.min_stack)
        return self.min_stack[length - 1]
