import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
board = []

swan_pos = []

q = deque()
next_q = deque()
qq = deque()
next_qq = deque()

flag = True
visited1 = [[False for _ in range(C)] for _ in range(R)]
visited2 = [[False for _ in range(C)] for _ in range(R)]
direction = [[0,1], [0,-1], [1,0], [-1,0]]


            


for i in range(R):
    board.append(list(sys.stdin.readline()))
    
    for j in range(C):
        if board[i][j] == '.':
                q.append((i,j))
                visited1[i][j] = True
        if board[i][j] == 'L':
            swan_pos.append((i,j))
            q.append((i,j))

visited2[swan_pos[0][0]][swan_pos[0][1]] = True
qq.append((swan_pos[0]))


day = 0




while(flag):
    
    while (qq and flag):
        r, c = qq.popleft()
        
        
        for dr, dc in direction:
            move_r, move_c = r + dr, c + dc
            
            if move_r < 0 or move_r >= R or move_c < 0 or move_c >= C:
                continue
            
            if visited2[move_r][move_c] :
                continue
            
            
            
            if board[move_r][move_c] == 'X':
                next_qq.append((move_r, move_c))
            elif move_r == swan_pos[1][0] and move_c == swan_pos[1][1]:
                flag = False
                print(day)
                break
            else:
                qq.append((move_r, move_c))
            visited2[move_r][move_c] = True
    
    
    while (q and flag):
        r, c = q.popleft()

        
        for dr, dc in direction:
            move_r, move_c = r + dr, c + dc
            
            if move_r < 0 or move_r >= R or move_c < 0 or move_c >= C:
                continue
            
            if visited1[move_r][move_c]:
                continue
            
            if board[move_r][move_c] == 'X':
                next_q.append((move_r, move_c))
                board[move_r][move_c] = '.'
            else :
                q.append((move_r, move_c))
                
            visited1[move_r][move_c] = True
               
    
            
    day+=1
    q = next_q
    qq = next_qq
    next_q = deque()
    next_qq = deque()
    
