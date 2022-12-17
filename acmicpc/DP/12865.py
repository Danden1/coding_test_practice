N, K = map(int, input().split())

info = {}

ans = 0

input_list = [(0 ,0)]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(N):
    w, v = map(int, input().split())
    input_list.append((w,v))

for i in range(1, N+1):

    w,v = input_list[i]

    for j in range(1, K+1) :
        if w > j:
            dp[i][j] = dp[i-1][j]
        
        
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
print(dp[N][K])
        