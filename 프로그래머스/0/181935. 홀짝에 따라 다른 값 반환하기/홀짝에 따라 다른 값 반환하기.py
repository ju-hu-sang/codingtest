def solution(n):
    even = 0
    odd = 0
    if n % 2 == 1 :
        for i in range(1,n+1,2):
            odd += i
        return odd
    else:
        for i in range(2,n+2,2):
            even += i**2
        return even
            
        