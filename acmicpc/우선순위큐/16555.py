from heapq import heappop, heappush;
import sys

N = int(sys.stdin.readline())

left_h = []
right_h = []
mid = int(sys.stdin.readline())
print(mid)

for _ in range(N-1):
    num = int(sys.stdin.readline())
    
    if mid <= num:
        heappush(right_h,num)
    elif mid > num:
        heappush(left_h, (-num, num))
    

    right_len = len(right_h)
    left_len = len(left_h)
    if (right_len - left_len) >= 2:
        pop_num = heappop(right_h)
        heappush(left_h, (-mid, mid))
        mid = pop_num
    elif (right_len - left_len) <= -1:
        _, pop_num = heappop(left_h)
        heappush(right_h, mid)
        mid = pop_num
    

    print(mid)