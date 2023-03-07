from collections import deque

def solution(board):
    return bfs(board)


def is_out(y1,x1,y2,x2, n):
    if y1 < 0 or y1 >= n or y2 < 0 or y2 >= n or x1 < 0 or x1 >= n or x2 < 0 or x2 >= n:
        return True
    return False


def bfs(board):    
    vertical_squares = [[0,-1], [0,1]]
    horizontal_squares = [[-1,0], [1,0]]
    
    visited = set()
    
    q =deque()
    q.append([((0,0), (0,1)),0])
    
    visited.add(((0,0), (0,1)))
    
    while q:
        p,t= q.popleft()
        for y,x in p:
            if y==len(board)-1 and x == len(board)-1:
                return t
        
        #가로
        if p[0][0] == p[1][0]:
            for dy, dx in horizontal_squares:
                ny1, nx1, ny2, nx2 = p[0][0]+dy, p[0][1]+dx, p[1][0]+dy, p[1][1]+dx
                
                if is_out(ny1,nx2,ny2,nx2,len(board)):
                    continue
                    
                if board[ny1][nx1] == 1 or board[ny2][nx2] == 1:
                    continue
                
                npos = [[ny1, nx1], [ny2, nx2]]
                
                for i in range(2):
                    robot_pos = [[p[i][0], p[i][1]], [npos[i][0] ,  npos[i][1]]]
                    robot_pos.sort(key= lambda x : (x[0], x[1]))
                    
                    robot_pos = (tuple(robot_pos[0]), tuple(robot_pos[1]))
                    if robot_pos in visited:
                        continue
                    
                    visited.add(robot_pos)
                    q.append([robot_pos, t+1])
        #세로
        else:
            for dy, dx in vertical_squares:
                ny1, nx1, ny2, nx2 = p[0][0]+dy, p[0][1]+dx, p[1][0]+dy, p[1][1]+dx
                
                if is_out(ny1,nx2,ny2,nx2,len(board)):
                    continue
                    
                if board[ny1][nx1] == 1 or board[ny2][nx2] == 1:
                    continue
                
                npos = [[ny1, nx1], [ny2, nx2]]
                
                for i in range(2):
                    robot_pos = [[p[i][0], p[i][1]], [npos[i][0] , npos[i][1]]]
                    robot_pos.sort(key= lambda x : (x[0], x[1]))
                    
                    robot_pos = (tuple(robot_pos[0]), tuple(robot_pos[1]))
                    if robot_pos in visited:
                        continue
                    
                    visited.add(robot_pos)
                    q.append([robot_pos, t+1])
          
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        
        for dy, dx in direction:
            robot_pos = ((p[0][0]+dy, p[0][1]+dx),(p[1][0]+dy,p[1][1]+dx))
            
            if is_out(robot_pos[0][0], robot_pos[0][1], robot_pos[1][0], robot_pos[1][1], len(board)):
                continue
            if board[robot_pos[0][0]][robot_pos[0][1]] == 1 or board[robot_pos[1][0]][robot_pos[1][1]] == 1:
                    continue
        
            if robot_pos in visited:
                continue
            
            visited.add(robot_pos)
            q.append([robot_pos, t+1])
