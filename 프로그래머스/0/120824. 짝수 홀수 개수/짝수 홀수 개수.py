def solution(num_list):
    jjak = []
    hor = []
    for i in num_list:
        if i%2 == 0:
            jjak.append(i)
        else:
            hor.append(i)
            
    return [len(jjak),len(hor)]