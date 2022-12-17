from collections import deque

front_stack = deque(input())
back_stack = deque()

N = int(input())

for i in range(N):
    input_str = list(input().split(" "))
    
    
    if input_str[0] == 'P':
        front_stack.append(input_str[1])
        
    elif input_str[0] == 'L':
        if len(front_stack) == 0:
            continue
        pop_str = front_stack.pop()
        back_stack.appendleft(pop_str)
        
    elif input_str[0] == 'D':
        if len(back_stack) == 0:
            continue
        pop_str = back_stack.popleft()
        front_stack.append(pop_str)
    elif input_str[0] == 'B':
        if len(front_stack) == 0:
            continue
        front_stack.pop()
    
print(''.join(front_stack) + ''.join(back_stack))

    
