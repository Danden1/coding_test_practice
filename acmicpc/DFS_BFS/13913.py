from collections import deque


a, b = map(int, input().split())

end = 100000

visited = [-1 for _ in range(end+1)]
visited[a] = a


q = deque()
q.append([a,0])


move = [-1,1]

while q:
    cur_pos, time = q.popleft()
    
    if cur_pos == b:
        print(time)
        break
    
    for dx in move:
        nx_pos = cur_pos + dx
        if nx_pos < 0 or nx_pos > end:
            continue
        
        if visited[nx_pos]>=0:
            continue
        
        q.append([nx_pos, time+1])
        visited[nx_pos] = cur_pos
    
    nx_pos = cur_pos * 2
    if nx_pos > end:
        continue
    if visited[nx_pos]>=0:
        continue
    
    q.append([nx_pos, time+1])
    visited[nx_pos] = cur_pos
    
    


ans = deque()
cur_pos = b
while cur_pos != a:
    ans.appendleft(cur_pos)
    cur_pos = visited[cur_pos]
ans.appendleft(a)

print(' '.join(map(str,ans)))