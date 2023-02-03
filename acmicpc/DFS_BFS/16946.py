import sys
from collections import deque

direction = [[1,0], [0,-1], [-1,0], [0,1]]


def bfs(board, start, r,c, g):
    q = deque()

    cnt = -1
    q.append([start[0], start[1]])
    board[start[0]][start[1]] = g
    
    while q:
        y, x= q.popleft()
        
        for dy, dx in direction:
            ny = y + dy
            nx = x + dx
            
            if ny < 0 or ny >= r or nx < 0 or nx >= c:
                continue
            if  board[ny][nx] == 1 or board[ny][nx] < 0:
                continue
            
            cnt -=1
            q.append([ny,nx])
            board[ny][nx] = g
        
    return g-1, cnt

r, c = map(int, sys.stdin.readline().split())

board = deque()

for i in range(r):

    board.append(list(map(int,list(sys.stdin.readline().strip()))))

dic = {}
g= -1
for i in range(r):
    for j in range(c):
        if board[i][j] == 0:
            tg, cnt = bfs(board,[i,j], r, c, g)
            dic[g] = cnt
            g = tg


for i in range(r):
    for j in range(c):
        cnt = -1
        s = set()
        if board[i][j] == 1:
            for dy, dx in direction:
                ny = i + dy
                nx = j + dx
                if ny < 0 or ny >= r or nx < 0 or nx >= c:
                    continue
                if board[ny][nx] < 0:
                   s.add(board[ny][nx])
        for ss in s:
            board[i][j] -= dic[ss]
                    

for i in board:
    for j in i:
        if j >= 0:
            print(j%10, end='')
        else:
            print(0, end='')
    print()
