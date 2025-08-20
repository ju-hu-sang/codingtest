def solution(my_string):
    num = ''
    total = 0
    for i in my_string:
        if i.isdigit():
            num +=i
        else:
            if num:
                total += int(num)
                num=''
    if num:
        total +=int(num)
    return total