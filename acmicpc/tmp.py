from collections import deque

a = deque()
a.appendleft(3)

b = a
a = deque()

print(b,a)