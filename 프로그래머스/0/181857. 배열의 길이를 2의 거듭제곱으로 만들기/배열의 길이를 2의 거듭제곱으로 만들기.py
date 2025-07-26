def solution(arr):
    answer = []
    i= 0
    j=0
    while len(arr) > j:
        j = 2**i
        i += 1
    answer.extend(arr+[0]*(j-len(arr)))    
    
    
    return answer