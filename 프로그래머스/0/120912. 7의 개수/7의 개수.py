def solution(array):
    cnt1 = 0
    for i in array:
        i = str(i)
        cnt = i.count('7')
        cnt1 += cnt
    return cnt1 if cnt1 else 0