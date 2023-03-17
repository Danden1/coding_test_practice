import sys

t = int(sys.stdin.readline())


for _ in range(t):
    n,m,w = map(int, sys.stdin.readline().split())
    
    graph = [ [] for _ in range(n+1)]
    
    for i in range(m):
        a,b,c = map(int, sys.stdin.readline().split())
        graph[a].append([b,c])
        graph[b].append([a,c])
        
    for i in range(w):
        a,b,c = map(int, sys.stdin.readline().split())
        graph[a].append([b,-c])
        
    inf = 987654321
    dist = [inf for _ in range(n+1)]
    dist[1] = 0
    flag = False
    
    for i in range(n):
        for a in range(1, n+1):
            
            for b,c in graph[a]:
                if dist[b] > c+dist[a]:
                    dist[b] = c+dist[a]
                    if i == n-1:
                        flag = True
                        
    if flag:
        print("YES")
    else:
        print("NO")
            
