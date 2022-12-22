import heapq


def bfs(r, c, start_pos, jail):
    direction = [[1,0], [-1,0], [0,1], [0,-1]]
    boards = [[[10001 for _ in range(c)] for _ in range(r)] for _ in range(3)]
    
    hq = []
    
    for i in range(3):
        heapq.heappush(hq, (0, start_pos[i]))
        boards[i][start_pos[i][0]][start_pos[i][1]] = 0
        while hq:
            dist , pos = heapq.heappop(hq)
            y1, x1 = pos[0], pos[1]
            
            if boards[i][y1][x1] < dist:
                continue
            
            for dir_y, dir_x in direction:
                y2, x2 = y1+dir_y, x1+dir_x
                
                if y2 >= r or y2 < 0 or x2 >= c or x2 < 0:
                    continue
                
                if jail[y2][x2] == '*':
                    continue
                
                dist2 = dist
                
                if jail[y2][x2] == '#':
                    dist2 += 1
                
                if boards[i][y2][x2] > dist2:
                    boards[i][y2][x2] = dist2
                    heapq.heappush(hq, (dist2, [y2,x2]))

        
        if i == 0:
            continue
        
        for j in range(r):
            for k in range(c):
                boards[0][j][k] += boards[i][j][k]

    min_door = 100001 
    
    for i in range(r):
        for j in range(c):
            ret = boards[0][i][j]
            if jail[i][j] == '*':
                continue
            if jail[i][j] == '#':
                ret  -= 2
        
            min_door = min(ret, min_door)
    
    return min_door
                        
            

T = int(input())

for _ in range(T):
    jail = []
    R, C = map(int, input().split())
    start_pos = []
    start_pos.append([0,0])
    
    jail.append(list('.'*(C+2)))
    
    for i in range(R):
        jail.append(list('.'+input()+'.'))
        
        for j in range(C+2):
            if jail[i+1][j] == '$':
                start_pos.append([i+1, j])
    
    jail.append(list('.'*(C+2)))
    
    print(bfs(R+2,C+2,start_pos, jail))