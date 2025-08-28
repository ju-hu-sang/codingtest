def solution(n):
    jjak = []
    for i in range(1,n+1):
        if i % 2 == 0:
            jjak.append(i)
    return sum(jjak)
        