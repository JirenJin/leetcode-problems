class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.is_reversed = False


    # @param x, an integer
    # @return nothing
    def push(self, x):
        if self.is_reversed == True:
            self.reverse_stack()
            self.is_reversed = False
        self.stack1.append(x)



    # @return nothing
    def pop(self):
        if self.is_reversed == False:
            self.reverse_stack()
            self.is_reversed = True
        self.stack1.pop(-1)


    # @return an integer
    def peek(self):
        if self.is_reversed == False:
            self.reverse_stack()
            self.is_reversed = True
        return self.stack1[-1]

    # @return an boolean
    def empty(self):
        if self.stack1:
            return False
        else:
            return True


    # @return reversed stack
    def reverse_stack(self):
        while(self.stack1):
            self.stack2.append(self.stack1.pop(-1))
        self.stack1, self.stack2 = self.stack2, []


