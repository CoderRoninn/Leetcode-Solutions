from collections import deque

class MyStack(object):

    def __init__(self):
        self.stack = deque()

        

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        for i in range(len(self.stack) -1):
            self.stack.append(self.stack.popleft())
        return self.stack.popleft()    
       
    def top(self):
        return self.stack[-1]
       
        

    def empty(self):
        if not self.stack:
            print("The stack is empty")
            return True
        else:
            return False
               
      
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()