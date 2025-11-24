
#https://github.com/nirupamgarai00/DSA.git

from Stack import Stack as st


# create a Queue using two stacks               
class Queue:
    def __init__(self):
        
        self.enQ_stack = st()
        self.deQ_stack = st()
        
    
    def enqueue(self,data):
        self.enQ_stack.push(data)
    
    def dequeue(self):
        if  self.deQ_stack.isempty():
            if self.enQ_stack.isempty():
                raise ValueError('Queue is empty')
            else:
                while not self.enQ_stack.isempty():
                    temp = self.enQ_stack.pop()
                    self.deQ_stack.push(temp)
        
        temp = self.deQ_stack.pop()
        return temp
    


# test
q = Queue()
q.enqueue(1)
q.enqueue(3)

q.dequeue() 
q.enqueue(4) 

print(q.enQ_stack.peak()) 
print(q.deQ_stack.peak())