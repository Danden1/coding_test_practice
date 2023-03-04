from collections import deque

def solution(p):
    answer = ''
    
    if is_right(p):
        return p
    
    u,v = parsing(p)
    return recur(u,v)




def recur(u, v):
    if u == "":
        return ""
    
    u2, v2 = parsing(v)
    
    
    if is_right(u):
        ret = u + recur(u2,v2)
    
    else:
        ret = recur(u2,v2)

        ret2 = ''
        for i in range(len(u)):
            if u[i] ==')':
                ret2 = ret2 + '('
            else:
                ret2 = ret2 + ')'

        ret = '(' + ret +')' + ret2[1:-1]

    return ret
        
        
    
def parsing(s):
    if len(s) == 0:
        return "",""
    
    for i in range(len(s)):
        if is_balanced(s[:i+1]):
            return s[:i+1], s[i+1:]
        
    # error
    return False
    
    
def is_right(s):
    q = deque()
    
    for i in range(len(s)):
        if s[i] == '(':
            q.append('(')
        
        elif s[i] == ')':
            if len(q) == 0:
                return False
            
            if q.popleft() == ")":
                return False
    
    return len(q) == 0

def is_balanced(s):
    a, b = 0,0
    
    for i in range(len(s)):
        if s[i] == '(':
            a += 1
        else:
            b += 1
            
    return a==b