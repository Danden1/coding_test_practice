import sys

V, E = map(int, sys.stdin.readline().split())

board = [[0 for _ in range(V+1)] for _ in range(V+1)]

floyd = [[0 if i==j else 987654321 for i in range(V+1)] for j in range(V+1)]

for _ in range(E):
    a,b,c =  map(int, sys.stdin.readline().split())
    
    board[a][b] = c
    floyd[a][b] = c
    


ans = 987654321

for i in range(1, V+1):
    for j in range(1, V+1):
        for k in range(1, V+1):
            floyd[j][k] = min(floyd[j][k], floyd[j][i]+floyd[i][k])
            if not j==k:
                ans = min(ans, floyd[j][k] + floyd[k][j])
            
if ans >=987654321:
    print(-1)
else:
    print(ans)
            
    
    
