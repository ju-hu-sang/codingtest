def solution(number):
    answer = 0
    for i in number :
        answer += int(i)
    if  int(number) %9 == int(answer) %9:
        return int(number)%9
    
    