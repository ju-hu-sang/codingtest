def solution(age):
    return ''.join(chr(ord('a')+int(ch)) for ch in str(age))