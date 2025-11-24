#https://github.com/nirupamgarai00/DSA.git

from Stack import Stack as st


# reverse String using Stack
def reverse_str(string):
    temp = st()
    result = ''
    
    for i in string:
        temp.push(i)
    while temp.isempty() == False:
        
        t = temp.pop()
        result += t
    return result

# text editor
def text_editor(string,operation):
    u = st() # for undo
    r = st()# for redo
    
    for i in string:
        u.push(i)

    
    for i in operation:
        if i == 'u':
            temp = u.pop()
            r.push(temp)
        else:
            if not r.isempty():
                temp = r.pop()
                u.push(temp)

    result = ''            
    while not u.isempty():
         result = u.pop() + result      
        

    return result





# balenced pernthesis
def balanced_parentheses(string):
    s = st()
    pairs = {')':'(',"}":"{","]":"["}
    for i in string:
        
        if i == '(' or i == '{' or i == '[':
            s.push(i)
        elif i == ')' or i == "}" or i == ']':
            if s.isempty():
                return ' Not balanced'
            temp = s.peak()
            if temp == pairs[i]:
                s.pop()
            else:
                return'str not balanced'
    
    if s.isempty():
        return 'balanced'
    else:
        s.show()
        return 'Not balanced'



# celebrity problem
def celebrity(L):
    s = st()
    for i in range(len(L)):
        s.push(i)
    
    
    while s.size>1:
        a = s.pop()
        b = s.pop()
        
        if L[a][b] == 1:
            s.push(b)
        else:
            s.push(a)
    i = 0
    result = s.pop()
    while i<len(L):
        if result == i:
            i += 1
            continue
        if L[result][i] != 0:
            return 'No celebrity'
        i += 1
    j = 0
    while j<len(L):
        if result == j:
            j += 1
            continue
        
        if L[j][result] != 1:
            return 'No celebrity'
        
        j += 1
    
    return result
        

    
    
            
    

        

