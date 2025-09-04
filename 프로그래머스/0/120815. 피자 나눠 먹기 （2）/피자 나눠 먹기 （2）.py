def solution(n):
    if n == 6:
        return 1
    cnt = 1
    while True:
        if (6*cnt)%n == 0:
            break
        cnt +=1
    return cnt 