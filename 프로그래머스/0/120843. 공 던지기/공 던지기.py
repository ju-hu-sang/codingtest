def solution(numbers, k):
    res=0
    if len(numbers) % 2 == 0:
        answer = numbers[::2]
        res+= answer[(k%len(answer))-1]
    else:
        answer = numbers[::2]+numbers[1::2]
        res += answer[(k%len(answer))-1]
    return res