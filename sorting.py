#https://github.com/nirupamgarai00/DSA.git
# sorting alogs
# bubble sort
# selecton_sort
# merage sort
#insetion_sort
# quick sort (with random pivot)
# heap sort


# bubble sort( time - O(n*n) worst case, stable, space - O(1))
def bubble_sort(arr):
    
    for i in range(len(arr)-1,0,-1):
        
        for j in range(i):
            
            if arr[j]>arr[j+1]:
                #swaping
                
                arr[j],arr[j+1] = arr[j+1],arr[j]
                
    
    return arr

# selection_sort(time - O(n*n), space - O(1) ) faster then bubble sort but in avarge and worst case but in best case bubble is faster
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_value_index = i
        for j in range(i+1,len(arr)):
            if arr[min_value_index]>arr[j]:
                min_value_index = j
        
        arr[i],arr[min_value_index] = arr[min_value_index],arr[i]
        
    
    return arr


    
# marge sort - time - O(nlongn) space - O(n), Not adaptive , Stable            
def merage_sort(arr):
    
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    
    # deviding all the elemnets
    arr1 = merage_sort(arr[:mid])
    arr2 = merage_sort(arr[mid:])
    
    j_arr1 = 0
    k_arr2 = 0
    # concoruring all the elemnest
    while j_arr1<len(arr1) and k_arr2<len(arr2):
        if arr1[j_arr1]<=arr2[k_arr2]:
            arr[j_arr1+k_arr2] = arr1[j_arr1]
            j_arr1 += 1
        else:
            arr[k_arr2+j_arr1] = arr2[k_arr2]
            k_arr2 += 1
    
    
    # copying arr2 left overs
    while k_arr2 <len(arr2):
        arr[j_arr1+k_arr2]= arr2[k_arr2]
        k_arr2 +=1
            
        
    # copying arr1 left overs
    while j_arr1<len(arr1):
        arr[j_arr1+k_arr2] = arr1[j_arr1]
        j_arr1 += 1
    
    return arr
    
        
# insertion sort - time O(n*n) space - O(1) adavtive -  yes         
def insertion_sort(arr):
    
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        
        while j>= 0 and key<arr[j]:
            
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key
                
    return arr




import random  # randow int generation
# hellper for quicck sort algo time - O(n)
def partition(arr,st,end):
    pivot_indx = random.randint(st,end)
    idx = st
    arr[end],arr[pivot_indx] = arr[pivot_indx],arr[end]
    pivot_indx = end
     
    for i in range(st,end):
        
        if arr[i]<=arr[pivot_indx]:
            arr[idx],arr[i] = arr[i],arr[idx]
            idx += 1
    
    arr[idx],arr[pivot_indx] = arr[pivot_indx],arr[idx]  
    
    return idx  
    
# quick sort algo - time - O(nlogn) space- O(1)       
def quick_sort(arr,st,end):
    if st>=end:
        return
    
    idx = partition(arr,st,end)
    
    
    
    quick_sort(arr,st,idx-1)
    quick_sort(arr,idx+1,end)
    
    
    
from my_heap_class import Max_heap # this data stucture i made it my self
# time - O(nlog) space - O(1)
def heap_sort(arr):
    
    heap_size = len(arr)
    # bulding max heap
    Max_heap.Buildheap(arr)
    
    
    while heap_size>0:
        
        # deleting all elements
        heap_size = Max_heap.deletion(arr,heap_size)# this function returs the current size of heap
    
    
    


        
        
    
    
    
    
    
    
            
            
                
    
    
    



       
