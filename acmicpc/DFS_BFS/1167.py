import sys
sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline())
ans = 0
end = -1

def dfs(cur, dist, graph, visited):
    global ans
    global end

    if dist > ans:
        ans = dist
        end = cur
    visited[cur]= True   
    for next_node, now_dist in graph[cur]:
        if visited[next_node]:
            continue
        
        
        dfs(next_node, now_dist + dist, graph, visited)


# node, dist
graph = [[] for _ in range(n+1)]

for _ in range(n):
    arr = list(map(int,sys.stdin.readline().split()))
    i = 1
    
    start = arr[0]
    while arr[i] != -1:
        graph[start].append([arr[i], arr[i+1]])
        
        i+=2
        
visited = [False for _ in range(n+1)]

dfs(1, 0, graph, visited)

visited = [False for _ in range(n+1)]
ans = 0
dfs(end, 0, graph, visited)
print(ans)
