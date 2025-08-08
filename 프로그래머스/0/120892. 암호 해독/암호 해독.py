def solution(cipher, code):
    a = cipher
    return  ''.join(a[i-1] for i in range(code, len(a)+1, code)) 