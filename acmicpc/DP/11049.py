T = int(input())


matrixs = []

dp = [[[0,0,0] for _ in range(T+1)] for _ in range(T+1)]

for i in range(1,T+1):
    matrixs.append(list(map(int, input().split())))

    dp[i][i][0] = matrixs[i-1][0]
    dp[i][i][1] = matrixs[i-1][1]
    
    for j in range(1,i):
        dp[i-j][i][0] = matrixs[i-1][0]
        dp[i-j][i][1] = matrixs[i-1][1]


for i in range(1, T+1):
    for j in range(1,  T-i+1):
        dp[j][i+j][2] = 9876543210
        
        for k in range(j, i+j):
            tmp_sum = dp[j][k][2] + dp[k+1][i+j][2] + dp[j][k][0] * dp[j][k][1] * dp[k+1][i+j][1]
            if dp[j][i+j][2] > tmp_sum:
                dp[j][i+j][2] = tmp_sum
                dp[j][i+j][0] = dp[j][k][0]
                dp[j][i+j][1] = dp[k+1][i+j][1]
                

print(dp[1][T][2])
    
    
    