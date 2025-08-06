def solution(s1, s2):
    cnt = 0
    for i in s1:
        b = s2.count(i)
        cnt += b
    return cnt if cnt else 0 