def solution(n):
    cnt = 0 
    while n !=0 :
        c = n % 10
        n = n // 10 
        cnt += c
    return cnt