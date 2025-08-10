def solution(my_string):
    an =''
    for i in my_string:
        if i not in an:
            an+=i
    return an
    