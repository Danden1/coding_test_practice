from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    weak_len = len(weak)
    
    for i in range(weak_len):
        weak.append(weak[i]+n)
        
    dist_permus = list(map(list, permutations(dist, len(dist))))
    
    for start in range(weak_len):
        for dist_permu in dist_permus:
            num_friends = 0
            max_len = weak[start] + dist_permu[0]
            
            for i in range(weak_len):
                cur = i + start
                
                if max_len < weak[cur]:
                    num_friends += 1
                    
                    if num_friends >= len(dist):
                        break
                    
                    max_len = weak[cur] + dist_permu[num_friends]
                    
            answer = min(num_friends+1, answer)
            
    if answer == len(dist) + 1:
        return -1
            
    
    return answer
