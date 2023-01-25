from collections import deque
import sys

input = sys.stdin.readline
N = int(input())

numbers = list(map(int, input().split()))

num_info = [[False for _ in range(len(numbers))] for _ in range(len(numbers))]

for i in range(1, len(numbers)):
    
    if i >= 2:
        if numbers[i] == numbers[i-2]:
            num_info[i][i-2] = True

    if numbers[i] == numbers[i-1]:
        num_info[i][i-1] = True
        
    for j in range(0,i-1):
        if j -1 >= 0:
            if num_info[i-1][j] and numbers[j-1] == numbers[i]:
                num_info[i][j-1] = True
                

M = int(input())


for _ in range(M):
    s, e = map(int, input().split())
    s -= 1
    e -= 1

    if num_info[e][s] or s == e:
        print(1)
    else:
        print(0)
    