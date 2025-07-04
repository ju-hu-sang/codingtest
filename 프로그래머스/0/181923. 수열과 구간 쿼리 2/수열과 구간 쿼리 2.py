def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        bin = []
        for i in range(s, e+1):
            if arr[i]>k:
                bin.append(arr[i])
        if bin:
            answer.append(min(bin))
        else:
            answer.append(-1)
    
    return answer