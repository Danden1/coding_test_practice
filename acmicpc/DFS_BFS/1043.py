import sys


def is_with_truth(graph, i, truths, visited):
    flag = False
    for j in graph[i]:

        if visited[j]:
            continue
        
        if j in truths:
            flag = True
            break
        
        visited[j] = True
        if is_with_truth(graph,j,truths,visited):
            flag = True

    return flag

n, m = map(int,sys.stdin.readline().split())

truths = list(map(int,sys.stdin.readline().split()))
party = []
graph = [set([i]) for i in range(n+1)]

for i in range(m):
    party.append(list(map(int, sys.stdin.readline().split()))[1:])

    for j in range(len(party[i])-1):
        for k in range(j+1, len(party[i])):
            graph[party[i][j]].add(party[i][k])
            graph[party[i][k]].add(party[i][j])

if truths[0] == 0:
    print(m)

else:
    truths = truths[1:]
    ans = 0
    
    for i in range(m):
        flag=False
        for j in range(len(party[i])):
            visited = [False for _ in range(len(graph))]
            
            if is_with_truth(graph, party[i][j], truths, visited):
                flag=True
                break

        if not flag:
            ans+=1
                
        
    print(ans)
