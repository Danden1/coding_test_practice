'''
이번 문제는 시간이 상당히 걸렸다.

cluster가 두 개 동시에 떨어지지 않는다는 조건을 잘 이용할 필요가 있다.

사실 고려안하고도 풀 수 있지만, 시간 복잡도나 메모리 사용량에 대해서 이 코드보다 비효율적이다.

'''


from collections import deque
import copy
DIR = [[0,1], [0,-1], [1,0], [-1,0]]

cave = []

R, C = map(int, input().split())

for _ in range(R):
    cave.append(list(input()))


def get_cluster(ay,ax):
    
    
    q = deque()
    visited = [[False for _ in range(C)] for _ in range(R)]
    flag = True

    for dir_y, dir_x in DIR:
        
        ret_q = deque()
        if not flag:
            break
        dir_y, dir_x = dir_y + ay, dir_x + ax
        
        if dir_y >= R or dir_y < 0 or dir_x >= C or dir_x < 0:
            continue
            
        if cave[dir_y][dir_x] == '.' or visited[dir_y][dir_x]:
            continue

        q.append([dir_y,dir_x])
        ret_q.append([dir_y,dir_x])
        visited[dir_y][dir_x] = True


        while q:
            y, x = q.popleft()
            
            for dir_y, dir_x in DIR:
                dir_y, dir_x = dir_y + y, dir_x + x
                
                if dir_y >= R or dir_y < 0 or dir_x >= C or dir_x < 0:
                    continue
                
                if visited[dir_y][dir_x] or cave[dir_y][dir_x] == '.':
                    continue
                
                ret_q.append([dir_y, dir_x])
                q.append([dir_y, dir_x])
                visited[dir_y][dir_x] = True
                
        flag = update_cave(ret_q)

            


def check_crash(cluster, cnt):
    q = copy.deepcopy(cluster)
    
    while q:
        y, x = q.popleft()
        y += cnt
        
        if y == R-1:
            return True
        
        
        dir_y, dir_x = y + 1, x
        
        if dir_y >= R or dir_y < 0 or dir_x >= C or dir_x < 0:
            continue
        
        if cave[dir_y][dir_x] == 'x':
            return True
            
    return False
    

def update_cave(cluster):
    crash = False
    cnt = 0

    while (not crash):
        
        for y,x in cluster:
            cave[y+cnt][x] = '.'
            
        crash = check_crash(cluster, cnt)
        
        if not crash:
            cnt+=1
        for y,x in cluster:
            cave[y+cnt][x] = 'x'
            
    if cnt == 0:
        return True
    return False
    

        
def remove_right(row):
    for i in reversed(range(C)):
        if cave[row][i] == 'x':
            return [row, i]
        
        
    return []

def remove_left(row):
    for i in range(C):
        if cave[row][i] == 'x':
            return [row, i]
        
        
    return []
        
N = int(input())

sticks = list(map(int, input().split()))

for i in range(len(sticks)):
    if i%2 == 1:
        pos = remove_right(R-sticks[i])
    else:
        pos = remove_left(R-sticks[i])
        
    if len(pos) == 0:
        continue
    cave[pos[0]][pos[1]] = '.'
    
    
    cluster = get_cluster(pos[0], pos[1])

for i in cave:
    print(''.join(i))
