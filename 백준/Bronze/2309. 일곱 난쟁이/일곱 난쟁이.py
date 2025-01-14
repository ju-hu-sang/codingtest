ddongjaru = [int(input()) for _ in range(9)]
ddongjaru_s = sum(ddongjaru)
found = False
for i in range(len(ddongjaru)):
    for j in range(i + 1, len(ddongjaru)):
        if ddongjaru_s - (ddongjaru[i] + ddongjaru[j]) == 100:            
            ddongjaru.pop(j)
            ddongjaru.pop(i)
            ddongjaru.sort()
            for ddong in ddongjaru:
                print(ddong)
            found = True
            break
    if found:
        break