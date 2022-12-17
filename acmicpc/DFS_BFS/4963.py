import sys
sys.setrecursionlimit(10**6)

def dfs(y,x):
    global board
    global visited
    global direction


    for add_y, add_x in direction:
        next_y, next_x = y + add_y, x + add_x
        
        if next_y < 0 or next_y >= h or next_x < 0 or next_x >= w:
            continue
        
        if visited[next_y][next_x] == 1:
            continue
        
        if board[next_y][next_x] == 0:
            continue
        
        visited[next_y][next_x] = 1
        
        dfs(next_y,next_x)

while True:
    w,h = map(int, input().split())
    
    if w ==0 and h == 0:
        break
    
    board = []
    for i in range(h):
        board.append(list(map(int, input().split())))
    visited = [[0 for i in range(w)] for j in range(h)]
    count = 0
    direction = [(1,1), (1,-1), (-1,1), (-1,-1), (0,1), (0, -1), (1, 0), (-1,0)]
    
    land_idx = []
    
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                land_idx.append((i,j))
                
    for i,j in land_idx:

        if visited[i][j] == 1:
            continue


        visited[i][j] = 1
 
        dfs(i,j)
        count+=1
        
    print(count)