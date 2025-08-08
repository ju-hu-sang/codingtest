def solution(s):
    result ='' 
    new = list(set(s))
    for i in new:
        if s.count(i) ==1 :
            result += i
    if not result:
        return 0
    return ''.join(sorted(result))