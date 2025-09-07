def solution(emergency):
    answer = []
    n_emer = sorted(emergency, reverse=True)
    dic = {}
    for i in range(len(n_emer)):
        dic[n_emer[i]] = i+1
    for i in emergency:
        answer.append(dic[i])
    
    return answer