def solution(arr, k):
    answer = []
    temp = set()
    for i in arr:
        if i not in temp:
            temp.add(i)
            answer.append(i)
        if len(answer) == k:
            break
    if len(answer) < k:
        answer = answer+[-1]*(k-len(answer))
    return answer