# 페르마의 소정리
# 모듈러 연산
from collections import deque
import sys
sys.setrecursionlimit(10**6)
p = 1000000007

def fac(n):
    ret = 1
    
    for i in range(2, n+1):
        ret = (ret * i) % p
        
    return ret


def div(base, ex):
    if ex == 1:
        return base
    elif ex == 0:
        return 1
    
    ret = div(base, ex // 2)
    
    if ex % 2 == 1:
        return (ret * ret % p) * base % p
    
    
    return ret * ret % p
    



N, K = map(int, sys.stdin.readline().split())

print(fac(N) * div(fac(K) * fac(N-K), p-2) % p)
