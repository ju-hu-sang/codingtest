def solution(str_list):
    for i, j in enumerate(str_list):
        if j == 'r':
            return str_list[i+1:]
        elif j == 'l':
            return str_list[:i]
    return []
    