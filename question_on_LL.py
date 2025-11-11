from Single_LinkedList import LinkedList as LL




# find the max value in the LL and replace it with given value
def replace_max(L,value):
    temp = max(L)
    i,t = L.find(temp)
    t.data = value

# replace_max(a,'hello')
# print(a)

# find the sum of all elements which is at the odd position
def sum_of_odd(L):
    
    sum = 0
    for i in range(1,len(L),2):
        sum += L[i]
    return sum

# print(sum_of_odd(a))

# linked list revere
def revers(L,curr,prev= None,):
    # with recursion technique
    # end case
    if( curr.next == None):
        curr.next = prev
        L.tail = L.head
        L.tail.next = None
        L.head = curr
        
        return
    
    # normal cases
    revers(L,curr.next,curr)
    curr.next = prev
    
    
    '''
    # with loop
    while curr != None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    L.tail = L.head
    L.tail.next = None
    L.head = prev
    
    '''
    
# in a LL replace a space in '*' or '/' have came and if two came 
# one after anther replace with a single space and turn 
# the next later to upper case case
def char_to_sentence(L):
    prev = False
    result = ''
    temp = L.head
    while temp != None:
        if temp.data == '*' or temp.data == '/':
            if (prev == True):
                result += temp.next.data.upper()
                temp = temp.next
                prev = False
            else:
                result += ' '
                prev = True
            
        
        else:
            result += temp.data
            prev = False

        temp = temp.next
    return result
            
        
        


l = LL()
l.append('A')
l.append('n')
l.append('*')
l.append('/')
l.append('a')
l.append('p')
l.append('p')
l.append('l')
l.append('e')
l.append('*')
l.append('a')
l.append('/')
l.append('d')
l.append('a')
l.append('y')
l.append('*')
l.append('*')
l.append('k')
l.append('e')
l.append('e')
l.append('p')
l.append('s')
l.append('/')
l.append('*')
l.append('a')
l.append('/')
l.append('/')
l.append('d')
l.append('o')
l.append('c')
l.append('t')
l.append('o')
l.append('r')
l.append('*')
l.append('A')
l.append('w')
l.append('a')
l.append('y')

print(char_to_sentence(l))

    
