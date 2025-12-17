
#https://github.com/nirupamgarai00/DSA.git

# Hi, this my code to create my own Binary search Tree with basic funtionality there will be mixed consept of DSA and OOPS in python
# ======= Binary Search tree ==================
#len function [D]
# insert[D]
# delet [D]
# build tree[D]
# traversal - inorder[D]
# searching [D]



# node for BST
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    

# BST class
class Binary_Search_Tree:
    
    _SENTINEL = object() # to mange external calls
    def __init__(self,arr=None):
        
        self.n = 0 # counter of element
        self.root = None # stores the root node
        if arr is None:
            return
        self.build_tree(arr)# building BST
    
    def build_tree(self,arr):
        # case of empty tree
        if len(arr) == 0:
            return
        # else creating BST with the list 
        for i in arr:
            self.insert(i)
    
    # len funtion 'len(BST)'
    def __len__(self):
        return self.n 
       
    def search(self,key,root = _SENTINEL):
        # to mange first call and empty tree case
        if root is self._SENTINEL:
           root = self.root
           if root is None:
               raise ValueError("BST is empty")
        
        # key not found case
        if root == None:
            raise KeyError(F'Key - "{key}" not found')
        # key == data
        if root.data == key:
            return root
        
        # cuting the tree based on the key and data
        elif key<root.data:
            self.search(key,root.left)
        else:
            self.search(key,root.right)
        
    
    def _find_in_ord_successor(self,root): #left most Node in the tree
        # if None then returning the node
        if root.left is None:
            return root
        # else recursion for finding the last left Node
        return self._find_in_ord_successor(root.left)
    
    # delet by key    
    def delet(self,key,root = _SENTINEL):
        
        # to mange first call and also empty tree case
        if root is self._SENTINEL:
            root = self.root
            if root is None:
                raise ValueError('BST is empty')
        
        # if root is None key not found
        if root is None:
            raise KeyError(f'Key -"{key} not found"')
        
        # searching the key
        if key<root.data:
           root.left = self.delet(key,root.left)
        elif key>root.data:
            root.right = self.delet(key,root.right)
        
        # deletion logic
        else:
            self.n -= 1 # decreamenting the list
            # zero child
            if root.left is None and root.right is None:
                return None
            # one child
            elif root.left is None:
                return root.right
            # one child
            elif root.right is None:
                return root.left
            
            # two child case
            else:
                # finding the inord successor
                inord_successor = self._find_in_ord_successor(root.right)
                # swaping the value
                root.data,inord_successor.data = inord_successor.data,root.data
                
                # lastly deleting the successot Node
                root.right = self.delet(key,root.right)
            
                
        # returning the node      
        return root
     
    
    # romve method    
    def remove(self,key):
        # storing the node 
        temp = self.search(key)  
        # deleting the node
        self.delet(key)
        return temp# returning the node
        
            
            
                  
    
    
    # insert values in the tree and using SENTINEL for first call  - time - O(logN)  
    def insert(self,data,root=_SENTINEL):
        # if 1st call making root as main root
        if root is self._SENTINEL:
            root = self.root 
            
        # if main root is empty then seting self.root = Node(data)(enters only if the tree is empty)    
        if root is None:
            self.root = Node(data)
            self.n += 1
            return 
        
        # if data is smaller
        if data<root.data:
            # if left have empty slot
            if root.left is None:
                root.left = Node(data)
                self.n +=1
                return
            
            # if dont have empty slot
            else:
                self.insert(data,root.left)
        
        # when data is bigger then root
        else:
            # if left have empty slot
            if root.right is None:
                root.right= Node(data)
                self.n +=1
                return
            # if dont have empty slot
            else:
                self.insert(data,root.right)
                

    # travers inorder (magic - returs a fully sorted data)            
    def travers_inord(self,root = _SENTINEL):
        if root is self._SENTINEL:
            root = self.root
        
        if root is None:
            return
        
        # calling for left
        self.travers_inord(root.left)
        
        print(root.data,end=' ') # printing the current value
        
        # calling for the right
        self.travers_inord(root.right)
                        
        
        