import heapq
import sys

from collections import deque



def djk(board, s, n):

    hq = []
    
    dst = deque([987654321 for _ in range(n+1)])
    
    heapq.heappush(hq, (0, s))
    dst[s] = 0
    
    
    while hq:
        d, node = heapq.heappop(hq)
           
        if dst[node] < d:
            continue
        
        for i in board[node]:
            
            if board[node][i] + d < dst[i]:
                dst[i] = board[node][i] + d
                heapq.heappush(hq, (dst[i], i))
    
    return dst


T = int(sys.stdin.readline())


for _ in range(T):
    n, m , t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    
    board = [{} for _ in range(n+1)]
    
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        
        board[a][b] = d
        board[b][a] = d
    
    dst_condidate = deque()
    
    for _ in range(t):
        dst_condidate.append(int(sys.stdin.readline()))
    
    ss = djk(board, s, n)
    gg = djk(board, g, n)
    hh = djk(board, h, n)
    
    ans = []
    
    for dd in dst_condidate: 
        if ss[dd] == ss[g] + board[g][h] + hh[dd] or ss[dd] == ss[h] + board[h][g]+ gg[dd]:
            ans.append(dd)
            
    ans.sort()
    for w in ans:
        print(w, end=' ')
    print()