def solution(num_list):
    arr =[]
    for i in num_list:
        if i<0:
            arr.append(i)
            return num_list.index(i)
    if not arr:
        return -1