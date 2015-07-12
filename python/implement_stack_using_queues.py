class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.q1 = []
        self.q2 = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        q_using, q_empty = self.is_using()
        q_using.append(x)

    # @return nothing
    def pop(self):
        if not self.empty():
            q_using, q_empty = self.is_using()
            while(len(q_using) > 1):
                q_empty.append(q_using.pop(0))
            q_using.pop(0)

    # @return an integer
    def top(self):
        if not self.empty():
            q_using, q_empty = self.is_using()
            while(len(q_using) > 1):
                q_empty.append(q_using.pop(0))
            top = q_using.pop(0)
            q_empty.append(top)
            return top
        else:
            return None


    # @return an boolean
    def empty(self):
        if not self.q1 and not self.q2:
            return True
        else:
            return False

    # @return a tuple contains q_using and q_empty
    def is_using(self):
        if not self.q1:
            return self.q2, self.q1
        else:
            return self.q1, self.q2
