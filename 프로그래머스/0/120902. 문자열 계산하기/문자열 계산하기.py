def solution(my_string):
    new = my_string.split()
    start = int(new[0])
    for i in range(1, len(new),2):
        cal = new[i]
        num = int(new[i+1])
        if cal == "+":
            start += num
        else:
            start -= num
    return start