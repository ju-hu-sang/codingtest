def solution(i, j, k):
    cnt=0
    k = str(k)
    for i in range(i,j+1):
        i = str(i)
        cnt += i.count(k)
    return cnt