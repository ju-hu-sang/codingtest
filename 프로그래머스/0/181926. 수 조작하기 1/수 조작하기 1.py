def solution(n, control):
    answer = 0
    w = control.count('w')
    s = control.count('s')
    d = control.count('d')
    a = control.count('a')
    answer += n+w-s+10*d-10*a
    return answer