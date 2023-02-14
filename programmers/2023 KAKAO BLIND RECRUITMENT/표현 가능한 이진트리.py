from collections import deque
import itertools
import math

flag = True

def solution(numbers):
    answer = []
    
    for i in numbers:
        if i == 1:
            answer.append(1)
        else:
            an = ans(dec_to_bin(i))
            if an == -1:
                an =0
            answer.append(an)
    
    return answer


def dec_to_bin(number):
    ret = deque()
    while number!= 1:
        ret.appendleft(number%2)
        number = number // 2
        
    ret.appendleft(1)
    
    n = int(math.log2(len(ret))) + 1
    
    while 2**n-1 != len(ret):
        ret.appendleft(0)

    
    return ret

def ans(number):
    n = int(math.log2(len(number)))
    mid = len(number)//2

    return search(mid, number, n)


def search(idx, number, level):
    if (idx+1)%2 == 1:
        return number[idx]
    
    left = idx - 2**(level-1)
    right = idx + 2**(level-1)
    
    
    l = search(left, number, level-1)
    r = search(right, number, level-1)
    
    if l == -1 or r == -1:
        return -1

    if number[idx] == 0:
        if l == 0 and r == 0:
            return 0
        else:
             return -1

    else:
        return  1
