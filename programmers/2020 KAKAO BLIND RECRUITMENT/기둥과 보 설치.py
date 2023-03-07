from collections import deque

def solution(n, build_frame):
    answer = []
    board = [[ [] for _ in range(n+1)] for _ in range(n+1)]
    
    for x,y,a,b in build_frame:
        if b == 0:
            delete(board, x, y, a)
        else:
            install(board, x, y, a)
    
    for j in range(n+1):
        for i in range(n+1):
            if len(board[i][j]) == 2:
                answer.append([j,i,0])
                answer.append([j,i,1])
            
            elif len(board[i][j]) == 1:
                answer.append([j,i,board[i][j][0]])
            
    
    
    return answer


def install(board, x, y, a):
    if y == 0:  #보는 바닥에 올 수 없음.
        board[y][x].append(a)
        return
    
    flag = False
    
    if a == 0:  # 기둥
        direction = [[-1,0], [0,-1], [0,0]]
        
        for i in board[y][x]:
            if i == 1:
                flag = True
                break
        
        for i in range(len(direction)):
            ny, nx = direction[i][0] + y, direction[i][1] + x

            if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board):
                continue
            
            if i == 0:
                if 0 in board[ny][nx]:
                    flag = True
                    break
            else:
                if 1 in board[ny][nx]:
                    flag = True
                    break   
    
    else:
        direction1 = [[-1,0],[-1, 1]] # 기둥
        direction2 = [[0,-1], [0,1]] 
        
        for dy, dx in direction1:
            ny, nx = dy + y, dx + x

            if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board):
                continue
            
            if 0 in board[ny][nx]:
                flag=True
                break
                
        cnt = 0
        for dy, dx in direction2:
            ny, nx = dy+y, dx+x
            
            if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board):
                continue
            
            if 1 in board[ny][nx]:
                cnt+=1
            
        if cnt == 2:
            flag = True
    
    if flag:
        board[y][x].append(a)
        

def delete(board, xx, yy, aa):
    q = deque()
    visited = [[False for _ in range(len(board))] for _ in range(len(board))]
    direction = [[[-1,0, 0],[0,-1, 1],[0,0,1]], 
                 [[-1,0,0], [-1,1,0],[0,-1,1],[0,1,1]]]
    
    direction2 = [[1,0],[-1,0],[0,-1],[0,1],[0,0],[1,1],[1,-1],[-1,1],[-1,-1]]
    
    board[yy][xx].remove(aa)                
    q.append([xx,yy,aa])
    
    
    
    
    while q:
        x, y, a = q.popleft()
        
        flag = True
        cnt = 0
        for dy, dx, da in direction[a]:
            ny, nx = y + dy, x + dx
            
            if a == 0 and y == 0:
                flag=False
                break
            
            if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board):
                continue
        
            if a == 1 and da == 1 and da in board[ny][nx]:
                cnt += 1
                if cnt == 2:
                    flag = False
                    break
            
            elif da in board[ny][nx]:
                flag = False
                break
                
        
        if flag:
            board[yy][xx].append(aa) 
            return
        
        for dy, dx in direction2:
            ny, nx = y + dy, x + dx
            
            if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board):
                continue
                
            if visited[ny][nx]:
                continue
            
            for na in board[ny][nx]:
                q.append([nx,ny,na])
                visited[ny][nx] = True
    
    