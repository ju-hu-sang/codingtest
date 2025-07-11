def solution(arr, idx):
    answer = []
    for i in range(len(arr)):
        if arr[i] == 1 and ( i >=idx) :
            answer.append(i) 
    return min(answer) if answer else -1