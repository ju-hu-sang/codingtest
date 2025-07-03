def solution(num_list):
    answer = 0
    x=1
    for i in num_list:
        x *= i
        answer += i
    
    
    return 1 if x < (answer)**2 else 0