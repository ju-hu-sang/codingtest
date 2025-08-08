def solution(my_string, num1, num2):
    my_string = list(my_string)
    temp = my_string[num2]
    my_string[num2] = my_string[num1]
    my_string[num1] =temp
    return ''.join(my_string)