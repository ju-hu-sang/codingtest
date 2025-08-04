def solution(n):
    num = n//2
    yes = 0
    for i in range(num):
        if i*i == n:
            yes += 1
    return 1 if yes >0 else 2