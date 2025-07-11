def solution(arr):
    answer = []
    for i in range(len(arr)):
        if arr[i] == 2 :
            answer.append(i)
    if 2 not in arr:
        return [-1]
    else:
        return  arr[min(answer):max(answer)+1]