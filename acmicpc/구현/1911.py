n, l = map(int,input().split())

board = []

for _ in range(n):
    board.append(list(map(int,input().split())))
    

board.sort(key= lambda x:x[0])

exceed = -1

total = 0

for start, end in board:
    if exceed >= start:
        start = exceed+1
        print(start)
        
    if start > end:
        continue
        
    need = end-start
    
           
    total += need//l
    
    if need % l:
        total += 1
        exceed = start + need//l * l + l-1
        
    print(total)

print(total)
        
        
    