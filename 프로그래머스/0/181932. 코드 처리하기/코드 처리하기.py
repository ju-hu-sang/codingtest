def solution(code):
    mode = 0
    ret = ''
    for i in range(len(code)):
        if code[i] == "1":
            mode = 1-mode
            continue
        if (i % 2 == 0) and mode == 0 :
            ret += code[i]
        elif (i % 2 != 0) and mode == 1:
            ret += code[i]
    return ret if ret else "EMPTY"
            
            
            
    