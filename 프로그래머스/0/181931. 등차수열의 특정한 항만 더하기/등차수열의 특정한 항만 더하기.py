def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        bin = a + i*d
        if included[i]:
            answer += bin
    return answer