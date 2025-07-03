def solution(a, b, c):
    answer = 0
    if (a != b) and (b != c) and (c !=a):
        answer += (a+b+c)
    elif a == b ==c :
        answer += (a+b+c)*(a**2+b**2+c**2)*(a*a*a+b*b*b+c*c*c)
    else:
        answer += (a+b+c)*(a**2+b**2+c**2)
    return answer