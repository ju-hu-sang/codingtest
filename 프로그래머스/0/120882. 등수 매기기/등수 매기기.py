def solution(score):
    
    total = [i+j for i, j in score]
    order = sorted(total, reverse=True)
    
    dic1 = {}
    for index, k in enumerate(order):
        if k not in dic1:
            dic1[k] = index+1
    return [dic1[k] for k in total]
    
        