def solution(arr):
    cnt = 0
    for i in range(len(arr[0])):
        for j in range(len(arr[0])):
            if arr[i][j] == arr[j][i]:
                cnt +=1
    return 1 if cnt ==len(arr[0])*len(arr[0]) else 0