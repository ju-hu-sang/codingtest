def solution(n):
    cnt = 1
    while True:
        res = 1
        for i in range(1,cnt+1):
            res *= i
        if res >n:
            return cnt -1
            break
        cnt +=1
