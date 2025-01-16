N, B = map(int, input().split())
result=""

while N>0:
    s = N%B
    if s >=10:
        result = chr(s-10+ ord('A')) + result        # 역순으로 해야 진법이맞다.
    else:
        result = str(s)+result
    N = N//B
print(result)