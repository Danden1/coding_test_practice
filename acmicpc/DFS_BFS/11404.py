import heapq
import sys


def bfs(city, start, n):
    dst = [987654321 for _ in range(n+1)]
    dst[start] = 0
    
    hq = []
    heapq.heappush(hq, (0, start))
    
    while hq:
        prev_dst, node = heapq.heappop(hq)
        
        if prev_dst > dst[node]:
            continue
        
        for next_node, next_dst in city[node]:
            now_dst = next_dst + dst[node]
            
            if now_dst < dst[next_node]:
                dst[next_node] = now_dst
                heapq.heappush(hq, (now_dst, next_node))
                
    for i in range(n+1):
        if dst[i] == 987654321:
            dst[i] = 0
    
    return dst

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

city = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    
    city[a].append([b,c])
    
    
for i in range(1, n+1):
    print(' '.join(list(map(str, bfs(city, i, n)[1:]))))
