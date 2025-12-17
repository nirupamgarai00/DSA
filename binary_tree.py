#https://github.com/nirupamgarai00/DSA.git

# Hi, this my code to create my own Binary Tree with basic funtionality there will be mixed consept of DSA and OOPS in python
# ======= Binary tree ==================
#len function [D]
# insert[D]
# delet [D]
# Tree builder using pre ord list[D] & also with preorder and inorder combaine[D]
# cal - depth[D]
# cal - level of given data[D]
# traversal - pre ,post , in , level[D]
# convert tree into - preorder,inorder,postorder list[D]
# searching [D]










# using Queue for level traversal
from my_queue import Queue


# node for tree
class Node:
    def __init__(self,data):
       
        self.data = data
        self.left = None
        self.right = None
        
        
class Binary_tree:
    
    _SENTINEL = object()
    
    def __init__(self,arr,order:str='pre'):
        
        
        # a index for adding converthing the list into tree
        self.idx = -1
        self.n = 0# count the len
        
        
        self.root = self.Build_preorder(arr)
    
    
   
    #len of tree
    def __len__(self):
        return self.n
    
    # calculates depth of the tree
    def depth_of_tree(self,root = _SENTINEL):
        # first case  for external call
        if root is self._SENTINEL:
            root = self.root
        
        # end case    
        if root is None:
            return 0
        
        # cal  culating left and right sub tree height
        left_h = self.depth_of_tree(root.left)
        right_h = self.depth_of_tree(root.right)
        
        # returning the max of it and adding it own height
        return max(left_h,right_h)+1
    
    
    # cal culates the height of any given value    
    def level_of_data(self,data):
        # using queue for level ord traversal
        from my_queue import Queue
        q = Queue()
        
        level = 0 # counts level
        
        q.enqueue(self.root)
        q.enqueue(self._SENTINEL)# level marker
        
        while not q.isempty():
            curr = q.dequeue()# pop
            
            # marker of when levels ends
            if curr is self._SENTINEL:
                
                # when data is not found also queue is empty
                if q.isempty():
                    raise ValueError(f'{data} not found')
                # queue is not empty
                else:
                    level += 1
                    q.enqueue(curr)
                    continue
            
            # if data in found
            if curr.data == data:
                return level
            
            
            
            if curr.left is not None:
                q.enqueue(curr.left)
            if curr.right is not None:
                q.enqueue(curr.right)
    
    # searching bye key            
    def search(self,key):
        # using queue for level ord traversal
        from my_queue import Queue
        q = Queue()
        
        level = 1 # counts level
        
        q.enqueue(self.root)
        q.enqueue(self._SENTINEL)# level marker
        
        while not q.isempty():
            curr = q.dequeue()# pop
            
            # marker of when levels ends
            if curr is self._SENTINEL:
                
                # when data is not found also queue is empty
                if q.isempty():
                    raise KeyError(f'your key - {key} not found')
                # queue is not empty
                else:
                    level += 1
                    q.enqueue(curr)
                    continue
            
            # if data in found
            if curr.data == key:
                return curr,level
            
            
            # adding the child of that node
            if curr.left is not None:
                q.enqueue(curr.left)
            if curr.right is not None:
                q.enqueue(curr.right)        
    
    
    def __find_rightmost_node_node_of_heighest_depth(self,root):
        
        
        # using a queue
        q = Queue()
        q.enqueue((root,None))# adding (node, perent)
        
        privous_node = None # storing the previous node
        while not q.isempty():
            
            curr = q.dequeue()
            
            if curr[0].left is not None:
                q.enqueue((curr[0].left,curr[0]))
            if curr[0].right is not None:
                q.enqueue((curr[0].right,curr[0]))
            
            privous_node = curr
            
        
        return privous_node
     
    # helper for insertion gives node of any possible node where data can be insertable        
    def __helper_for_insert(self,root):
        q= Queue()
        q.enqueue(root)
        
        appendable_node = None
        while not q.isempty():
            curr = q.dequeue()
            
            
            if curr.left is not None:
                q.enqueue(curr.left)
            else:
                appendable_node = curr
                break
            if curr.right is not None:
                q.enqueue(curr.right)
            else:
                appendable_node = curr
                break
        
        return appendable_node
    
        
        
        
        
        
        
        
            
    # insertion if any node have None then insert there   
    def insert(self,data):
        # if its empty
        if self.root is None:
            self.root = Node(data)
            return
        
        node = self.__helper_for_insert(self.root)
        
        if node.left is None:
            node.left = Node(data)
        else:
            node.right = Node(data)
            
        
        
                                
        
    def delet(self,key):
        if self.root is None:
            raise ValueError("Binary Tree is empty")
        # gives the last node and its perent node
        last_node,perent = self.__find_rightmost_node_node_of_heighest_depth(self.root)
        # in case tree has on element
        if perent is None:
            if last_node.data == key:
                self.root = None
            
            return
        # searching the node
        node,level = self.search(key)
        
        # swaping the data with last node
        node.data = last_node.data
        
        # removing the last element
        if perent.left is last_node:
                perent.left = None
        else:
            perent.right = None
            
        self.n+=1# increamenting the size
            
        
    
    
        
        
            
    
    # helper of inorder converter
    def __helper_inorder_list(self,curr,arr):
        if curr is None:
            arr.append(-1)
            return
        
        
        self.__helper_inorder_list(curr.left,arr)
        arr.append(curr.data)
        self.__helper_inorder_list(curr.right,arr)
        
        return
    
    # converts the tree into a inorder list
    def to_in_ord_list(self):
        result = []
        self.__helper_inorder_list(self.root,result)
        return result
        
    
    # inorder travers and _sentinel marker for the for first call
    def travers_in(self,curr=_SENTINEL):
        if curr is Binary_tree._SENTINEL:
            curr = self.root
        if curr is None:
            return
        
        self.travers_in(curr.left)
        print(curr.data,end=' ')
        self.travers_in(curr.right)
        
        return
    
    # helper funtion for converting the pre order Tree into List
    def __helper_preorder_list(self,curr,arr):
        if curr is None:
            arr.append(-1)
            return
        arr.append(curr.data)
        self.__helper_preorder_list(curr.left,arr)
        self.__helper_preorder_list(curr.right,arr)
        
        return
    
    # convts the tree into preorder list            
    def to_pre_ord_list(self):
        result = []
        self.__helper_preorder_list(self.root,result)
        return result
        
               
    # preorder traversal and _SENTINEL marker for the for the first call        
    def travers_pre(self,curr = _SENTINEL):
        if curr is Binary_tree._SENTINEL:
            curr = self.root
        
        if curr is None:
            return
        
        print(curr.data,end=' ')
        self.travers_pre(curr.left)
        self.travers_pre(curr.right)
        
        return
        
    #helper of the postorder converter    
    def __helper_postorder_list(self,curr,arr):
        if curr is None:
            arr.append(-1)
            return
        
        
        self.__helper_postorder_list(curr.left,arr)
        self.__helper_postorder_list(curr.right,arr)
        arr.append(curr.data)
    
    # tree to post order list
    def to_post_ord_list(self):
        result = []
        self.__helper_postorder_list(self.root,result)
        return result
    
    
    # postorder traversal        
    def travers_post(self,curr = _SENTINEL):
        if curr is Binary_tree._SENTINEL:
            curr = self.root
            
        if curr is None:
            return
        
        self.travers_post(curr.left)
        self.travers_post(curr.right)
        print(curr.data,end=' ')
        
        return
        
        
                    
        
    # bulding a preorder tree
    def Build_preorder(self,arr):
        # an itarator
        self.idx +=1
        if self.idx>=len(arr):
            return None
        # if value is -1 then return None
        if arr[self.idx] == -1:
            return None
        # creating Node
        new_node = Node(arr[self.idx])
        self.n += 1# updating size
        
        # adding left subtree
        new_node.left = self.Build_preorder(arr)
        # adding right subtree
        new_node.right = self.Build_preorder(arr)
        
        return new_node # returning the root
    @classmethod
    def _helper_for_treeBuilder(cls,pre,in_ord,inord_range:tuple):
        Binary_tree.__idx += 1
        # when idx>len(pre)
        if Binary_tree.__idx>=len(pre):
            return None
        
        # creating new node
        new_node = Node(pre[Binary_tree.__idx])
        
        if new_node.data in in_ord:
            index_of_node_inord = in_ord[new_node.data]
        else:
            cls.__idx = -1
            raise ValueError('inorder list invaild')
        
        
        
        # adding the left subtree
        new_node.left = Binary_tree._helper_for_treeBuilder(pre,in_ord,(inord_range[0],index_of_node_inord))
        # adding the right subtree
        new_node.right = Binary_tree._helper_for_treeBuilder(pre,in_ord,(index_of_node_inord+1,inord_range[1]))
        
        # returning the node
        return new_node
        
    __idx = -1 # using class level idx for traversing the pre ord list
    @classmethod
    def build_tree(cls,pre,in_ord=None):
        # in case of one complet pre ord list
        if in_ord is None:
            temp = Binary_tree(pre)
            return temp.root
        
        # when both pre and in order are given
        else:
            # constract the tree and returns the root
            in_ord_map={}
            for idx,val in enumerate(in_ord):
                in_ord_map[val] = idx
                
            root = Binary_tree._helper_for_treeBuilder(pre,in_ord_map,(0,len(in_ord)))
            Binary_tree.__idx = -1# setting the idx in the intial state
            # returning the root
            return root
        
        
            
     
    # using Queue for the level order traversal    
    # level ord traversal
    def level_ord_travers(self):
            
            q = Queue()

            if self.root is None:
                return

            q.enqueue(self.root)
            q.enqueue(self._SENTINEL)  # level marker

            while not q.isempty():
                curr = q.dequeue()

                if curr is self._SENTINEL:
                    print()  # end of level

                    if not q.isempty():   # if more nodes exist
                        q.enqueue(curr)   # push next level marker
                    continue

                # print current node
                print(curr.data, end=' ')

                # enqueue children ONLY if they exist
                if curr.left is not None:
                    q.enqueue(curr.left)
                if curr.right is not None:
                    q.enqueue(curr.right)

        
    
        
        
        

       
            
            
            
           

               
                 
            
    
    
        
