from collections import deque

str1 = input()
str2 = input()


dp = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]


for i in range(1,len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            

i = len(str1)
j = len(str2)

print(dp[i][j])
ret = deque()

if dp[i][j] != 0:
    while dp[i][j] !=0:
        if str1[i-1] == str2[j-1]:
            ret.appendleft(str1[i-1])
            i-=1
            j-=1
        else:
            if dp[i][j-1] > dp[i-1][j]:
                j -=1
            else:
                i -= 1
                
    print(''.join(ret))