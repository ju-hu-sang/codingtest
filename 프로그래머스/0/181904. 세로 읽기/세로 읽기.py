def solution(my_string, m, c):
    a = ''
    for i in range(0,len(my_string),m):
        a += my_string[i:i+m][c-1]
    return a
    