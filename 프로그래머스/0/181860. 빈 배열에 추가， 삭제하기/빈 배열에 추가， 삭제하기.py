def solution(arr, flag):
    answer = []
    for i, j in zip(arr, flag):
        if j:
            answer += [i]*i*2
        elif not j:
            answer = answer[:-i]
    
    return answer