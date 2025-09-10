def solution(balls, share):
    a = balls
    b = share
    
    up = 1
    down = 1
    for i in range(a,b,-1):
        up *= i
    for j in range(1,a-b+1):
        down*=j
    return up//down
        
        