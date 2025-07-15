def solution(s, skip, index):
    result =''
    eng = []
    for i in range(97, 123):
        if chr(i) not in skip:
            eng.append(chr(i))
    for char in s:
        start = eng.index(char)
        new_index = (start + index) % len(eng)
        result += eng[new_index]
    return result
            