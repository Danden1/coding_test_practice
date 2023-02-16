dic = {i : "" for i in range(50*50)}
board = [[j*50 + i for i in range(50)] for j in range(50)]

def solution(commands):
    answer = []

    for command in commands:
        command = list(command.split())
        
        if command[0] == "UPDATE":
            if len(command) == 4:
                update1(int(command[1])-1, int(command[2])-1, command[3])
            else:
                update2(command[1], command[2])
        elif command[0] == "MERGE":
            merge(int(command[1])-1, int(command[2])-1, int(command[3])-1, int(command[4])-1)
        elif command[0] == "UNMERGE":
            unmerge(int(command[1])-1, int(command[2])-1)
        elif command[0] == "PRINT":
            answer.append(print2(int(command[1])-1,int(command[2])-1))
        
    return answer


def update1(r, c, value):
    dic[board[r][c]] = value

def update2(value1, value2):
    for key in dic:
        if dic[key] == value1:
            dic[key] = value2

            
def merge(r1, c1, r2, c2):
    if board[r1][c1] == board[r2][c2]:
        return

    if dic[board[r1][c1]] != "":
        
        tmp = board[r2][c2]
        for i in range(50):
            for j in range(50):
                if board[i][j] == tmp:
                    board[i][j] = board[r1][c1]
                    
    else:
        tmp = board[r1][c1]
        for i in range(50):
            for j in range(50):
                if board[i][j] == tmp:
                    board[i][j] = board[r2][c2]

        
        
def unmerge(r, c):
    group = board[r][c]
    tmp_value = dic[group]
    
    for i in range(50):
        for j in range(50):
            if board[i][j] == group:
                board[i][j] = 50*i + j
                dic[50*i + j] = ""
                
    dic[board[r][c]] = tmp_value

def print2(r, c):
    if dic[board[r][c]] == "":
        return "EMPTY"
    else:
        return dic[board[r][c]]
