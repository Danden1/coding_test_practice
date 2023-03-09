import sys


n = int(sys.stdin.readline())

houses = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

inf = 987654321

ans=inf

for i in range(3):
    dp = [[inf, inf, inf] for _ in range(n)]
    
    dp[0][i] = houses[0][i]
    
    for j in range(1,n):
        for k in range(3):
            dst = min(dp[j-1][(k+1)%3], dp[j-1][(k+2)%3])
            dp[j][k] = houses[j][k]+dst

    ans = min(min(dp[n-1]),ans)

print(ans)
