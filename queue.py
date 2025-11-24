#https://github.com/nirupamgarai00/DSA.git

# Hi, this my code to create my own queue with basic funtionality there will be mixed consept of DSA and OOPS in python
# ======= Queue ==================
#len function [D]
# enqueue [D]
# dequeue [D]
# isempty[D]
# peek fron and rear[D]
# travers[D]

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
     
        

class Queue:
    
    # constractor
    def __init__(self):
        self.end = None # to mange rear
        self.front = None # to mange front
        self.size = 0 # for len
    
    # enqueue method 
    def enqueue(self,data):
        new_node = Node(data) # creating a new node
        
        # in case of empty Queue both front and end is the same
        if self.end == None:
            self.front = new_node
            self.end = new_node
        
        # normal case adding at the end and sefting the end    
        else:    
            
            self.end.next  = new_node
            
            self.end = new_node
        
        self.size += 1 # size counter increese
    
    # dequeue method
    def dequeue(self):
        
        # in case of empty queue 
        if self.front == None:
            raise ValueError('Queue os empty')
        
        # in case one element in the queue
        if self.front == self.end:
            self.front = None
            self.end = None
        
        # normal case
        else:
            self.front = self.front.next
            
        # decreasing the counter
        self.size -= 1
    
    # for traversing
    def travers(self):
        temp = self.front
        while temp != None:
            print(temp.data,end=' ')
            temp = temp.next

    # len funtion
    def __len__(self):
        return self.size
    
    # queue empty cheker
    def isempty(self):
        return self.front == None
    
    # front peek
    def peek(self):
        if self.front == None:
            raise ValueError('Queue is empty')
        
        return self.front.data
    # rear peek 
    def rear_peek(self):
        if self.end == None:
            raise ValueError('Queue is empty')
        return self.end.data
            
        
        
        