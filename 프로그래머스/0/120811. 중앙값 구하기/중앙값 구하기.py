def solution(array):
    a = len(array)
    b = sorted(array)
    
    if a % 2 == 1:
        return b[a//2]
    else :
        return (b[a//2-1]+b[a//2])/2
