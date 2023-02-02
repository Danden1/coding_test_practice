import sys
from collections import deque

N = 8

direction = [[0,0],[1,0], [0,1], [-1,0], [0,-1], [1,1], [1,-1], [-1,-1], [-1,1]]
wall_pos = []

board = []

for i in range(N):
    board.append(list(sys.stdin.readline()))
    
    for j in range(N):
        if board[i][j] == '#':
            wall_pos.append([i,j])
            

boards = [board]
wall_cnt = len(wall_pos)
for i in range(1,8):
    boards.append([['.' for _ in range(N)] for _ in range(N)])
    
    for j in range(wall_cnt):
        wall_pos[j][0] += 1
        
        if wall_pos[j][0] < N:
            boards[i][wall_pos[j][0]][wall_pos[j][1]] = '#'

hq  = deque()
hq.append([N-1, 0, 0])
visited = [[[False for _ in range(N)] for _ in range(N)] for _ in range(N)]

visited[0][N-1][0] = True

flag = False

while hq:
    y, x, time = hq.popleft()
    
    if time == 8:
        flag = True
        break
    
    if boards[time][y][x] == '#':
        continue
    
    
    
    for dy, dx in direction:
        ny = dy+y
        nx = dx+x
        
        if ny >= N or ny < 0 or nx >= N or nx < 0:
            continue
            
        if visited[time][ny][nx] and not(ny==y and nx ==x):
            continue
        
        if boards[time][ny][nx] == '.':
            visited[time][ny][nx] = True
            hq.append([ny,nx,time+1])
    
if flag:
    print(1)
else:
    print(0)
