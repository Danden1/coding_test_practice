from collections import deque


def check_out(n,m,i,j):
    if i >=m-1 and i < n + m-1 and j >= m-1 and j < n + m-1:
        return False
    return True

def solution(key, lock):
    board = []
    cnt = 0
    #padding
    for i in range(len(lock) + (len(key)-1) * 2):
        tmp_list = []
        
        for j in range(len(lock) + (len(key)-1)*2):
            if check_out(len(lock), len(key), i, j):
                tmp_list.append(-1)
                
            else:

                if lock[i-len(key)+1][j-len(key)+1] == 1:
                    tmp_list.append(1)
                else:
                    cnt += 1
                    tmp_list.append(0)
            
        board.append(tmp_list)
    
    
    return check(key,board,cnt)




def check(key, board, cnt):
    m = len(key)
    direction = [[[0, m, 1],[0, m, 1]], # i j
                 [[0,m,1],[m-1,-1,-1]], #j i
                 [[m-1,-1,-1],[m-1,-1,-1]], # i j
                 [[m-1,-1,-1],[0,m,1]] # j i
                ]
    
    for i in range(4):
        di = direction[i][0]
        dj = direction[i][1]
        
        
        for n1 in range(len(board)-len(key)+1):
            for n2 in range(len(board)-len(key)+1):
                ret = 0
                
                b1,b2 = -1,-1
                flag = False
      
                for m1 in range(di[0],di[1],di[2]):
                    if flag:
                        break
                        
                    b1+=1
                    b2 = -1
                    for m2 in range(dj[0],dj[1],dj[2]):
                        b2+=1
                        if board[n1+b1][n2+b2] == -1:
                            continue
                        
                        if i %2 == 0:
                            if board[n1+b1][n2+b2] == 0 and key[m1][m2] ==1:
                                ret+=1
                            elif  board[n1+b1][n2+b2] == key[m1][m2]:
                                flag= True
                                break
                        else:
                            if board[n1+b1][n2+b2] == 0 and key[m2][m1] ==1:
                                ret+=1
                            elif board[n1+b1][n2+b2] == key[m2][m1]:
                                flag= True
                                break
                        
                        if ret == cnt:
                            return True

    return False