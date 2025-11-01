#https://github.com/nirupamgarai00/DSA.git

# Hi, this my code to create my own list there will be mixed consept of DSA and OOPS in python
# =======dynamic array==================
#len function [D]
# append [D]
# print[D]
# index [D]
# pop [D]
# push[D]
# find [D]
# insert [D]
# delete [D]
# remove [D]
# short[D]
# min/max/sum [D]
# extend [D]
# nagative indexing[D]
# marge[D]
# slicing [D]


import ctypes # this modle allows you to use C compatible data types

class Mylist:# creating a class for list
    
    def __init__(self):# constractor - when instance in created this function is called
        
        # as you know list is a dinamic array So we need mange the size of of array and well as number of elements in it
        self.size = 1# to track the size of the array
        self.n = 0 # to track number of elements in the array
        
        self.A = self.__make_arr(self.size)# creating a empty array of size 1
        
    def __len__(self):# this is dunnder funtion which called when len(obj) is executed
        return self.n # returns the number elemnt in the array
    
    def __resize(self):# this is private funtion which is just to make bigger array and copy the previous array to new one
        
        self.size += 8 # updating the new size
        
        temp = self.__make_arr(self.size) # making new array with +8 with the previous self.size and storing the new array into temp
        
        # coping the whole array from self.A to temp
        for i in range(self.n):
            temp[i] = self.A[i]
        
        self.A = temp # coping temp to self.A
    
    
    # appned method
    def append(self,item):
        
        # makking the array bigger
        if self.n>=self.size:
            self.__resize()
        
        # adding a new element into the end of elements   
        self.A[self.n] = item
        self.n += 1
     
    # dunnder funtion called  when obj + obj is exicuted    
    def __add__(self,obj):
        # checking if obj is in Mylist class or not
        if type(obj) != Mylist:
            raise TypeError("Can only concatenate Mylist or list")
        
        result = Mylist() # new instance to store the obj + obj
        
        # adding the self to the result
        result.extend(self)
         # adding the obj to the result
        result.extend(obj)
        
        # now returning the result
        return result    
            
    
    def __make_arr(self,size):
        
        return (size*ctypes.py_object)() # this line for creating ctype array(static,refarencial)
    
    
    def __str__(self):# this dunnder method called when print(obj) is exicuted
        temp = ''# creating a empty string
        
        # converting array into string
        for i in range(self.n):
            temp += str(self.A[i])+','
        
        return '['+temp[:-1]+']'# returing a string just like list shows (:
    
    # a method to handle both nagative indexing and well as invalid range
    def __mange_index(self,idx):
        
        if 0<=idx<self.n:# when positive idx
            return idx
        
        elif -self.n<idx<0:# when negative idx
            return self.n + idx
        
        else:# when invalid index
            raise IndexError('index out range')
    
    # this is dunnder method called when obj[i] is exicuted
    def __getitem__(self,idx):
        
        # idx contain value like [2:8:2]
        if isinstance(idx,slice): 
            
            start , stop, step = idx.indices(self.n) # convert the slice into start , stop and step safly
            
            result = Mylist() # creating new Mylist to store the new refine list as start, stop and step
            # to store the new refine list as per start, stop and step
            for i in range(start, stop, step):
                result.append(self.A[i])
            return result
        
        
        
        # single index case
        # cheking if index in range or not if yes then returning the value 
        # else giving an index error
        idx = self.__mange_index(idx)
        return self.A[idx]
        
    # pop funtion    
    def pop(self): 
        
        
        if self.n>0:# cheking if the list is empty or not
            # if not 
            temp = self.A[self.n - 1] # storing the last value
            self.n -= 1 # decreasing the element number
            return temp # return the pop item
        else: 
            # if empty
            raise ValueError("list is empty") # returing an error that list is empty
    
    # push funtion    
    def push(self,var):
        
        # as you know funtionality of push and append are same just calling the append function
        self.append(var)
    
    # clear funtion
    def clear(self):
        
        # seting list into intial sate
        self.n = 0
        self.size = 1
    
    # find 
    def find(self, item):
        # searching if item exsist in the list
        for i in range(self.n):
            if self.A[i] == item:# if yes then returning the index
                return i
        # if not then ValueError a value error
        raise ValueError(f"{item} is not in the list")
    
    
    # insert
    def insert(self, idx, item):
        
        
        # if idx >= self.n then used append funtion
        if idx>=self.n or idx<-self.n:
            self.append(item)
            return
        
        # if index is nagative value then ??
        idx = self.__mange_index(idx)
        
        
        # resizing if the list is full
        if self.n >= self.size:
            self.__resize()
        
        # shifting every value till index
        i = self.n # itarator
        while i>idx:
            self.A[i] = self.A[i-1]
            i -= 1
        
        # lastly puting the item into idx index
        # and increamenting the number of element tracker
        self.A[idx] = item
        self.n += 1
    
    # a magic method its called when del obj[key] is exsicuted
    def __delitem__(self,idx):
        
            # to handle index error
            idx = self.__mange_index(idx)
         
        
            # shifting the values to the left
            for i in range(idx,self.n -1):
                self.A[i] = self.A[i+1]
            
            self.n -= 1 # lastly decreassing the element tracker
            
            
            

    # remove funtion
    def remove(self,item):
        # finding the items index
        idx = self.find(item)
        
        
        # then deleting the element based on index
        if type(idx) == int:
            self.__delitem__(idx)
    
    # extened method        
    def extend(self,other):
        # checking if the index is iterable or not
        iter(other)
        
        #if yes then just adding all the values to the list
        for i in other:
            self.append(i)
    
    # insertion sort              
    def sort(self):
        for i in range(1, self.n):
            key = self.A[i]      # element to insert
            j = i - 1
            while j >= 0 and self.A[j] > key:
                self.A[j + 1] = self.A[j]  # shift element to right
                j -= 1
            self.A[j + 1] = key  # insert key at correct position

               
        
        
            
            
            
        
        
        
        
        


