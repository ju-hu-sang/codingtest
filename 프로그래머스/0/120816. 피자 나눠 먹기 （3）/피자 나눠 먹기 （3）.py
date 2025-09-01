def solution(slice, n):
    
    if n <2:
        return 1
    elif n % slice == 0:
        return n //slice
    elif n % slice != 0:
        return n//slice +1
    