#https://github.com/nirupamgarai00/DSA.git

# hi its my own max heap class which can be used both as instance and for a spesifict users array via class method
# methods
# instance method - insert[D]
                 # - extract_max[D]
                 # - is_empty[D]
                 # - peak_max[D]
                 # - len [D]
# class method  - sfit_down[D]
                 # - soft_up
                 # - deletion[D] - returns the new size of heap
                 # - bulidheap[D]
                 # heapify[D]
                 # gives_index_of_second_level_last_element[D]   






class Max_heap:
    
    def __init__(self,arr=[],heap_size = -1):
        if heap_size == -1:
            self.__heap_size = len(arr)
        else:
            self.__heap_size = heap_size
        self.__heap = arr
        if self.__heap_size>0:
            Max_heap.__heapify(self.__heap,self.__heap_size)
            
    def __str__(self):
        print(self.__heap[:self.__heap_size])
        return''
            
    # insert funtion
    def insert(self,item):
        self.__heap.insert(self.__heap_size,item)
        Max_heap.__sift_up(self.__heap,self.__heap_size)
        self.__heap_size += 1
    
    # returns the max root of the heap
    def extract_max(self):
        if self.__heap_size<=0:
            raise ValueError('heap is empty')
        
        if self.__heap_size == 1:
            return self.__heap.pop()
        
        self.__heap_size = Max_heap.deletion(self.__heap,self.__heap_size)
        temp = self.__heap.pop()
        
        return temp
    
    def is_empty(self):
        return self.__heap_size == 0    
        
        
    # peak max method
    def peak_max(self):
        if self.__heap_size>0:
            return self.__heap[0]
        else:
            raise ValueError('Heap is empty')
    
    def __len__(self):
        return self.__heap_size
    
    # sifht up oparation
    @classmethod
    def __sift_up(cls,arr,i):
        
        
        while i>0:
            #cal - perent index
            perent = (i-1)//2
            
            # swap if bigger
            if arr[i]>arr[perent]:
                #swap
                arr[i],arr[perent] = arr[perent], arr[i]
                i = perent
            # else break
            else:
                break
            
            
            
        
    
    @classmethod
    def Buildheap(cls,arr):
        Max_heap.__heapify(arr)
    
    # time - wost case - O(logN)
    @classmethod
    def __sift_down(cls,arr,i,heap_size):
        
        while i<heap_size:
            #if the element have both child
            if i*2+2 < heap_size:
                # when both child is larger 
                if arr[i]<arr[i*2+2] and arr[i]<arr[i*2+1]:
                    # if 2nd child larger swap and update
                    if arr[i*2+1]<arr[i*2+2]:
                        arr[i],arr[i*2+2] = arr[i*2+2],arr[i] # swap
                        i = i*2+2 # update
                    
                    # if 1st child larger then swap and update
                    else:
                        arr[i],arr[i*2+1] = arr[i*2+1],arr[i]
                        i = i*2+1
                    
                    
                # if 1st child is bigger swap and update        
                elif arr[i]<arr[i*2+1]:
                    
                    arr[i],arr[i*2+1] = arr[i*2+1],arr[i]
                    i = i*2+1
                #if only second child is bigger 
                elif arr[i]<arr[i*2+2]:
                    arr[i],arr[i*2+2]=arr[i*2+2],arr[i]
                    i = i*2+2
                # if any one is not bigger then break
                else:
                    break
            # in case of only one child 
            # if the child is bigger the swap and break    
            elif i*2+1<heap_size:
                if arr[i]<arr[i*2+1]:
                    arr[i],arr[i*2+1] = arr[i*2+1],arr[i]
                break
            
            #if the child is not bigger then break
            else:
                break
                    
                
    # time - O(logN)            
    @classmethod
    def deletion(cls,arr,heap_size=-1):
        # if size nit given
        if heap_size == -1:
            heap_size = len(arr)
        # delet then return the new heap_size help full for heap sort
        if len(arr)>0:
            arr[0],arr[heap_size-1] = arr[heap_size-1],arr[0]
            Max_heap.__sift_down(arr,0,heap_size-1)
            return heap_size-1
        else:
            raise ValueError('List is empty')
        
                    
                
            
    # time - O(n)
    @classmethod
    def __heapify(cls,arr,heap_size=-1):
        # fi size not given
        if heap_size == -1:
            heap_size = len(arr)
        
        # gives the last index of the 2nd last level based on heap size
        idx = Max_heap.__gives_index_of_second_level_last_element(heap_size)
            
        
        # heapify 
        while idx>=0:
            # left and roght child
            left = idx*2+1
            right =  idx*2+2
            
            # if both child exsist
            if right<heap_size:
                # in case of both are bigger
                if arr[idx]<arr[left] and arr[idx]<arr[right]:
                    #chosing the bigger one and performing swap and _shift_down oparation
                    if arr[left]<arr[right]:
                        arr[idx],arr[right] = arr[right],arr[idx]
                        Max_heap.__sift_down(arr,right,heap_size)
                    elif arr[right]<=arr[left]:# swaps with left child if both are equal
                        arr[idx],arr[left] = arr[left],arr[idx]
                        Max_heap.__sift_down(arr,left,heap_size)
                
                # in case left bigger        
                elif arr[idx]<arr[left]:
                    arr[idx],arr[left] = arr[left],arr[idx]
                    Max_heap.__sift_down(arr,left,heap_size)
                # in case of right child bigger    
                elif arr[idx]<arr[right]:
                    arr[idx],arr[right] = arr[right],arr[idx]
                    Max_heap.__sift_down(arr,right,heap_size)
                    
                    
            # in case of only one child exsist
            elif left<heap_size:
                if arr[idx]<arr[left]:
                    arr[idx],arr[left] = arr[left],arr[idx]        
                        
            # updation            
            idx -= 1
    
            
    # time - O(1)
    @classmethod        
    def __gives_index_of_second_level_last_element(cls,heap_size:int):
        # checking if its nit invalid heap size
        if heap_size<=1:
            return -1
        
        h = heap_size.bit_length() -1 # (gives the bit len of the nummber)  - 1
        
        index =  (1<<h) - 2 # 2*h - 2
        return index
           
    
            
                
            
            
        
            

        
    
    
    
    