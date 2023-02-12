d_list = []
d_list.append(10)
d_list.append(20)
d_list.append(30)
d_list.append(40)

def solution(users, emoticons):
    answer = [0,0]
    discount = [0 for _ in range(len(emoticons))]
    dfs(users, emoticons, discount, 0, answer)
    return answer


def dfs(users, emoticons, discount, start, answer):
    if start == len(emoticons):
        tmp_answer = [0,0]
        for user in users:
            price = 0
            for i in range(len(emoticons)):
                if user[0] <= discount[i]:
                    price = price + (emoticons[i] * ((100-discount[i]) / 100))
                if price >= user[1]:
                    price = 0
                    tmp_answer[0]+=1
                    break
            tmp_answer[1] += price
        
        if tmp_answer[0] > answer[0]:
            answer[0] = tmp_answer[0]
            answer[1] = tmp_answer[1]
        elif tmp_answer [0] == answer[0] and tmp_answer[1] > answer[1]:
            answer[0] = tmp_answer[0]
            answer[1] = tmp_answer[1]
        return
    
    for j in d_list:
        discount[start] = j
        dfs(users, emoticons, discount, start+1, answer)
    
    
