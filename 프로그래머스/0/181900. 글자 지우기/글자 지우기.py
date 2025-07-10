def solution(my_string, indices):
    my_list = list(my_string)
    for i in sorted(indices, reverse=True):
        my_list.pop(i) 
    return ''.join(my_list)