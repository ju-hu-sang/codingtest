def solution(order):
    a_cnt = 0
    c_cnt = 0
    for i in order:
        if 'americano' in i:
            a_cnt +=1
        elif 'cafe' in i : 
            c_cnt +=1
        else:
            a_cnt +=1
    return a_cnt * 4500 + c_cnt*5000