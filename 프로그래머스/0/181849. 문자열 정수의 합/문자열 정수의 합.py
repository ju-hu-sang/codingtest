def solution(num_str):
    num_str=  int(num_str)
    sum= 0
    while num_str !=0:
        sum += num_str % 10
        num_str //= 10
    
    return sum