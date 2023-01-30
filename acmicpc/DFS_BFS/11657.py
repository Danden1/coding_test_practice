import sys
from collections import deque


def bellman_ford(start, bus, N):
    dst = [sys.maxsize for _ in range(N+1)]
    dst[start] = 0
        
    for i in range(N):
        q = deque()
        q.append(start)
        visited = [False for _ in range(N+1)]
        visited[start] = True
        
        while q:
            s = q.popleft()
            for b,c in bus[s]:

                if dst[s]+c < dst[b]:

                    if i == N-1:
                        return (False, dst)
                    
                    dst[b] = dst[s] + c
                    
                if not visited[b]:
                    q.append(b)
                    visited[b] = True
                
    return (True, dst)   
    

N, M = map(int, sys.stdin.readline().split())

bus = [[] for _ in range(N + 1)] #

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    
    bus[a].append([b,c])
    
flag, dst = bellman_ford(1, bus, N)

if N == 1:
    print()
elif flag:
    for i in range(2,N+1):
        if dst[i] == sys.maxsize:
            print(-1)
        else:
            print(dst[i])
else:
    print(-1)

    
