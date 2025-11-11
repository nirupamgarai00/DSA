#https://github.com/nirupamgarai00/DSA.git

# Hi, this my code to create my own Stack(using Linked List) there will be mixed consept of DSA and OOPS in python

#len function [D]
# print[D]
# pop [D]
# push[D]
# peak [D]
# isempty[D]




class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    # push
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    # pop
    def pop(self):
        
        # if stack is empty
        if self.top == None:
            raise ValueError('Stack is empty')
        
        temp = self.top.data
        
        self.top = self.top.next
        self.size -= 1
        
        return temp # returing the value
    
    # if Stack is empty
    def isempty(self):
        return self.top == None
    
    
    # peak
    def peak(self):
        if self.isempty():
            raise ValueError('Stack is empty')
        else:
            return self.top.data
    
    
    # print method
    def show(self):
        temp = self.top
        
        while temp != None:
            print(temp.data)
            temp = temp.next
        
    # len method
    def __len__(self):
        return self.size
        
    
    
        
    
        