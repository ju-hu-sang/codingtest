def solution(n):
    num = n //2
    yak = [1,n]
    for i in range(2,num+1):
        if n % i == 0:
            yak.append(i)
            yak.append(n//i)
    return sorted(set(yak))