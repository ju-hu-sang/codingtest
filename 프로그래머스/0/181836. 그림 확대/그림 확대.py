def solution(picture, k):
    res = []
    for li in picture:
        temp = ""
        for i in li:
            temp = temp +(i*k)
        for _ in range(k):
            res.append(temp)
        
    return res