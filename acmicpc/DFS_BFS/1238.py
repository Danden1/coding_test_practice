import sys
import heapq

n, m, x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    
    graph[a].append([b,c])

inf = 987654321

ans = 0

dist_x = [inf for _ in range(n+1)]
dist_x[x] = 0
q= []
heapq.heappush(q,[0, x])

while q:
    cur_d, cur = heapq.heappop(q)

    if cur_d > dist_x[cur]:
        continue
        
    for nx, nd in graph[cur]:
        now_dist = cur_d + nd
        
        if dist_x[nx] > now_dist:
            dist_x[nx] = now_dist

            heapq.heappush(q, [now_dist, nx])
            
              
              
for i in range(1, n+1):
    dist = [inf for _ in range(n+1)]
    dist[i] = 0
    tmp_ans = inf
    q= []
    heapq.heappush(q,[0, i])
    
    while q:
        cur_d, cur = heapq.heappop(q)

        if cur_d > dist[cur]:
            continue
           
        for nx, nd in graph[cur]:
            now_dist = cur_d + nd
            
            if dist[nx] > now_dist:
                dist[nx] = now_dist

                heapq.heappush(q, [now_dist, nx])
                
                
    ans = max(ans, dist[x]+dist_x[i])
                
print(ans)   
        
