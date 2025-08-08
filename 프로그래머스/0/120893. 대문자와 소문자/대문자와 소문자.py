def solution(my_string):
    ab = ''.join([ i.upper() if i.lower()==i else i.lower() for i in my_string ]) 
    return ab 