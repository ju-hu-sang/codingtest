def solution(strArr):
    dic1= {}
    for i in strArr:
        if len(i) not in dic1:
            dic1[len(i)] = 1
        else:
            dic1[len(i)] +=1
    return max(list(dic1.values()))
   