import heapq
import sys


def djk(board, start):
    inf = 987654321
    dist = [inf for _ in range(len(board))]
    
    hq = []
    dist[start] = 0
    heapq.heappush(hq, [0, start])
    
    while hq:
        cur_dist, cur = heapq.heappop(hq)
        
        if cur_dist > dist[cur]:
            continue
        
        for nx, nx_dist in board[cur]:
            
            if nx_dist + cur_dist < dist[nx]:
                dist[nx] = nx_dist + cur_dist
                heapq.heappush(hq, [dist[nx],nx])

    return dist

n, e = map(int, sys.stdin.readline().split())
board = [[] for _ in range(n+1)]

for i in range(e):
    a,b,c = map(int, sys.stdin.readline().split())
    board[a].append([b,c])
    board[b].append([a,c])

mid1, mid2 = map(int, sys.stdin.readline().split())


inf = 987654321

dist_start = djk(board,1)
dist_mid1 = djk(board, mid1)
dist_mid2 = djk(board, mid2)

ans = min(dist_start[mid1]+dist_mid1[mid2]+dist_mid2[n], dist_start[mid2]+dist_mid2[mid1]+dist_mid1[n])

if ans >= inf:
    print(-1)
else:
    print(ans)

    
    
