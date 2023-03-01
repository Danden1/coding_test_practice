import sys
from collections import deque


tiles = deque()


N = int(sys.stdin.readline())
k = -1

graph = [deque() for _ in range(N*N - N//2)]

for i in range(N):
    if i % 2 == 1:
        m = N-1
    else:
        m = N

    for j in range(m):
        k+=1
        tiles.append(list(map(int, sys.stdin.readline().split())))
        
        if j == 0:
            continue
        
        if tiles[k-1][1] == tiles[k][0]:
            graph[k].append(k-1)
            graph[k-1].append(k)
        
        

for i in range(1,N//2+1):
    idx = i * N + (i-1) * (N-1)
    
    for j in range(N-1):
        if tiles[j+idx][0] == tiles[j+idx - N][1]:
            graph[j+idx].append(j+idx-N)
            graph[j+idx-N].append(j+idx)
            
        if tiles[j+idx][1] == tiles[j+idx - N+1][0]:
            graph[j+idx].append(j+idx-N+1)
            graph[j+idx-N+1].append(j+idx)
            
        if j+idx+N >= N*N - N//2:
            continue
        
        if tiles[j+idx][0] == tiles[j+idx+N-1][1]:
            graph[j+idx].append(j+idx+N-1)
            graph[j+idx+N-1].append(j+idx)
        
        if tiles[j+idx][1] == tiles[j+idx+N][0]:
            graph[j+idx].append(j+idx+N)
            graph[j+idx+N].append(j+idx)
            
            

q = deque()

max_val = -1
ans = []

visited = [-1 for _ in range(N*N - N //2)]


q.append(0)
visited[0] = 0

while q:
    cur_node= q.popleft()

    
    if max_val < cur_node:
        max_val = cur_node
    

    for nx_node in graph[cur_node]:
        
        if visited[nx_node] >= 0:
            continue
        
        q.append(nx_node)
        visited[nx_node] = cur_node
        

ans = deque()

if max_val == -1:
    print(1)
    print(1)
    
else:

    while max_val != 0:
        ans.appendleft(max_val+1)
        max_val = visited[max_val]
    ans.appendleft(1)

    print(len(ans))
    print(' '.join(list(map(str,ans))))
