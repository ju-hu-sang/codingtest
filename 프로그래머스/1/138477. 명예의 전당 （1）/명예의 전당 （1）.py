def solution(k, score):
    pri = []
    result = []
    for i in score:
        pri.append(i)
        pri.sort(reverse=True)
        if len(pri)>k:
            pri = pri[:k]
        result.append(pri[-1])
    return result