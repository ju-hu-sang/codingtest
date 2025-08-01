def solution(A, B):
    cnt = 0
    if A==B :
        return 0
    for i in range(1,len(A)+1):
        cnt +=1
        C = A[-i:] + A[:-i]
        if C == B :
            return cnt
    if cnt == len(A):
        return -1
    
    