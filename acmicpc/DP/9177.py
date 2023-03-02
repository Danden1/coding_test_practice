import sys


N = int(sys.stdin.readline())


for i in range(1,N+1):
    a,b,c = sys.stdin.readline().split()
    
    dp = [[False for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    
    dp[0][0] = True
    
    for j in range(1, len(a)+1):
        if c[j-1] == a[j-1]:
            dp[j][0] = True
            
    for j in range(1, len(b)+1):
        if c[j-1] == b[j-1]:
            dp[0][j] = True
    
    for j in range(1, len(a)+1):
        for k in range(1, len(b)+1):
            if c[j+k-1] == a[j-1] and c[j+k-1] == b[k-1]:
                dp[j][k] = True
            elif c[j+k-1] == a[j-1] and dp[j-1][k]:
                dp[j][k] = True
            elif c[j+k-1] == b[k-1] and dp[j][k-1]:
                dp[j][k] = True
                
    if dp[len(a)][len(b)]:
        print("Data set {}: yes".format(i))
    else:
        print("Data set {}: no".format(i))