def solution(s):
    answer = 1001
    
    if len(s)==1:
        return 1
    
    for i in range(1,len(s)//2 +1):
        
        sub_str = ''
        tmp_answer = 0
        tmp_count = 0
        j = 0
        while j < len(s)+1:
            
            if j == 0:
                sub_str = s[j:j+i]
            
            if sub_str == s[j:j+i]:
                tmp_count +=1
            else:
                if tmp_count == 1:
                    tmp_answer += i
                else:
                    tmp_answer += i + tmp_count//10+1
                tmp_count = 1
                
                sub_str=s[j:j+i]
            
            j+=i
        
        if tmp_count != 1:
            tmp_answer += i + 1
        
        tmp_answer += len(s) % i
        
        answer = min(answer, tmp_answer)
            
    
    return answer

print(solution(input()))