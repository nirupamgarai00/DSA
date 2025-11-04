#https://github.com/nirupamgarai00/DSA.git

# Hi, this my code to create my own Linkedlist there will be mixed consept of DSA and OOPS in python

#len function [D]
# append [D]
# print[D]
# index [D]
# pop [D]
# push[D]
# find [D]
# insert after [D]
# delete [D]
# remove [D]
# min/max/sum [D]

# its a Node for Linkedlist
class Node:
    def __init__(self, data):
        self.data = data# contain data
        self.next = None # its contain the next Node



class LinkedList:
    
    def __init__(self):
        # creating a empty linked list
        self.head = None # mange only the start
        self.tail = None # mange only the end
        self.n = 0 # counts the number item in the list
    
    # a magic method which is called when exicuted len(obj)    
    def __len__(self):
        return self.n # return the len of the LL(linkedlist)
    
    
    # inseting item from head
    def insert_head(self, data):
        
        n = Node(data) # creating a Node
        
        # in case of LL is empty
        if self.head == None: 
            self.head = n
            self.tail = n
        # when LL is not empty
        else:
            n.next = self.head
            self.head = n
        
        self.n += 1 # increamenting the counter
    
    # append funtion
    def append(self,data):
        
        n = Node(data) # creating a Node
        if self.head == None:# its a empty LL(linkedlist)
            self.head = n
            self.tail = n
            
        else:# when linked list is Not empty
            self.tail.next = n
            self.tail = n
        
        self.n += 1 # increasing the count
    
    # this method travers the LL by index or value
    def __travers(self,index = None, value = None):
        # for the cuurent Node
        temp = self.head
        # in case of index
        if index != None:
            
            for i in range(index):
                if temp == None:
                    raise IndexError(f"{index} out of range")
                temp = temp.next
            return temp
        # in case of value
        else:
            i = 0 # for identifaing the index of the value
            # travering
            while temp != None:
                # returing index and Node if value is found
                if temp.data == value:
                    return temp , i
                temp = temp.next # itarator
                i += 1# index manger
            
            raise ValueError(f'{value} is not in the Linked list')# rasing error if value not found in the LL
    
    # insert by index(after) 
    def index_insert(self,idx,data):
        if idx >=self.n:
            self.append(data)
            return
        n = Node(data)# new Node
        # finding the node
        temp = self.__travers(idx)
        # adding it to the LL
        n.next = temp.next
        temp.next = n 
        
        self.n += 1# incrementing counter   
        
        # in case last element
        if temp == self.tail:
            self.tail = n 
    
    # clear
    def clear(self):
        self.__init__() # intial sate of LL or an empty LL
    
    # clear from head
    def head_del(self):
        # in case of empty list
        if self.head == None:
            raise ValueError('LinkedList is empty')
        # there is only one elemt in the LL then making it empty
        if self.n == 1:
            self.__init__()
        
        # deleting head
        self.head = self.head.next
        self.n -= 1# decreamenting the counter
    
    # delete by index
    def __delitem__(self,idx):
        # when LL is empty
        if self.head == None:
            raise ValueError('Linkedlist is empty')
        if idx == 0:# when one element
            self.head_del()
            return
        # when more thenone element
        if 0<idx<self.n:
            temp = self.__travers(idx-1)
            if temp.next == self.tail:
                self.tail = temp
            temp.next = temp.next.next
            self.n -= 1
            
            return
        # in case of invalid index    
        raise IndexError(f'{idx} is out of range')
    
    # delete by value
    def remove(self,value):
        temp,i = self.__travers(value=value)
        self.__delitem__(i)
    
    # delete item from the tail
    def tail_del(self):
        # when LL is empty
        if self.head == None:
            raise ValueError('Linkedlist is empty')
        # when LL has only one element
        elif self.n == 1:
            self.__init__()
        
        # when LL has more then one element    
        else:
            # finding the Node of the 2nd last element and making it as tail
            self.tail = self.__travers(self.n-2)
            
            self.tail.next = None # and making the next Node of tail None
            self.n -= 1 # counter decrement   
    
    # search by index
    def __getitem__(self,idx):
        
        if 0<=idx<self.n:            
            temp = self.__travers(idx) # this handles invalid idex but to use inbuild min, max and sum funtion i need to raise an error in the __getitem__ method
            return temp.data
        else:
            raise IndexError(f"{idx} out of range")
    
    # search by value
    def find(self, value):
        temp,i = self.__travers(value=value)
        return i, temp
    
    # magic method called when print(obj) is exicuted    
    def __str__(self):
        # starting Node
        temp = self.head
        # storing the result
        result = ''
        # traversing and adding data to result
        while temp != None:
            result += str(temp.data)+'->'
            temp = temp.next
            
        return result[:-2]# result returned
    
    