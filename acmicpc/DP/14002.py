from collections import deque

N = int(input())

arr = list(map(int, input().split()))


dp = [1 for _ in range(N)]

ans = [-1 for i in range(N)]

for i in range(N):
    tmp_idx = -1
    
    for j in range(i):
    
       if arr[i] > arr[j]:
           if dp[i] < dp[j]+1:
                dp[i] = dp[j] + 1
                tmp_idx = j
    
    ans[i] = tmp_idx
    

max_len = max(dp)
print(max_len)

ret = deque()

max_idx = dp.index(max_len)

ret.appendleft(arr[max_idx])


while ans[max_idx] != -1:
    max_idx = ans[max_idx]
    ret.appendleft(arr[max_idx])
    

print(' '.join(list(map(str,ret))))
        
           

