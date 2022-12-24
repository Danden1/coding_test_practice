import heapq


def dij(razer_pos, board, r, c):
    
    hq = []
    
    direction = {}
    direction['up'] = {'up':(1,0), 'left':(0,-1), 'right' : (0,1)}
    direction['down'] = {'down':(-1,0), 'left':(0,-1), 'right' : (0,1)}
    direction['left'] = {'left' : (0,-1), 'up': (1,0), 'down' :(-1,0)}
    direction['right'] = {'right' : (0,1), 'up': (1,0), 'down' :(-1,0)}
    
    board_dist = [[100001 for _ in range(C)] for _ in range(R)]
    
    heapq.heappush(hq, (0, (razer_pos[0], 'up')))
    heapq.heappush(hq, (0, (razer_pos[0], 'down')))
    heapq.heappush(hq, (0, (razer_pos[0], 'left')))
    heapq.heappush(hq, (0, (razer_pos[0], 'right')))

    while hq:
        dist, prev = heapq.heappop(hq)
        
        pos, prev_dir = prev
        y, x = pos
        
        if y == razer_pos[1][0] and x == razer_pos[1][1]:
            print(dist)
            break
        
        if dist > board_dist[y][x]:
            continue
        
        for key, val in direction[prev_dir].items():
            dir_y, dir_x = val
            dir_y, dir_x = dir_y + y, dir_x + x
            
            if dir_y >= r or dir_y < 0 or dir_x >= c or dir_x < 0:
                continue
            
            if board[dir_y][dir_x] != '*' :

                now_dist = 0
                
                if key != prev_dir:
                    now_dist += 1
                    
                if dist + now_dist <= board_dist[dir_y][dir_x]:
                    heapq.heappush(hq, (dist+now_dist, ((dir_y,dir_x),key)))
                    board_dist[dir_y][dir_x] = dist+now_dist
                    

C, R = map(int, input().split())

board = []

razer_pos = []

for i in range(R):
    board.append(list(input()))
    
    for j in range(C):
        if board[i][j] == 'C':
            razer_pos.append((i,j))
            




dij(razer_pos, board, R, C)
        
                

                
            
            

        