class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []
        self.min = []


    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)
        if self.min:
            if self.stack[self.min[-1]] > x:
                self.min.append(len(self.stack) - 1)
            else:
                pass
        else:
            self.min.append(len(self.stack) - 1)


    # @return nothing
    def pop(self):
        if len(self.min) > 0:
            if self.min[-1] == len(self.stack) - 1:
                self.min.pop()
        if self.stack:
            self.stack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]


    # @return an integer
    def getMin(self):
        if self.min:
            return self.stack[self.min[-1]]
