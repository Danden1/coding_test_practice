N, E = map(int, input().split())

def div(ret ,e):
    if e == 1:
        return ret
    if e == 0:
        return 1
    
    ret = div(ret, e//2)
    
    if e % 2 == 1:
        ret = mul(mul(ret,ret),mat)
    else:

        ret = mul(ret,ret)
    
    return ret

def mul(mat1, mat2):
    ret = []
    
    for i in range(N):
        tmp_ret = [0 for _ in range(N)]
        for j in range(N):
            for k in range(N):
                tmp_ret[j] = (tmp_ret[j] + mat1[i][k] * mat2[k][j]) % 1000
                
        ret.append(tmp_ret)

    return ret
    
    
mat = []

for _ in range(N):
    mat.append(list(map(int, input().split())))
ret = div(mat,E)
if(E == 1):
    for i in range(N): 
        for j in range(N):
            ret[i][j] %= 1000
            
for i in range(N): 
    print(' '.join(map(str, ret[i])))


