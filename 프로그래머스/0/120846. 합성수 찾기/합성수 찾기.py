def solution(n):
    cnt = 1
    for i in range(2,n+1):
        cnt2=0
        for j in range(1,i+1):
            if i % j == 0:
                cnt2 +=1
        if cnt2 <=2 :
            cnt +=1
        cnt2 = 0
    return n-cnt
                
            