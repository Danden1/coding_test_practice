# 검색을 통해 풀었음. 

T = int(input())

INF = 987654321

for _ in range(T):
    l = int(input())
    
    dp = [[0 for _ in range(l+1)] for _ in range(l+1)]
    s = [0 for _ in range(l+1)]
    novels = list(map(int, input().split()))
    
    for i in range(1,l+1):
        s[i] = s[i-1] + novels[i-1]
    
    for i in range(1,l+1):
        

        for j in range(1,l-i+1):
            dp[j][i+j] = INF
            for k in range(j, i+j):
                dp[j][j+i] = min(dp[j][i+j], dp[j][k] + dp[k+1][i+j] + s[i+j] - s[j-1])
                
        
    print(dp[1][l])