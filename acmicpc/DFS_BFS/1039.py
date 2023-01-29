#dfs.
import sys
ans = -1

def dfs(N, K, cnt):
    global visited
    global ans
    if N[0] == '0':
        return

    if K == cnt:
        ans = max(ans,int(''.join(N)))
        return
    

    
    for i in range(len(N)):
        for j in range(i+1,len(N)):
            tmp = N[j]
            N[j] = N[i]
            N[i] = tmp
            tmp_str = ''.join(N) 
            if tmp_str in visited[cnt]:
                N[i] = N[j]
                N[j] = tmp
                continue
            visited[cnt].add(tmp_str)
            dfs(N,K,cnt+1)
            
            N[i] = N[j]
            N[j] = tmp
        
N, K = sys.stdin.readline().split()

K = int(K)
N = list(N)
visited = [set() for _ in range(K)]
dfs(N, K, 0)
if len(N) == 1:
    ans=-1
print(ans)