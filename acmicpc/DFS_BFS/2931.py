import sys
from collections import deque
blocks = {'|' : [[1,0],[-1,0]], '-' : [[0,1],[0,-1]], '+' : [[0,1],[0,-1],[1,0],[-1,0]],
          '1':[[1,0],[0,1]],'2':[[-1,0],[0,1]], '3':[[-1,0],[0,-1]], '4':[[1,0],[0,-1]]}

def bfs(start, city, R, C):
    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[start[0]][start[1]] = True
    q = deque()
    
    init_dir = [[0,1],[1,0],[-1,0],[0,-1]]
    
    for dy, dx in init_dir:
        y = dy + start[0]
        x = dx + start[1]
        
        if y >= R or y < 0 or x >= C or x < 0:
            continue
        if city[y][x] != '.' and city[y][x] != 'M' and city[y][x] != 'Z':
            q.append([y,x])
            visited[y][x] = True
            
    if not q:
        return True

    while q:
        py, px = q.popleft()
            
        for dir_y, dir_x in blocks[city[py][px]]:
            y = py + dir_y
            x = px + dir_x
            
            if y >= R or y < 0 or x >= C or x < 0:
                continue
            if city[y][x] == 'Z' or city[y][x] == 'M':
                continue
            
            if city[y][x] == '.':
                ans_dir = []
                
                for dir_y2, dir_x2 in init_dir:
                    y2 = y + dir_y2
                    x2 = x + dir_x2
                    if y2 >= R or y2 < 0 or x2 >= C or x2 < 0:
                        continue
                    
                    if city[y2][x2] == '.':
                        continue 
                    
                    if city[y2][x2] == 'M' or city[y2][x2] == 'Z':
                        ans_dir.append([dir_y2, dir_x2])
                    elif [-dir_y2, -dir_x2] in blocks[city[y2][x2]]:
                        ans_dir.append([dir_y2, dir_x2])
                
                if len(ans_dir) == 4:
                    ans_dir2 = []
                    for dir_y2, dir_x2 in ans_dir:
                        if city[y+dir_y2][x+dir_x2] != 'M' and city[y+dir_y2][x+dir_x2] != 'Z':
                            ans_dir2.append([dir_y2, dir_x2])
                    
                    if len(ans_dir2) == 4:
                        print(str(y+1) + ' ' + str(x+1) +' ' + '+')

                    else:
                        ans_keys = []
                        for keys in blocks:
                            if keys == '+':
                                continue
                            if ans_dir2[0] in blocks[keys]:
                                ans_keys.append(keys)

                        for keys in ans_keys:

                            if ans_dir2[1] in blocks[keys]:
                                print(str(y+1) + ' ' + str(x+1) +' ' + keys)
                    
                     
                    q.clear()
                    break
                
                elif len(ans_dir) == 2:
                    ans_keys = []
                    for keys in blocks:
                        if keys == '+':
                            continue
                        if ans_dir[0] in blocks[keys]:
                            ans_keys.append(keys)

                    for keys in ans_keys:

                        if ans_dir[1] in blocks[keys]:
                            print(str(y+1) + ' ' + str(x+1) +' ' + keys)
                    q.clear()
                    break
            
                
                      
            elif not visited[y][x]:
                visited[y][x] = True
                q.append([y, x])
    
    return False    
        


R, C = map(int,sys.stdin.readline().split())

m_pos = []
z_pos = []

city = []

for i in range(R):
    city.append(list(sys.stdin.readline()))
    
    for j in range(C):
        if city[i][j] == 'M':
            m_pos.extend([i,j])
        if city[i][j] == 'Z':
            z_pos.extend([i,j])
            
if bfs(m_pos,city,R,C):
    bfs(z_pos,city,R,C)
