#https://github.com/nirupamgarai00/DSA.git

# Hi, this my code to create my own Dictionary(its a haibrid Hastable of both chaning and probing) there will be mixed consept of DSA and OOPS in python
# =======dynamic array==================
#len function [D]
# append [D]
# print[D]
# find [D]
# insert [D]
# delete [D]


# a Node class for chaning
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class Dict:
    
    _deleted = object() # this is tombstone code used as a marker for the deleted indext
    
    # Constractor
    def __init__(self,size = -1,probing_or_chaning = False,linear_or_quadratic = False):
        self._colision_manager = probing_or_chaning #(False for probing and True for chaning)
        self.n = 0 # its the counter which counts the element in the Dict
        
        # if its probing then i only need those
        if self._colision_manager is False:
            # dynamic size
            if size == -1:
                self.slots = [None]*8 # store keys
                self.values = [None]*8 # store values
                self.size = 8
                self.fix_size = False # False means the size is Dynamic
            
            # fixed size
            else:
                self.size = size
                
                self.fix_size = True # marker for fixed and Dynamic size(if its True then size is fixed)  
                            
                self.slots = [None]*size # store keys
                self.values = [None]*size # store values  
                          
            self._prob_tech = linear_or_quadratic # (false for linear and True for Quadratic)
            
            
        else:
            self.slots = [None]*8
            self.size = 8
            self.load_factor = 2 # load factor for chaning
            
        
        
        
        
        
    def __iter__(self):
        
        # for chaning
        if self._colision_manager:
            for i in self.slots:
                if i is not None:
                    j = i
                    while j is not None:
                        yield j.key
                        j.next
                    
                
        # for probing
        else:
            for key in self.slots:
                if key is not None and key is not Dict._deleted:
                    yield key
            
    
    # this magic method is called when obj[key] is used
    def __getitem__(self,key):
        
        hash_value = self.hashing(key) # storing the index
        # home index is None
        if self.slots[hash_value] is None:
            raise KeyError(f'{key} not found')
        
        # home case for probing
        if self.slots[hash_value] == key:
            return self.values[hash_value]
        
        # else probing method
        elif self._colision_manager is False:
            # loop for searching key
            for i in range(1,self.size):
                
                new_hash = self.rehash(hash_value,i) # calculating new_hash value
                # found the key
                if self.slots[new_hash] == key:
                    return self.values[new_hash]
                
                # if None is appear then there is no more keys
                elif self.slots[new_hash] is None:
                    raise KeyError(f'{key} not found')
            
            # if loop is compelet and haven't found the key , then key is not found
            raise KeyError(f'{key} not found')
        # chaning method
        else:
            
            
            i = self.slots[hash_value]
            
            while i is not None:
                # if key is found
                if i.key == key:

                    

                    return i.value
                        
                i = i.next
                
            # if key is not found
            raise KeyError(f'{key} not found')            
                
    
    def __delitem__(self,key):
        # calculets has vlaue
        hash_value = self.hashing(key)
        
        # if the home case is empty
        if self.slots[hash_value] is None:
            raise KeyError(f'{key} not found')
        
        # home case for probing
        if self.slots[hash_value]== key:
            # deleting the key and value and returning the value
            self.slots[hash_value] = Dict._deleted
            temp = self.values[hash_value]
            self.values[hash_value] = None
            
            self.n -= 1 # len decreamenting
            
            return temp
        
        # probing case 
        elif self._colision_manager is False:
            # for searching the key
            for i in range(1,self.size):
                # calculating the new hash value
                new_hash = self.rehash(hash_value,i)
                
                # key found
                if self.slots[new_hash] == key:
                    # deleting the key and value and return the value
                    self.slots[new_hash] = Dict._deleted
                    temp = self.values[new_hash]
                    self.values[new_hash] = None
                    self.n -= 1 # len decreamenting
                    return temp
                    
                # key not found
                elif self.slots[new_hash] is None:
                    raise KeyError(f'{key} not found')
                
            # after loop if stil key not found
            raise KeyError(f'{key} not found')
        
        # chaning case
        else:
            # home case
            if self.slots[hash_value].key == key:
                # it has only one element
                if self.slots[hash_value].next is None:
                   temp = self.slots[hash_value].value
                   self.slots[hash_value] = None
                   
                   
                
                # if there are many elements
                else:
                    temp = self.slots[hash_value].value
                    self.slots[hash_value] = self.slots[hash_value].next
                    
                
                self.n -= 1 # len decreamenting
                
                return temp
                 
            # normal case
            i = self.slots[hash_value]
            
            
            while i is not None and i.next is not None:
                # found the key
                if i.next.key == key:
                    
                    temp = i.next.value
                    i.next = i.next.next
                    
                    
                    self.n -= 1 # len decreamenting
                    return temp
                # incrementor        
                i = i.next
                
                
            # key not found
            raise KeyError(f'{key} not found')
             
                
                
    
    # this magic method is called when obj[key] = value is exicuted
    def __setitem__(self,key,value):
        
        hash_value = self.hashing(key) # stroing the index (where is the key)
        
        # in case home slot
        if self.slots[hash_value] is None or self.slots[hash_value] is Dict._deleted:
            # for chaning
            if self._colision_manager:
                self.slots[hash_value] = Node(key,value)
                
                self.n += 1 # len increament
                return
            # for probing
            self.slots[hash_value] = key
            self.values[hash_value] = value
            self.n += 1 # len increament
            
        
        # home case updation for probing
        elif self.slots[hash_value] == key:
            
            # for probing
            self.values[hash_value] = value
        
        # probing 
        elif  self._colision_manager is False:
                
            for i in range(1,self.size):
                # calculating new hash value
                new_hash = self.rehash(hash_value,i)
                
                checker = self.slots[new_hash]
                # in case of updation  
                if checker == key:
                    self.values[new_hash] = value
                    return
                # in case of insertion  
                elif checker is None or checker is Dict._deleted:
                    self.slots[new_hash] = key
                    self.values[new_hash] = value
                    self.n += 1 # len increament
                    return
            
            # if size is fixed    
            if self.fix_size is True:
                raise ValueError('Dictionary is full')
            
            # if size is not given
            else:
                self.resize(key,value)
                
                
                
        # chaning
        else:
            # intilizing the slots and values
            temp1 = self.slots[hash_value]
            
            
            # adding the counter for checking the load factor
            
            # searching the Node
            while temp1 != None:
                
                # in case of updation
                if temp1.key == key:
                    temp1.value = value
                    return
                
                #insertion case
                elif temp1.next is None:
                    
                    # the load factor does not go higher then counter
                    if (self.n/self.size)<self.load_factor:
                        temp1.next = Node(key,value)
                        self.n += 1 # len increament
                        
                    # else doing the resize the Dict
                    else:
                        self.resize(key,value)
                    
                    
                        
                    return
                        
                
                
    
    # returns only the keys            
    def keys(self):
        result = []# empty List
        # probing case
        if self._colision_manager is False:
            # loop for adding all the items in the list 
            for i in range(len(self.slots)):
                if self.slots[i] is not None and self.slots[i] is not Dict._deleted:
                    result.append(self.slots[i])
            
            return result
        # chaning case
        else:
            # loop
            for i in self.slots:
                
                if i is not None :

                        # adding all the keys in the list
                        j = i
                        
                        while j is not None:
                            
                            result.append(j.key)
                            j = j.next
                
                            
                
            # returning the list
            return result
    
    # returns only values
    def get_value(self):
        result = [] # empty List
        # probing case
        if self._colision_manager is False:
            for i in self.values:
                if i is not None :
                    result.append(i)
            
            return result
        # chaning case
        else:
            for i in self.slots:
                # if there is not an empty slots
                if i is not None :
                    
                    
                    j = i
                    # adding all the values into the List    
                    while j is not None:
                            
                        result.append(j.value)
                        j = j.next
            
            return result                         
    
    # returns the a list of tuples (key , values)                    
    def items(self):
        result = [] # empty list
        # chaning case
        if self._colision_manager:
            
            for i in range(len(self.slots)):
                if self.slots[i] is not None:
                    
                    temp1 = self.slots[i]
                    
                    while temp1 is not None:
                        # adding as a tuple
                        result.append((temp1.key,temp1.value))
                        
                        # updating
                        temp1 = temp1.next
                        
        
                            
                        
                        
        else:
            
            for i in range(len(self.slots)):
                # adding
                if self.slots[i] is not None and self.slots[i] is not Dict._deleted:
                    result.append((self.slots[i],self.values[i]))
        
        return result
        
                    
    # resize funtion        
    def resize(self,key,value):
        
        new_size = self.size*2 # making the size double
        
        items = self.items() # retreving all values
        
        # probing case
        if self._colision_manager is False:
           
           # creating the new Dict Dict with same lags and new size
           new_dict = Dict(new_size,linear_or_quadratic= self._prob_tech)   
           
       # chaning
        else:
            # creating the new Dict Dict with same lags and new size
            new_dict = Dict(new_size,True)
            
        # adding the keys and values
        for i in range(len(items)):
            new_dict[items[i][0]] = items[i][1]
            
        new_dict[key] = value # seting the last value
        
            
        # making the self as new_dict        
        self.slots = new_dict.slots
        if self._colision_manager is False:
            self.values = new_dict.values
        self.size = new_dict.size
        self.n = new_dict.n

                
            
    # print            
    def __str__(self):
        results = ''
        # chaning
        if self._colision_manager:
            for i in range(len(self.slots)):
                if self.slots[i] is not None:
                    j = self.slots[i]
                    
                    while j is not None:
                        results += str(j.key)+':'+str(j.value)+ ' , '

                        j = j.next
                        
        # probing                
        else:
            for i in range(len(self.slots)):
                if self.slots[i] is not None and self.slots[i] is not Dict._deleted:
                    results += str(self.slots[i])+':'+str(self.values[i])+' , '
            
        if self.n == 0:
            return "{ }"
        return '{ '+results[:-3]+' }'
                
    # len method                       
    def __len__(self):
        return self.n
                
                
                
    # this to calculate hash value based on probing and key            
    def rehash(self,hash_value,iter):
        # linear probing
        if self._prob_tech == False:
 
            return (hash_value + iter)%self.size
        
        # quadratic probing
        else:
            return (hash_value + iter**2)%self.size
           
                
    # calculates hash value based on key
    def hashing(self,key):
      
            return abs(hash(key)) %self.size

            
    
                 
    

        
