import heapq
import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

board = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    
    board[a].append((b,c))
    
start, end = map(int, sys.stdin.readline().split())
    

hq = []

heapq.heappush(hq, (0, start))

dk = [[987654321, -1] for _ in range(n+1)]
dk[start][0] = 0
dk[start][1] = start

while hq:
    dst, cur_node = heapq.heappop(hq)

    if dk[cur_node][0] < dst:
        continue
    
    for nx_node, nx_d in board[cur_node]:
        nx_dst = nx_d + dst
        
        if dk[nx_node][0] > nx_dst:
            dk[nx_node][0] = nx_dst
            dk[nx_node][1] = cur_node
            
            
            heapq.heappush(hq, (nx_dst, nx_node))
        

cur = end



ans = deque()

while cur!=start:
    ans.appendleft(cur)
    cur=dk[cur][1]

ans.appendleft(start)

print(dk[end][0])
print(len(ans))
print(' '.join(map(str, ans)))
