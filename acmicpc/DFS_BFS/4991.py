# 도착하면 visited를 reset한느 방법으로 하면 될 듯?
from collections import deque
from itertools import permutations

direction = [[0,1], [0,-1], [1,0], [-1,0]]


while(True):
    C, R = map(int, input().split())
    
    if R==0 and C==0:
        break
    
    board = []
    
    dirty_pos = []
    start_pos = []
    
    
    for i in range(R):
        board.append(list(input()))
        
        for j in range(C):
            if board[i][j] == 'o':
                start_pos.append([i, j])
            elif board[i][j] == '*':
                dirty_pos.append([i,j])
                
    start_pos.extend(dirty_pos)
    

    
    dist = [[0 for _ in range(len(start_pos))] for _ in range(len(start_pos))]
    
    for i in range(len(start_pos)):
        q = deque()
        visited = [[False for _ in range(C)] for _ in range(R)]
        visited[start_pos[i][0]][start_pos[i][1]] = True
        dirty_cnt = len(start_pos) - 1
        q.appendleft([start_pos[i][0], start_pos[i][1], 1])
        
        while q :
            y, x, tmp_dist = q.pop()
            
            for dir_y, dir_x in direction:
                dir_y, dir_x = dir_y + y, dir_x + x
                
                if dir_x < 0 or dir_x >= C or dir_y < 0 or dir_y >= R:
                    continue
                if visited[dir_y][dir_x] or board[dir_y][dir_x] == 'x':
                    continue
        
                if board[dir_y][dir_x] == '*' or board[dir_y][dir_x] == 'o':
                    dirty_cnt -= 1
                    for j in range(len(start_pos)):
                        if start_pos[j][0] == dir_y and start_pos[j][1] == dir_x:
                            dist[i][j] = tmp_dist
                            break
                
                visited[dir_y][dir_x] = True
                q.appendleft([dir_y, dir_x, tmp_dist+1])
                
        if dirty_cnt > 0:
            print(-1)
            break
        
    if dirty_cnt == 0:
        pl = [i for i in range(1, len(start_pos))]
        
        pms = permutations(pl, len(pl))
        
        start = 0        
        ans = 987654321
        
        for i in range(len(start_pos)):
            print(dist[i])

        for pm in pms:
            adist = 0
            start= 0
            for j in pm:
                adist += dist[start][j]
                start = j
            print(adist)
            ans = min(ans, adist)
            
        print(ans)