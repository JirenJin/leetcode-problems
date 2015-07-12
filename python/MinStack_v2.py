class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []
        self.min = []


    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)
        if not self.min or self.min[-1] >= x:
            self.min.append(x)



    # @return nothing
    def pop(self):
        if self.stack[-1] == self.min[-1]:
            self.min.pop()
        self.stack.pop()


    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]

    # @return an integer
    def getMin(self):
        if self.min:
            return self.min[-1]
