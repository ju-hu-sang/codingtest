def solution(array, n):
    
    cnt = 110
    j = 0
    for i in array:
        cnt1 = abs(n-i)
        if cnt1 < cnt or (cnt1 == cnt and i < j):
            cnt = cnt1
            j =i
    return j